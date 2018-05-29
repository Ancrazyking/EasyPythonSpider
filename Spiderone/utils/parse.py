#Author :afeng
#Time   :2018/5/27 19:13

import re
import requests
from retrying import retry

'''
专门请求url地址的方法
'''
headers = {
    "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Mobile Safari/537.36"}

@retry(stop_max_attempt_number=3)
def _parse_url(url):
    print("*"*100)
    response=requests.get(url,headers=headers,timeout=5)
    return  response.content.decode()

def parse_url(url):
    try:
        html_str=_parse_url(url)
    except:
        html_str=None
    return html_str

if __name__=="__main__":
    url="http://www.baidu.com"
    url1="www.baidu.com"
    print(parse_url(url1))


