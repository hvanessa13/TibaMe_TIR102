# Several Albums

import requests
from bs4 import BeautifulSoup

url = "https://api.spotify.com/v1/albums?ids=382ObEPsp2rxGrnsizN5TX%2C1A2GTWGtFfWp7KSQTwWOyo%2C2noRn2Aes5aoNVsU6iWThc&market=TW"
access_token = "BQCiLFq-HrWMasZNmecWaOyE4G0g2FSaSM9iLolgdXEETEgxY3Fvvfwd6MFCvnnuepR9m9sgivl_pZZu7ARPq5OGbqYXeWl9HPkAAVcC-j2Il_KZFrE"  # 請用有效的訪問令牌替換這個值
headers = {"Authorization": f"Bearer {access_token}"}

res = requests.get(url, headers = headers)
print(res.text)

# soup = BeautifulSoup(res.text, "html.parser")

# 使用 prettify() 進行排版
# print(soup.prettify())

