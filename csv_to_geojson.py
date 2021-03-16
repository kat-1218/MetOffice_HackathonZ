import pandas as pd
import geopandas as gpd


hedgehogs = pd.read_csv("data/Lisa L - hedgehog_small.csv")
hedgehogs = hedgehogs[hedgehogs["Genus"] == "Erinaceus"]

geometry = gpd.points_from_xy(x=hedgehogs["Longitude (WGS84)"],
                              y=hedgehogs["Latitude (WGS84)"])

hedgehogs_gdf = gpd.GeoDataFrame(hedgehogs, geometry=geometry, crs="EPSG:4326")
hedgehogs_gdf.to_file("data/hedgehogs.geojson", driver="GeoJSON")