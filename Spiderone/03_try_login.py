#Author :afeng
#Time   :2018/5/27 19:25
import  requests
url="http://www.renren.com/966149094/profile"
headers = {
    "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Mobile Safari/537.36"
    ,"Cookie":"anonymid=jhoqmwo2jec6jk; depovince=GW; _r01_=1; JSESSIONID=abcFQryf46NcZe9FnwHow; ick_login=36b01246-b871-4a2e-9156-61f672702d60; t=bc3a654912806c62c1d92edbc2c066a84; societyguester=bc3a654912806c62c1d92edbc2c066a84; id=966149094; xnsid=5ea2bd84; ver=7.0; loginfrom=null; jebe_key=56b356cc-fe8e-4dd8-bcb2-133d8a155db4%7C0c8cb5cc6a032091698d2ebae7269473%7C1527420635151%7C1%7C1527420636417; wp_fold=0; jebecookies=c9c74bc0-091f-4460-b102-8fc83a27c236|||||; XNESSESSIONID=86ecf776516e; WebOnLineNotice_966149094=1"}
response=requests.get(url,headers=headers)
with open("./renrencookie.html","w",encoding="utf-8") as f:
    f.write(response.content.decode())