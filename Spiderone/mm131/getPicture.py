#Author :afeng
#Time   :2018/5/27 18:00
import requests
import re
import retrying

def getResponse(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Mobile Safari/537.36"}
    response=requests.get(url,headers=headers,timeout=3)
    return response

def getJpgList(data):
    jpgList=re.findall(r'src="http.+?.jpg"',data)
    return jpgList

url="http://www.mm131.com"
response=getResponse(url)
data=response.content.decode("gbk")
#print(response.content.decode("gbk"))
jpgList=getJpgList(data)
for jpgUrl in jpgList:
    url=re.findall(r'http.+?.jpg',jpgUrl)
    print(url[0])
