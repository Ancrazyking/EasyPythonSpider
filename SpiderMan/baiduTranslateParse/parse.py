#Author :afeng
#Time   :2018/5/28 9:07
import requests
import json
url="http://fanyi.baidu.com/basetrans"
headers={"User-Agent":"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Mobile Safari/537.36",
         }
def translate(data):
    query_string = {"query": data,
                    "from": "zh",
                    "to": "en"}
    response=requests.post(url,data=query_string,headers=headers)
    print(response)
    #print(response.content.decode())
    "由于该response的text文件返回的是一个json字符串"
    "可以将字符串转换为字典类型,通过Key,便于读取Value"
    json_dict=json.loads(response.content.decode())
    #print(json_dict)
    #print(type(json_dict))
    print("翻译的结果为:"+json_dict["trans"][0]["dst"])

if __name__=="__main__":
    while 1:
        data=input("请输入要翻译的中文,输入exit退出:")
        if  data=="exit":
            break;
        else:
            translate(data)
    print("bye")
