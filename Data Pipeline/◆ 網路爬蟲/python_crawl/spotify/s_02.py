

import requests
from bs4 import BeautifulSoup

url = "https://api.spotify.com/v1/artists/4Z8W4fKeB5YxbusRsdQVPb"
access_token = "BQCiLFq-HrWMasZNmecWaOyE4G0g2FSaSM9iLolgdXEETEgxY3Fvvfwd6MFCvnnuepR9m9sgivl_pZZu7ARPq5OGbqYXeWl9HPkAAVcC-j2Il_KZFrE"  # 請用有效的訪問令牌替換這個值
headers = {"Authorization": f"Bearer {access_token}"}

res = requests.get(url, headers = headers)

soup = BeautifulSoup(res.text, "html.parser")

# 使用 prettify() 進行排版
print(soup.prettify())

