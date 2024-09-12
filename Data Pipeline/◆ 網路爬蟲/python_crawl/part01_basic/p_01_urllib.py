from urllib import request
from bs4 import BeautifulSoup


# url = "http://httpbin.org/get"

# res = request.urlopen(url)

# print("res.read():", res.read())

# print(res.read().decode("utf8"))

# 需要 headers (user-agent)

url = "https://www.ptt.cc/bbs/joke/index.html"

# res = request.urlopen(url)

# 使用 headers (user-agent)
useragent = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36")
headers = {"User-Agent": useragent}
req = request.Request(url = url, headers = headers)
res = request.urlopen(req)

# print(res.read().decode("utf8"))

soup = BeautifulSoup(res, "html.parser")
print(soup)