import pandas as pd
import geopandas as gpd


# hedgehogs = pd.read_csv("data/Lisa L - hedgehog_small.csv")
# hedgehogs = hedgehogs[hedgehogs["Genus"] == "Erinaceus"]

# geometry = gpd.points_from_xy(x=hedgehogs["Longitude (WGS84)"],
#                               y=hedgehogs["Latitude (WGS84)"])

# hedgehogs_gdf = gpd.GeoDataFrame(hedgehogs, geometry=geometry, crs="EPSG:4326")
# hedgehogs_gdf.to_file("data/hedgehogs.geojson", driver="GeoJSON")


birds = pd.read_csv("../data/Florence Hope - birds_uk_2018_2019.csv")
birds = birds[birds["Start date"].str.contains("2019")]

geometry = gpd.points_from_xy(x=birds["Longitude (WGS84)"],
                              y=birds["Latitude (WGS84)"])

birds_gdf = gpd.GeoDataFrame(birds, geometry=geometry, crs="EPSG:4326")
birds_gdf.to_file("birds_2019.geojson", driver="GeoJSON")