import geopandas as gpd
import numpy as np
from shapely.geometry import Polygon
import matplotlib.pyplot as plt

# birds_gdf = gpd.read_file("../data/SU_hedgehogs_2019.geojson", driver="GeoJSON")
# birds_gdf.to_csv("../data/SU_hedgehogs_2019.csv")

# birds_gdf["coords"] = birds_gdf.geometry.apply(lambda x: x.coords[0])
# # bird_count = birds_gdf[["coords", "Genus"]].groupby(["coords"]).count()
# birds_gdf["count"] = 1
# bird_count = birds_gdf[["coords", "Genus", "count"]].groupby(["coords", "Genus"]).sum()


def box(left_x, bottom_y, size):
    return Polygon([
        (left_x, bottom_y),
        (left_x, bottom_y + size),
        (left_x + size, bottom_y + size),
        (left_x + size, bottom_y),
    ])

bl_corner = [400000, 100000]
easting_intervals = np.arange(400000, 500000, 10000)
northing_intervals = np.arange(100000, 200000, 10000)

geometries = []
for e in easting_intervals:
    for n in northing_intervals:
        geometries.append(
            box(e, n, 10000)
        )

gdf = gpd.GeoDataFrame(geometry=geometries, crs="epsg:27700")
gdf.to_file("SU_10km_grid.geojson", driver="GeoJSON")