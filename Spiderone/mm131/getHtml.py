#Author :afeng
#Time   :2018/5/27 15:56
from urllib import request
from urllib import error
import  re

def getResponse(url):
    """获取HttpRespnose的对象
    通过request.urlopen获取"""
    #获得url的请求对象
    httpRequest=request.Request(url)
    #获得url的响应对象
    httpResponse=request.urlopen(url)
    return httpResponse

def getJpg(data):
    """获取图片的url地址返回list列表"""
    jpgList=re.findall(r'src="http.+?.jpg"',data)
    return jpgList

def downLoad(jpgUrl,n):
    try:
        request.urlretrieve(jpgUrl,'%s.jpg'%n)
    except Exception as e:
        print(e)
    finally:
        print('图片%s下载完成'%n)

global n
n=1
url="http://lol.tgbus.com/tu/"
data=getResponse(url).read().decode('utf-8')
#print(data)
jpgList=getJpg(data)
for jpgUrl in jpgList:
    print(jpgUrl)
    s=re.findall(r'http.+?.jpg',jpgUrl)
    downLoad(s[0],n)
    n=n+1