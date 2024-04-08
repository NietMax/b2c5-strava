# General imports for calling the Strava API
import requests


def get_strava_data():
    url = "https://www.strava.com/api/v3/athlete"
    headers = {"Authorization": "Bearer f2852e3c857f6aa06aa4771c09510da7d29ab91e"}

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return response.json()
        print("Success! Code" + str(response.status_code))
    else:
        return None


data = get_strava_data()
if data is not None:
    print(data)
else:
    print("Failed to get data from Strava API | Or no data available")
