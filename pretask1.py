import requests

url = "http://www.baidu.com"
headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.3 Safari/605.1.15"}
res = requests.get(url,headers = headers)
print(res)
html = res.content.decode()

with open ("baidu-unlogin.html","w",encoding="utf-8") as f:
    f.write(html)

#print(html)

url2 = "https://courses.zju.edu.cn/user/index"
headers_for_login = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.3 Safari/605.1.15"
                     ,"Referer":"https://zjuam.zju.edu.cn/",
                     "Host":"courses.zju.edu.cn",
                     "Cookie":""}
res_login = requests.get(url2,headers=headers_for_login)
print(res_login)
with open ("zjuam-login.html","w",encoding="utf8") as f:
    f.write((res_login.content.decode()))
