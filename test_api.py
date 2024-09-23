import requests

# The URL of your Flask API
url = 'http://127.0.0.1:8080/recommend'

# The data to send in the POST request
data = {
    "age": 30,
    "budget": 200,
    "group_size": 2,
    "city": "dubai",
    "attractions": {
        "shopping": 5,
        "outdoor": 4,
        "historical": 2,
        "landmark": 3,
        "kids": 1
    },
    "season": "winter",
    "num_days": 15,
    "user_latitude": 25.2048,  # Example latitude (Dubai)
    "user_longitude": 55.2708,  # Example longitude (Dubai)
    "transportation_mode": "taxi",  # Can be 'bus' or 'taxi'
    "excluded_places": []
}

# Send the POST request
response = requests.post(url, json=data)

# Print the status code and response
print("Status Code:", response.status_code)

try:
    response_json = response.json()
    print("Response JSON:", response_json)
except ValueError:
    print("Response content is not valid JSON:")
    print(response.text)
