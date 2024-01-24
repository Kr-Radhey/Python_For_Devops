import requests

api_url = "https://api.gameofthronesquotes.xyz/v1/random"
response = requests.get(api_url)

data = response.json()
print(f"Today's quote of the day is from {data['character']['name']}, {data["character"]["house"]["name"]}")
print("Quote : ", data['sentence'])
