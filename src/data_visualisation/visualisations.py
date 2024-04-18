import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import os
import glob


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
    plt.savefig('src/data_visualisation/figures/matplotlib_figure.png')
    plt.close()

    # Seaborn
    sns.boxplot(x='type', y='distance', data=df)
    plt.title('Distribution of Distance by Activity Type')
    plt.savefig('src/data_visualisation/figures/seaborn_figure.png')
    plt.close()

    # Plotly
    fig = px.scatter(df, x='distance', y='moving_time', color='type')
    fig.write_image('src/data_visualisation/figures/plotly_figure.png')

    print('Data visualisation complete!')