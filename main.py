import requests

# URL of the API
url = "https://date.nager.at/api/v3/PublicHolidays/2026/za"

# Make a GET request
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse JSON response
    data = response.json()

    for holidays in data:
        print(holidays["date"], holidays["name"])
else:
    print(f"Error: {response.status_code}")