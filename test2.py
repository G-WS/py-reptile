from urllib import parse
#读取get和post的参数的一个类
from urllib import request
data=bytes(parse.urlencode({'word':'hello'}),encoding='utf8')
response=request.urlopen('http://httpbin.org/post',data=data)
print(response.read().decode('utf-8'))
reponse2=request.urlopen('http://httpbin.org/get',timeout=1)
print(reponse2.read())
import urllib
import socket
try:
    reponse3=urllib.request.urlopen('http://httpbin.org/get',timeout=0.1)
except urllib.error.URLError as e:
    if isinstance(e.reason,socket.timeout):
        print('Time out')
