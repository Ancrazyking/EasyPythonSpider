#Author :afeng
#Time   :2018/5/27 21:42
import requests
import json

url="http://fanyi.baidu.com/basetrans"

data=input("请输入你要翻译的中文:")

query_string={"query":data,
              "from":"zh",
              "to":"en"
           }
headers={"User-Agent":"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Mobile Safari/537.36"}
response=requests.post(url,data=query_string,headers=headers)
print(response)
html_str=response.content.decode()

"json.loads(html)代表将json类型的数据转换为Python内置类型的字典类型"
dict_json=json.loads(html_str)
#print(dict_json)
#print(type(dict_json))#输出类型为dict类型
print("翻译结果为:"+dict_json["trans"][0]["dst"])