from urllib import request, parse

url = 'http://httpbin.org/post'
headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate,sdch",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Host": "httpbin.org",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"

}
#头部有问题，缺少cookie
dict = {'name': 'value'}
data=bytes(parse.urlencode(dict),encoding='utf8')
req=request.Request(url=url,data=data,headers=headers,method='post')
response=request.urlopen(req)
print(response.read().decode('utf_8'))