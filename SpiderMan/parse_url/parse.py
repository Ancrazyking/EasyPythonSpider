#Author :afeng
#Time   :2018/5/28 10:03
import requests
import retrying

headers={"User-Agent":"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Mobile Safari/537.36",
         "Referer":"https://m.douban.com/tv/american"}

def _parse_url(url):
    print("*"*100)
    response=requests.get(url,headers=headers,timeout=5)
    return response.content.decode()

def parse_url(url):
    "该函数用于处理异常,防止读取失败,html_str返回None"
    try:
        html_str=_parse_url(url)
    except:
        html_str=None
    return html_str



if __name__=="__main__":
    url="http://www.baidu.com"
    print(parse_url(url))
