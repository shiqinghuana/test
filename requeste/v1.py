import requests


# 手机号没法注册，抓包拿到cookie
cookies = 'anonymid=jwa3pytk-u110wo; depovince=GW; _r01_=1; JSESSIONID=abckrMR9VbzBc-5COYgSw; ick_login=9c5e0670-dd6d-4bd2-a2a4-5a137b87b55a; _de=1EDB9396C3D240E5; t=36e292e7f648b5306956bc86b80c5b092; societyguester=36e292e7f648b5306956bc86b80c5b092; id=971006872; xnsid=f87974f3; jebecookies=627007da-7e77-4ed8-879f-7968905599f0|||||; ver=7.0; loginfrom=null; jebe_key=91591787-7628-4f6f-8def-5708aabdce57%7C90afe7c6e6de96a4dfaab3f43d45d864%7C1559199390454%7C1%7C1559199389962; wp_fold=0'
# 转成字典
# cook = {}
# for i in cookies.split(';'):
#     cook[i.split("=")[0]] = i.split("=")[1]

cook = {i.split("=")[0] :i.split("=")[1] for i in cookies.split(';')}
print(cook)
header = {
    'User-Agent':""
}
url = "http://www.renren.com/971006872"  # 个人主页网址
url1 = "http://www.renren.com/971006872/newsfeed/origin" #原创内容板块

# requests访问
# 不带cookies
rsp = requests.get(url)
rsp1 = requests.get(url1)
print(rsp.request.headers)
print(rsp.status_code)
print(rsp.text)

print(rsp1.request.headers)
print(rsp1.status_code)
print(rsp1.text)
#结果  被重定向到登陆页

# 一个请求带cookies
rsp = requests.get(url,cookies=cook)
rsp1 = requests.get(url1)
print(rsp.request.headers)
print(rsp.status_code)
print(rsp.text)

print(rsp1.request.headers)
print(rsp1.status_code)
print(rsp1.text)
# 第二个请求被重定向到登录页

# 都带cookies
rsp = requests.get(url,cookies=cook)
rsp1 = requests.get(url1,cookies=cook)
print(rsp.request.headers)
print(rsp.status_code)
print(rsp.text)

print(rsp1.request.headers)
print(rsp1.status_code)
print(rsp1.text)
# 结果，正常访问
# session访问
session = requests.Session()  #实例化session
requests.utils.add_dict_to_cookiejar(session.cookies, cook)#设置全局cookies
# cooks = requests.utils.cookiejar_from_dict(cook)

rssp = session.get(url)
rssp1 = session.get(url1)
print(rssp1.request.headers)
print(rssp1.status_code)
print(rssp1.text)
#正常访问