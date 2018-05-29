#Author :afeng
#Time   :2018/5/27 22:23
import json
import requests

url="https://m.douban.com/rexxar/api/v2/subject_collection/filter_tv_american_hot/items?os=android&for_mobile=1&start=0&count=18&loc_id=108288&_=1527431239327"
headers={
    "User-Agent":"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Mobile Safari/537.36",
    "Referer":"https://m.douban.com/tv/american"
}
response=requests.get(url,headers=headers)
print(response)
#print(response.content.decode())#是个字符串
json_str=response.content.decode()
"将json字符串转换为Python类型的字典"
json_dict=json.loads(json_str)
print(json_dict)
with open("./douban.txt","w",encoding="utf-8",) as f:
    "将字典转换为json字符串,可以读写"
    "ensure_ascii=False可以写中文"
    "indent=2,能够让下一行在上一行的基础上空格"
    f.write(json.dumps(json_dict,ensure_ascii=False,indent=2))
