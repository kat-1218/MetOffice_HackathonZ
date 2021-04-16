## import packages
import geopandas as gpd 
import pandas as pd
import matplotlib.pyplot as plt
import datetime as dt

## load in County level boundary (OS data)
boundaries = gpd.read_file(r"C:\Users\*****\Documents\OS_zoomstack_sample\gb_boundary_line_ceremonial counties.geojson")
## convert boundaries to lat/long
boundaries_WGS84 = boundaries.to_crs(4326)

## import species data e.g. bird data

species_data = pd.read_csv(r"C:\Users\*****\Documents\OS_zoomstack_sample\- birds_uk_2018_2019_sample.csv")
## turn into point data with lat/long
species_geometry = gpd.points_from_xy(species_data['Longitude (WGS84)'], species_data['Latitude (WGS84)'])
species_gdf = gpd.GeoDataFrame(species_data, geometry=species_geometry, crs='EPSG:4326')
#species_gdf.plot()
#plt.show()

## calculate number of species in an area 

boundary_species = gpd.sjoin(boundaries_WGS84, species_gdf)
boundary_species = boundary_species.drop(labels=['OSGR 100km', 'OSGR 10km', 'OSGR 2km', 'OSGR 1km'], axis=1)

datetime = pd.to_datetime(boundary_species['Start date'])
boundary_species['Start date'] = datetime
boundary_species['Year'] = boundary_species['Start date'].dt.year
boundary_species['Month'] = boundary_species['Start date'].dt.month

# count per species for each boundary area
species_grouped = boundary_species.groupby(['Name','Common name', 'Year'])['fid'].count()
# Number of species for each boundary area
species_values = boundary_species.groupby(['Name', 'Year'])['Common name'].nunique()
species_values = species_values.reset_index()
species_values.set_index('Name', inplace=True)

species_prevelance = boundaries_WGS84.join(species_values, on='Name')

print(species_prevelance)
## Map the data for each month, with number of species as metric for choropleth map

for year in set(species_prevelance['Year']):
    plot = species_prevelance[species_prevelance['Year'] == year].plot("Common name")
    plt.savefig(fr"C:\Users\*****\Documents\OS_zoomstack_sample\{year}.png")

## calculate change in species numbers between time steps

