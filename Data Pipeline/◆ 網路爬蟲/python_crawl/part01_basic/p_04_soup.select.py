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

# 以下在 Python Console 操作

# action_bar[0].find("div") 結果與 action_bar[0].div 一樣

# action_bar[0].div.div 可以得到下一層的 div

# action_bar[0].div.div.next_sibling 會得到一個換行符號 \n

# action_bar[0].div.div.next_sibling.next_sibling 得到該層的第 2 個 div

# action_bar[0].div.div.next_sibling.next_sibling.a 得到下一層的第一個 a

# action_bar[0].div.div.next_sibling.next_sibling.a.next_siblings 因為多個a, 所以會得到
# <generator object PageElement.next_siblings at 0x000002B868C2D180>

# 利用 for 迴圈 取得其他 a
# for i in action_bar[0].div.div.next_sibling.next_sibling.a.next_siblings:
#     print(i)