from bs4 import BeautifulSoup
import requests
import json

url = "ここにスクレイピングしたいサイトのurl"
html_doc = requests.get(url).text
soup = BeautifulSoup(html_doc, 'html.parser')
# インデントの整理
# print(soup.prettify())

tags_a = soup.find_all('a')#aタグの指定

# aタグを取り出す
# for tag in tags_a:
#   print(tag)

#aタグのテキストを取り出す
# for tag in tags_a:
#   print(tag.string)

#aタグのhref属性を取り出す
# for tag in tags_a:
#   print(tag.get('href'))

#classがpost-titleのh3要素の取得
tags_post_title = soup.find_all("h3", {"class": "post-title"})
#指定した要素のテキストとurlを表示
for tag_post_title in tags_post_title:
  print(tag_post_title.a.string)
  print(tag_post_title.a.get('href'))