# artist_ID

import requests

client_id = "45da58455f7f46d5b30b0b8a117fa452"
client_secret = "7dd2efbeaecd4fd08136e682f7610f48"

# 獲取 access_token
def get_access_token():
    url = "https://accounts.spotify.com/api/token"
    headers = {
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {
        "grant_type": "client_credentials"
    }
    response = requests.post(url, headers=headers, data=data, auth=(client_id, client_secret))
    return response.json().get('access_token')

access_token = get_access_token()

def get_artist_id(artist_name):
    url = f"https://api.spotify.com/v1/search?q={artist_name}&type=artist"
    headers = {
        "Authorization": f"Bearer {access_token}"
    }
    response = requests.get(url, headers=headers)
    data = response.json()

    # 提取歌手 ID
    artist_id = data['artists']['items'][0]['id'] if data['artists']['items'] else None
    return artist_id


artist_name = "王心凌"  # 替換為你要查找的歌手名稱
artist_id = get_artist_id(artist_name)
print(f"Artist ID: {artist_id}")

