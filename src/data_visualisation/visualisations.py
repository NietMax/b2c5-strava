import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import os
import glob
import geopandas as gpd
import contextily as ctx
import xyzservices.providers as xyz
from shapely.geometry import LineString
from src.data_preprocessing.main import preprocess_geo_data


def visualize_data():
    # Find all CSV files in the data directory
    csv_files = glob.glob('data/*.csv')

    for csv_file_path in csv_files:
        # Read the CSV file
        df = pd.read_csv(csv_file_path)

    # Create the directory if it doesn't exist
    if not os.path.exists('src/data_visualisation/figures'):
        os.makedirs('src/data_visualisation/figures')

    # Matplotlib
    df['type'].value_counts().plot(kind='bar')
    plt.xlabel('Activity Type')
    plt.ylabel('Count')
    plt.title('Distribution of Activity Types')
    plt.xticks(rotation=0)
    plt.savefig('src/data_visualisation/figures/matplotlib_figure.png')
    plt.close()

    # Seaborn
    ax = sns.boxplot(x='type', y='distance', data=df)
    ax.set_xlabel('Type of Activity')
    ax.set_ylabel('Distance (m)')
    plt.title('Distribution of Distance by Activity Type')
    plt.savefig('src/data_visualisation/figures/seaborn_figure.png')
    plt.close()

    # Plotly
    #fig = px.scatter(df, x='distance', y='moving_time', color='type')
    #fig.update_layout(title_text='Scatter plot of Distance vs Moving Time')
    #fig.update_xaxes(title_text='Type of activity')
    #fig.update_yaxes(title_text='Moving time (s)')
    #fig.write_image('src/data_visualisation/figures/plotly_figure.png')

    # Geopandas
    df = preprocess_geo_data(csv_files)

    # Create GeoDataFrames for the start and end points
    gdf_start = gpd.GeoDataFrame(df, geometry=gpd.points_from_xy(df.start_longitude, df.start_latitude))
    gdf_end = gpd.GeoDataFrame(df, geometry=gpd.points_from_xy(df.end_longitude, df.end_latitude))

    # Set the initial CRS to WGS84
    gdf_start.crs = "EPSG:4326"
    gdf_end.crs = "EPSG:4326"

    # Convert the CRS to Web Mercator
    gdf_start = gdf_start.to_crs(epsg=3857)
    gdf_end = gdf_end.to_crs(epsg=3857)

    # Create a GeoDataFrame for the lines
    gdf_lines = gpd.GeoDataFrame(df, geometry=[LineString(xy) for xy in zip(gdf_start.geometry, gdf_end.geometry)])
    gdf_lines.crs = "EPSG:3857"

    # Create the plot
    fig, ax = plt.subplots(figsize=(10, 10))

    # Adjust subplot parameters to make the axes take up the whole figure
    plt.subplots_adjust(left=0, right=1, bottom=0, top=1)

    # Remove the border
    ax.set_frame_on(False)

    # Plot the start points in green
    gdf_start.plot(ax=ax, color='green', alpha=0.5, edgecolor='k')

    # Plot the end points in red
    gdf_end.plot(ax=ax, color='red', alpha=0.5, edgecolor='k')

    # Plot the lines
    gdf_lines.plot(ax=ax, color='blue')

    # Add the basemap
    ctx.add_basemap(ax, source=xyz.OpenStreetMap.Mapnik)
    ax.set_axis_off()

    plt.savefig('src/data_visualisation/figures/geopandas_plot.png', dpi=1500, bbox_inches='tight', pad_inches=0)

    print('Visualizations saved to src/data_visualisation/figures directory.')
