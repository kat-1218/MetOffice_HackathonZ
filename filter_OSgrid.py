import geopandas as gpd


birds_gdf = gpd.read_file("../data/gridded_10km_birds.geojson", driver="GeoJSON")
birds_gdf = birds_gdf[birds_gdf["OSGR 100km"] == "SU"]

birds_gdf.to_file("../data/SU_birds_2019.geojson", driver="GeoJSON")

hedgehogs_gdf = gpd.read_file("../data/gridded_10km_birds.geojson", driver="GeoJSON")
hedgehogs_gdf = hedgehogs_gdf[hedgehogs_gdf["OSGR 100km"] == "SU"]

hedgehogs_gdf.to_file("../data/SU_hedgehogs_2019.geojson", driver="GeoJSON")
