# 10-3 : 實作-以PTT 電影版為例-儲存內文

import requests
from bs4 import BeautifulSoup
import os
import re

# 宣告文章儲存的路徑
resource_path = "./res"
if not os.path.exists(resource_path):  # 若路徑沒有檔案則建立檔案
    os.mkdir(resource_path)

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

            article_url = "https://www.ptt.cc" + each_article.a['href']
            article_text = each_article.a.text

            # 對文章網址提出 requests
            article_res = requests.get(article_url, headers=headers)
            article_soup = BeautifulSoup(article_res.text, "html.parser")

            # 取得文章內容
            article_content = article_soup.select('div[id="main-content"]')[0].text.split("--")[0]
            # print(article_content)

            # 儲存文章內容
            with open(r"%s/%s.txt" % (resource_path, article_text), 'w', encoding="utf-8") as w:
                w.write(article_content)

        except AttributeError as err:
            print("==============")
            print(each_article)
            print(err.args)
            print("==============")
        except OSError as e:
            re.sub(r'[<>:"/\\|?*]', '', article_text)

    last_page_url = soup.select('a[class="btn wide"]')[1]['href']
    last_page_url = "https://www.ptt.cc" + last_page_url
    url = last_page_url