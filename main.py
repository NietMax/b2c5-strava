import os
import shutil
from datetime import datetime
from pathlib import Path
import pandas as pd

from src.api_methods import get_methods
from src.api_methods import authorize
from src.data_preprocessing import main as data_prep

# used to f.e set the limit of fetched activities (default - 30)
ACTIVITIES_PER_PAGE = 200
# current page number with activities
PAGE_NUMBER = 1

GET_ALL_ACTIVITIES_PARAMS = {
    'per_page': ACTIVITIES_PER_PAGE,
    'page': PAGE_NUMBER
}

def main():
    # Clean the data directory
    folder = 'data'
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))

    token:str = authorize.get_acces_token()
    data:dict = get_methods.access_activity_data(token, params=GET_ALL_ACTIVITIES_PARAMS)
    df = data_prep.preprocess_data(data)
    # Convert the dictionary to a DataFrame
    df = pd.DataFrame(df)
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    df.to_csv(Path('data', f'my_activity_data={timestamp}.csv'), sep=',', index=False)
    # Transpose the DataFrame
    df = df.transpose()
    # Print the DataFrame as a table
    print(df)

if __name__ == '__main__':
    main()