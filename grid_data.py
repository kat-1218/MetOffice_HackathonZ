import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
from shapely.geometry import Point
import numpy as np


hedgehogs_gdf = gpd.read_file("data/hedgehogs_2019.geojson", driver="GeoJSON")
hedgehogs_gdf.to_crs({'init' :'epsg:27700'}, inplace=True)


GRID_SIZE = 10000

HALF_STEP = GRID_SIZE / 2

def round_coord(x, y, to_nearest):
    return round_down(x, to_nearest), round_down(y, to_nearest)

def round_down(x, to_nearest):
    return to_nearest * np.floor(x / to_nearest)

gridded_points = []
for row in hedgehogs_gdf.itertuples():
    x, y = row.geometry.coords[0]
    grid_x, grid_y  = round_coord(x, y, GRID_SIZE)
    gridded_points.append(
        Point(grid_x + HALF_STEP, grid_y + HALF_STEP)
    )

hedgehogs_gdf["geometry"] = gridded_points

# Save
# hedgehogs_gdf.to_file("data/gridded_10km_hedgehogs.geojson", driver="GeoJSON")

# Plot
# hedgehogs_gdf.plot()
# plt.show()