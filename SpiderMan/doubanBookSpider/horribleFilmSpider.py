#Author :afeng
#Time   :2018/5/28 13:54
import json
from doubanBookSpider import parse

class HorribleFilmSpider:

    def __init__(self):
        "临时的url,通过格式化字符串可以获取所有get请求的url"
        self.tempUrl="https://m.douban.com/rexxar/api/v2/subject_collection/filter_movie_horror_hot/items?os=android&for_mobile=1&start={}&count=18&loc_id=108288&_=1527486737606"

    def get_content_list(self,html_str,num):
        """获取响应内容的解析,得到我们想要的数据"""
        dict_json=json.loads(html_str)#将json类型转换为dict类型
        list_json=dict_json["subject_collection_items"][0]["title"]#从字典中取到我们想要的
        total=dict_json["total"]#数据的总条数
        return list_json,total

    def save_content_list(self,content_list):
        """将获取到的有关的电影的信息写入到包下的./horror.txt中"""
        with open("./horror.txt","a",encoding="utf-8") as f:
            for content in content_list:
                f.write(json.dumps(content,ensure_ascii=False))
                f.write("\n")

    def  run(self):
        """主要逻辑写在run方法里面"""
        num=0#开始的start的值,用于格式化url的
        total=100
        while num<total+18:
            url=self.tempUrl.format(num)#获得开始请求url
            html_str=parse.parse_url(url)#获得解析到的响应文本
            content_list,total=self.get_content_list(html_str)
            self.save_content_list(content_list)
            num=num+18


if __name__=="__main__":
    film=HorribleFilmSpider()
    film.run()


