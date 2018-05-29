#Author :afeng
#Time   :2018/5/27 17:03
import requests

url="http://www.baidu.com"
response=requests.get(url)
#方式1
#print(response.content.decode())
#方式2
#print(response.content.decode("utf-8"))
#方式3
response.encoding="utf-8"
print(response.text)