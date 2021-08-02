import requests
import key
from datetime import datetime

USERNAME = "mischevouspython"
PIXELA_TOKEN = key.PIXELA_TOKEN
GRAPH_ID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"
user_params = {
    "token": PIXELA_TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_config = {
    "id": GRAPH_ID,
    "name": "Python Coding",
    "unit": "hour",
    "type": "float",
    "color": "ajisai"
}
headers = {
    "X-USER-TOKEN": PIXELA_TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# # print(response.text) == https://pixe.la/v1/users/mischevouspython/graphs/graph1.html

# HTTP POST
# today = datetime.today().date().isoformat().replace("-", "")
# today = datetime.today()
today = datetime(year=2021, month=4, day=1)

pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "4.5"
}

# response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
# print(response.text)

# HTTP PUT
pixel_update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"
pixel_update_data = {
    "quantity": "0.8"
}

response = requests.put(url=pixel_update_endpoint, json=pixel_update_data, headers=headers)
response.raise_for_status()
print(response.text)
