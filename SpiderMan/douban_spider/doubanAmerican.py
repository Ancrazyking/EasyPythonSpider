#Author :afeng
#Time   :2018/5/28 10:06
from parse_url import parse
import json

class DoubanSpider:
    def __init__(self):
        "start={}格式化字符串"
        self.temp_url = "https://m.douban.com/rexxar/api/v2/subject_collection/filter_tv_american_hot/items?os=android&for_mobile=1&start={}&count=18&loc_id=108288&_=1527471975968"

    def  get_content_list(self,html_str):
        "获得json字符串响应,提取json字符串,转换为dict类型"
        "返回类型为解析过的json串,我猜应该是list类型"
        dict_json=json.loads(html_str)
        content_list=dict_json["subject_collection_items"]
        total=dict_json["total"]
        return content_list,total

    def save_content_list(self,content_list):
        "保存content_list到american.json文件中"
        with open("./american.txt","a",encoding="utf-8") as f:
            for content in content_list:
                f.write(json.dumps(content,ensure_ascii=False))
                f.write("\n")

    def run(self):
        "主要逻辑业务"
        num=0#数据的总量
        total=100
        while num<total+18:
            #1.将开始url格式化
            url=self.temp_url.format(num)
            print(url)
            #2.发送get请求,获取响应的json串,html_str
            html_str=parse.parse_url(url)
            #3.提取数据
            content_list,total=self.get_content_list(html_str)
            #4.保存
            self.save_content_list(content_list)
            #5.构造下一页的url地址,循环2-5步
            num+=18

if __name__=="__main__":
    douban=DoubanSpider()
    douban.run()