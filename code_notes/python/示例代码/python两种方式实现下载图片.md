

## request 实现

```python

#!/usr/bin/env python
# -*- coding: utf-8 -*-
#coding:utf-8
#
import requests
from bs4 import BeautifulSoup
import re

DownPath = "/jiaoben/python/meizitu/pic/"
import urllib
head = {'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}
TimeOut = 5
PhotoName = 0
c = '.jpeg'
PWD="/jiaoben/python/meizitu/pic/"
for x in range(1,4):
  site = "http://www.meizitu.com/a/qingchun_3_%d.html" %x
  Page = requests.session().get(site,headers=head,timeout=TimeOut)
  Coding =  (Page.encoding)
  Content = Page.content#.decode(Coding).encode('utf-8')
  ContentSoup = BeautifulSoup(Content)
  jpg = ContentSoup.find_all('img',{'class':'scrollLoading'})
  for photo in jpg:
    PhotoAdd = photo.get('data-original')
    PhotoName +=1
    Name =  (str(PhotoName)+c)
    r = requests.get(PhotoAdd,stream=True)
    with open(PWD+Name, 'wb') as fd:
        for chunk in r.iter_content():
                fd.write(chunk)
print ("You have down %d photos" %PhotoName)


```


## urllib 实现

```python

#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
import urllib

def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    print html
    return html

def getImg(html):
    #reg = r'src=*"(.*?\.jpg)"'
    reg = r"(http:.*?\.jpg)"
    print reg
    imgre = re.compile(reg)
    imglist = re.findall(imgre,html)
    num = 0
    for imgurl in imglist:
        #print imgurl
        urllib.urlretrieve(imgurl,'%s.jpg' % num)
        num+=1
    return imglist

html = getHtml("http://jandan.net/pic")
print getImg(html)


```
