
import requests

url = "https://accounts.spotify.com/api/token"
client_id = "45da58455f7f46d5b30b0b8a117fa452"
client_secret = "7dd2efbeaecd4fd08136e682f7610f48"

# 設置請求的資料
data = {"grant_type": "client_credentials"}

# 設置基本認證
response = requests.post(url, data=data, auth=(client_id, client_secret))

# 檢查回應狀態
if response.status_code == 200:
    access_token = response.json().get("access_token")
    token_type = response.json().get("token_type")
    print("Access Token:", access_token)
    print("token_type:", token_type)
else:
    print("Error:", response.status_code, response.text)

