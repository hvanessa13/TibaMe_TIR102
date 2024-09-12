# 10-2 : 實作-以PTT 電影版為例-多頁爬取
# 方法1 : 按上一頁觀察url變化

import requests
from bs4 import BeautifulSoup

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36"}
page_number = 10246
while page_number >= 10244:
    url = f"https://www.ptt.cc/bbs/movie/index{page_number}.html"

    res = requests.get(url, headers = headers)

    soup = BeautifulSoup(res.text, "html.parser")

    # 使用 prettify() 進行排版
    # print(soup.prettify())

    article_title_html = soup.select('div[class="title"]')
    # print(article_title_html)

    for each_article in article_title_html:
        # 文章刪除會報錯, 使用 try_except
        try:
            print(each_article.a.text)
            print("https://www.ptt.cc" + each_article.a['href'])
        # 被刪除的文章, 印出 each_article 和錯誤訊息
        except AttributeError as err:
            print(each_article)
            print(err.args)
        print()

    page_number -=1
