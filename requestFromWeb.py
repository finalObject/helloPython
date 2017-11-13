#python3!
#抓去网页图片
#执行之后都存在根目录，自己注意
import urllib.request as myUrl
import re

req = myUrl.urlopen('http://www.imooc.com/course/list')
buf = req.read()

buf = buf.decode('utf-8')
#写入文档的时候也需要先decode，不能强制转换
#buf = str(buf) 不知道为啥，这个不能用

list1 = re.findall(r'//img.*?jpg',buf)

i=0
for url in list1:
	url = 'http:'+url#加入http前缀
	myUrl.urlretrieve(url,str(i)+'.jpg')
	i = i+1