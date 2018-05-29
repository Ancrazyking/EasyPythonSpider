#Author :afeng
#Time   :2018/5/28 13:40
import requests
headers={"User-Agent":"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Mobile Safari/537.36",
         "Referer":"https://m.douban.com/movie/horror"}

def _parse_url(url):
    """该方法用于解析url返回的文本"""
    print("*"*100)
    response=requests.get(url,headers=headers)
    return response.content.decode()

def parse_url(url):
    "处理异常,防止编码问题未获得返回的文本"
    try:
        html_str=_parse_url(url)
    except:
        html_str=None
    return html_str

if __name__=="__main__":
    url="https://m.douban.com/rexxar/api/v2/subject_collection/book_fiction/items?os=android&start=0&count=8&loc_id=0&_=1527485845858"
    html_str=parse_url(url)
    # dict_json=json.loads(html_str)
    # print(dict_json)
    # list_json=dict_json["subject_collection_items"]
    # print(list_json)
    # "果然,字典里面包含的是列表list"
    # print(type(list_json))#打印结果为<class 'list'>