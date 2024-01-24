import requests, time

url = "https://api.seriesquotes.10cyrilc.me/quote/"
response = requests.get(url)

data = (response.json())

print(f"Today's quote is from '{data[0]["author"]}' from series '{data[0]["series"]}' : '{data[0]["quote"]}'")

time.sleep(25)   #putting sleep for 25 secs to hold screen when user runs exe file.