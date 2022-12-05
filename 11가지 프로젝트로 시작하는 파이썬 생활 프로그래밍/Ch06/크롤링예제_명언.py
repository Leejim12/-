import os,re,usecsv
import requests
import urllib.request as ur
from bs4 import BeautifulSoup as bs

url = 'https://quotes.toscrape.com/'
# urllib.request.urlopen(url) ## 이미 import 저렇게 해 놨으니
html = ur.urlopen(url)
html
# Out[3]: <http.client.HTTPResponse at 0x2175d2a2340>
    # 
html.read()[:100]
## 자료의 일부가 출력됨

html = ur.urlopen(url) ## 다시, html을 불러옴
soup= bs(html.read(),'html.parser') ## 파싱 하기 쉬운 형태로 변환

soup

type(html)
type(soup)

soup = bs(ur.urlopen(url).read(),'html.parser')

soup

quote = soup.find_all('span')
quote[0]

quote[0].text

for i in quote:
    i.text
    
soup.find_all('div',{"class":"quote"})
print(soup.find_all('div',{"class":"quote"})[0].text)

for i in soup.find_all('div',{"class":"quote"}):
    print(i.text)
    