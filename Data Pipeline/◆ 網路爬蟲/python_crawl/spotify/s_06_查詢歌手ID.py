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


# 查詢歌手 ID
def get_artist_id(artist_name, access_token):
    url = f"https://api.spotify.com/v1/search?q={artist_name}&type=artist"
    headers = {
        "Authorization": f"Bearer {access_token}"
    }
    response = requests.get(url, headers=headers)
    data = response.json()

    # 提取歌手 ID
    artist_id = data['artists']['items'][0]['id'] if data['artists']['items'] else None
    return artist_id


# 主函數
def main():
    access_token = get_access_token()

    artist_names = [
    "V",
    "Jimin",
    "Bestards",
    "ILLIT",
    "BABYMONSTER",
    "Lee Young Ji",
    "(G)I-DLE",
    "邱軍",
    "Firdhaus",
    "NewJeans",
    "aespa",
    "Billie Eilish",
    "承桓",
    "KISS OF LIFE",
    "高爾宣 OSN",
    "Jung Kook",
    "张韶涵",
    "Sabrina Carpenter",
    "LISA",
    "Stray Kids",
    "Taylor Swift",
    "卢卢快闭嘴",
    "ZQS",
    "ZICO",
    "LE SSERAFIM",
    "NAYEON",
    "Karencici",
    "Energy",
    "JOYCE 就以斯",
    "Jay Chou",
    "ØZI",
    "颜人中",
    "Patrick Brasca",
    "WeiBird",
    "Nicky Lee",
    "Cyndi Wang",
    "Capper",
    "The Kid LAROI",
    "Jolin Tsai",
    "政学Zed-X",
    "elijah woods",
    "Benson Boone",
    "陳華",
    "王宇宙Leto",
    "*NSYNC",
    "keshi",
    "EggPlantEgg",
    "Ronghao Li",
    "The Chainsmokers",
    "小阿七",
    "David Tao",
    "向思思",
    "Dhruv",
    "李浩瑋 Howard Lee",
    "en",
    "Stefanie Sun",
    "Ariana Grande",
    "Kendrick Lamar",
    "Tanya Chua",
    "XG",
    "王赫野",
    "Tommy Richman",
    "IVE",
    "ENHYPEN",
    "sodagreen",
    "Xiao Bing Chih",
    "IN-K",
    "阿冗",
    "JJ Lin",
    "Chappell Roan",
    "J.Tajor",
    "Eric Chou",
    "TRASH",
    "芒果醬 Mango Jump",
    "告五人",
    "郑润泽",
    "A-Lin",
    "Justin Bieber",
    "苏星婕",
    "Mixer",
    "张远",
    "YOASOBI",
    "One Direction",
    "G.E.M.",
    "曾瑋中",
    "David Guetta",
    "Post Malone",
    "周星星",
    "Rachel Liang",
    "Kenshi Yonezu",
    "Myles Smith",
    "YUQI",
    "RIIZE",
    "Fish Leong",
    "OneRepublic",
    "Lewis Capaldi",
    "LBI利比",
    "Sophie Chen",
    "Power Station",
    "Vaundy",
    "吕口口",
    "GooGoo",
    "Shi Shi",
    "Tyson Yoshi",
    "Tate McRae",
    "Teddy Swims",
    "SEVENTEEN",
    "隊長",
    "Gyubin",
    "詹雯婷",
    "TAEYEON",
    "Eason Chan",
    "大泫"
    ]  # 替換為你的歌手名稱列表
    artist_ids = {"artist": "artist_id"}

    for artist in artist_names:
        artist_id = get_artist_id(artist, access_token)
        artist_ids[artist] = artist_id

    # print(artist_ids)

        


if __name__ == "__main__":
    main()
