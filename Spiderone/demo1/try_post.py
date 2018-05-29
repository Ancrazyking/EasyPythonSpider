#Author :afeng
#Time   :2018/5/27 17:11
import requests
url="http://fanyi.baidu.com/basetrans"

data={"query":"你好,世界","from":"zh","to":"en"}
headers={"User-Agent":"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Mobile Safari/537.36"}
response=requests.post(url,data=data,headers=headers)
print(response.content.decode())