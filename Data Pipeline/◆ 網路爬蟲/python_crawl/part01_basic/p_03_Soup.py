from urllib import request
from bs4 import BeautifulSoup

url = "https://www.ptt.cc/bbs/joke/index.html"

useragent = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36")
headers = {"User-Agent": useragent}
req = request.Request(url = url, headers = headers)
res = request.urlopen(req)

soup = BeautifulSoup(res, "html.parser")
# findAll 和 select 會得到一樣結果
# action_bar = soup.findAll("div", {"id": "action-bar-container"})
action_bar = soup.select('div[id = "action-bar-container"]')

print(action_bar)
print()

# 取出內層標籤
tmp_div = action_bar[0].find("div")
print("other <div>:")
print(tmp_div)
print()

tmp_a = action_bar[0].find("a")
print("other <a>:")
print(tmp_a)
print()

# 取出內容
tmp_text_in_a = tmp_a.text
print("Text in <a> tag:")
print(tmp_text_in_a)
print()

# 另一種做法 取出內容
tmp_text_in_a = tmp_a.string
print("Text in <a> tag:")
print(tmp_text_in_a)
print()

# 取出屬性
tmp_url = tmp_a["href"]
print("url:")
print(tmp_url)
print()
print("https://www.ptt.cc" + tmp_url)

