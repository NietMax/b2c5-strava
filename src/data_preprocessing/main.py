import pandas as pd
import ast
import glob


def preprocess_data(data: dict) -> pd.DataFrame:

    return pd.json_normalize(data)


def preprocess_geo_data(path_to_csv: list):
    # Find all CSV files in the data directory
    csv_files = glob.glob('data/*.csv')

    for csv_file_path in csv_files:
        # Read the CSV file
        df = pd.read_csv(csv_file_path)

        # Convert string representations of lists into actual lists
        df['start_latlng'] = df['start_latlng'].apply(ast.literal_eval)
        df['end_latlng'] = df['end_latlng'].apply(ast.literal_eval)

        # Remove rows where 'start_latlng' or 'end_latlng' are empty
        df = df[df['start_latlng'].apply(lambda x: bool(x)) & df['end_latlng'].apply(lambda x: bool(x))]

        # Separate the latitude and longitude values
        df['start_latitude'], df['start_longitude'] = zip(*df['start_latlng'])
        df['end_latitude'], df['end_longitude'] = zip(*df['end_latlng'])

    return df
