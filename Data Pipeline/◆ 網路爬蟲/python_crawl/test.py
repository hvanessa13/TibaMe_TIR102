import requests

url = "https://kma.kkbox.com/charts/weekly/song?terr=tw&lang=tc"

res = requests.get(url)

print(res.text)