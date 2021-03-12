import requests
import re

content = requests.get('http://www.cnu.cc/discoveryPage/hot-人像').text
print(content)
#  <div class="grid-item work-thumbnail">
# <a href="http://www.cnu.cc/works/420829" class="thumbnail" target="_blank">
# <div class="title">90年代</div>
# <div class="author">AKA十一11</div>
partten = re.compile(r'<a href="(.*?)".*?title">(.*?)</div>', re.S)
results = re.findall(partten, content)
print(results)
for result in results:
    url, name = result
    print(url, re.sub('\s', '', name))  # 去掉多余的空格和换行符，/s表示空白符，可以将空白符匹配成空值
