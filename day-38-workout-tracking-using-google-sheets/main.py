# Workout Tracking Using Google Sheets

import requests
from key import NUTRI_APP_ID, NUTRI_API_KEY, SHEETY_USERNAME, BEARER_AUTHENTICATION
from datetime import datetime

GENDER = "female"
WEIGHT_KG = 57
HEIGHT_CM = 168
AGE = 28

# ------------------------ API ENDPOINTS ------------------------
nutri_api_endpoint = f"https://trackapi.nutritionix.com/v2/natural/exercise"
sheety_api_endpoint = f"https://api.sheety.co/{SHEETY_USERNAME}/workoutTracking/workouts"

# -------------------- HTTP REQUESTS HEADERS --------------------
nutri_headers = {
    "x-app-id": NUTRI_APP_ID,
    "x-app-key": NUTRI_API_KEY,
    "x-remote-user-id": "0"
}
sheety_headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {BEARER_AUTHENTICATION}"
}

# -------------------- HTTP REQUESTS BODY --------------------
user_input = input("Tell me which exercises you did? ")
# user_input = "I ran for 10 mins, walked for 15 mins, and swam for 1 hour"
exercise_data = {
    "query": user_input,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

nutri_exercise_response = requests.post(url=nutri_api_endpoint, json=exercise_data, headers=nutri_headers)
result = nutri_exercise_response.json()

today = datetime.now()

for workout in result["exercises"]:
    workout_list = {
        "workout": {
            "date": today.strftime("%d/%m/%Y"),
            "time": today.strftime("%H:%M:%S"),
            "exercise": workout["name"].title(),
            "duration": workout["duration_min"],
            "calories": workout["nf_calories"]}
    }
    post_to_google_sheet_response = requests.post(url=sheety_api_endpoint, json=workout_list, headers=sheety_headers)
    print(post_to_google_sheet_response.text)
