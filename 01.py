import json
import requests

url = "https://enterpriseapi.benlai.com/Special/Login"

dicts = {
    "info": [{"key": "col1", "value": "13646"}, {"key": "col2", "value": "卢银彬"}, {"key": "col3", "value": "06116919"}],
    "code": "ty"}
data = json.dumps(dicts)
header = {
    "Host": "enterpriseapi.benlai.com",
    "Connection": "keep-alive",
    "Accept": "application/json, text/plain, */*",
    "Origin": "http://jc.benlai.com",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36 QBCore/3.53.1159.400 QQBrowser/9.0.2524.400 Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36 MicroMessenger/6.5.2.501 NetType/WIFI WindowsWechat",
    "Content-Type": "application/json",
    "Referer": "http://jc.benlai.com/ty",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.8,en-US;q=0.6,en;q=0.5;q=0.4",
}

POST
https: // feper.benlai.com / api / v1 / report / web
HTTP / 1.1
Host: feper.benlai.com
Connection: keep - alive
Content - Length: 735
Origin: http: // jc.benlai.com
User - Agent: Mozilla / 5.0(Windows
NT
6.1;
WOW64) AppleWebKit / 537.36(KHTML, like
Gecko) Chrome / 53.0
.2785
.116
Safari / 537.36
QBCore / 3.53
.1159
.400
QQBrowser / 9.0
.2524
.400
Mozilla / 5.0(Windows
NT
6.1;
WOW64) AppleWebKit / 537.36(KHTML, like
Gecko) Chrome / 39.0
.2171
.95
Safari / 537.36
MicroMessenger / 6.5
.2
.501
NetType / WIFI
WindowsWechat
content - type: application / json
Accept: * / *
Referer: http: // jc.benlai.com / ty
Accept - Encoding: gzip, deflate
Accept - Language: zh - CN, zh;
q = 0.8, en - US;
q = 0.6, en;
q = 0.5;
q = 0.4

s= {"time": 1559574127670,
 "preUrl": "",
 "errorList": [],
 "performance": {"dnst": 0, "tcpt": 0, "wit": 3, "domt": 78, "lodt": 79, "radt": 1, "rdit": 0, "uodt": 0, "reqt": 1,
                 "andt": 1},
 "resourceList": [{
                      "name": "https://enterpriseapi.benlai.com/Special/GetOrderTemplates?list=105881&code=ty&t=1559574122425.0.4112155745038042",
                      "method": "GET", "type": "xmlhttprequest", "duration": "546.05", "decodedBodySize": 0}, {
                      "name": "https://enterpriseapi.benlai.com/Special/GetOrderTemplates?list=105881&code=ty&t=1559574122425.0.4112155745038042",
                      "method": "GET", "type": "xmlhttprequest", "duration": "3791.13", "decodedBodySize": 0}],
 "addData": [], "markUser": "2XP3cGJP341559571621365", "markUv": "6G5ZFi5ebe1559571621366", "screenwidth": 624,
 "screenheight": 687, "appId": "pcT3T8h1548228082303"}

HTTP / 1.1
200
OK
Date: Mon, 03
Jun
2019
15: 05:42
GMT
Content - Type: application / json;
charset = utf - 8
Content - Length: 23
Connection: keep - alive
Vary: Origin
Access - Control - Allow - Origin: *
x - frame - options: SAMEORIGIN
x - xss - protection: 1;
mode = block
x - content - type - options: nosniff
x - download - options: noopen
x - readtime: 1
X - Kong - Upstream - Latency: 93
X - Kong - Proxy - Latency: 0
Via: kong / 0.10
.0 - 1017

{"code": 1000, "data": {}}

he = requests.post(url, headers=header, data=data, verify=False)
print(he.text)
print(he.url)
