#Author :afeng
#Time   :2018/5/28 14:59
import requests
from lxml import etree

url="https://movie.douban.com/chart"
headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36"}

response=requests.get(url,headers=headers)
html_str=response.content.decode()
#print(html_str)

