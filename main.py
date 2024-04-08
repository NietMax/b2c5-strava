# General imports for calling the Strava API
import requests
import os
from dotenv import load_dotenv

# Load the environment variables
load_dotenv()


def get_strava_data():
    url = "https://www.strava.com/api/v3/athlete"
    bearer_token = os.getenv("BearerToken")
    headers = {"Authorization": f"Bearer ${bearer_token}"}

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        print("Success! Code" + str(response.status_code))
        return response.json()
    else:
        print("Failed to get data from Strava API | Or no data available")
        return None


data = get_strava_data()
if data is not None:
    print(data)
else:
    print("Failed to get data from Strava API | Or no data available")
