import subprocess
from datetime import datetime
from pathlib import Path
import shutil

import pandas as pd

from src.api_methods import authorize
from src.api_methods import get_methods
from src.data_preprocessing import main as data_prep

ACTIVITIES_PER_PAGE = 200
PAGE_NUMBER = 1

GET_ALL_ACTIVITIES_PARAMS = {
    'per_page': ACTIVITIES_PER_PAGE,
    'page': PAGE_NUMBER
}


def clean_data_directory(directory: Path):
    for item in directory.iterdir():
        if item.is_file() or item.is_symlink():
            item.unlink()
        elif item.is_dir():
            shutil.rmtree(item)


def main():
    data_dir = Path('data')
    data_dir.mkdir(exist_ok=True)  # Create the directory if it doesn't exist
    clean_data_directory(data_dir)

    token = authorize.get_acces_token()
    data = get_methods.access_activity_data(token, params=GET_ALL_ACTIVITIES_PARAMS)
    df = data_prep.preprocess_data(data)
    df = pd.DataFrame(df)
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    df.to_csv(data_dir / f'my_activity_data={timestamp}.csv', sep=',', index=False)
    df = df.transpose()
    print(df)


if __name__ == '__main__':
    main()
