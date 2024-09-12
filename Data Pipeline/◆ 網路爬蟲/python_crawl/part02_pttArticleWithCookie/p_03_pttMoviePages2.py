# 10-2 : 實作-以PTT 電影版為例-多頁爬取
# 方法2 : 如果無法觀察到url變化 -> 開發人員工具 element

import requests
from bs4 import BeautifulSoup

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36"}
url = "https://www.ptt.cc/bbs/movie/index.html"

for i in range(0,3): # 印出3頁的資料
    res = requests.get(url, headers = headers)

    soup = BeautifulSoup(res.text, "html.parser")

    # 使用 prettify() 進行排版
    # print(soup.prettify())

    article_title_html = soup.select('div[class="title"]')
    # print(article_title_html)

    for each_article in article_title_html:
        try:
            print(each_article.a.text)
            print("https://www.ptt.cc" + each_article.a['href'])
        except AttributeError as err:
            print("==============")
            print(each_article)
            print(err.args)
            print("==============")

    last_page_url = soup.select('a[class="btn wide"]')[1]['href']
    last_page_url = "https://www.ptt.cc" + last_page_url
    url = last_page_url