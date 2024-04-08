
# General imports for calling the Strava API
import requests
import pandas as pd

def get_strava_data():
    url = "https://www.strava.com/api/v3/activities/"
    headers = {"Authorization": "Bearer f2852e3c857f6aa06aa4771c09510da7d29ab91e"}

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        print("Success! Code" + str(response.status_code))
        return response.json()
    else:
        return None

data = get_strava_data()
if data is not None:
    # Convert the data to a pandas DataFrame and print it
    df = pd.DataFrame([data])
    print(df)
else:
    print("Failed to get data from Strava API | Or no data available")
