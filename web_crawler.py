import urllib.request
from urllib import request,parse
import urllib
import http.cookiejar
from bs4 import BeautifulSoup

word=input("书名：")
title_url = "http://lib.ecust.edu.cn/books/query?field=title&key="+urllib.parse.quote(word)+"&form_build_id=form-igUepfuscRSQoiltLD6UPAWZUQGFSaSzy-gGvfFZoFE&form_id=ecust_lib_form_book_query&op=%E6%90%9C%E7%B4%A2"
page_info = urllib.request.urlopen(title_url).read()
page_info = page_info.decode('utf-8')
soup=BeautifulSoup(page_info)
print(soup.prettify())

