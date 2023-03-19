import requests

url = "http://www.google.com"
res = requests.get(url)
print(res)
print(res.text)