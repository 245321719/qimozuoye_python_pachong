import urllib
import urllib2
import re


x = 0
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = { 'User-Agent' : user_agent }
for i in range (2,5):
    url = 'https://www.qisuu.com/soft/sort01/index_'+str(i)+".html"
    print url
    try:
        request = urllib2.Request(url, headers=headers)
        response = urllib2.urlopen(request)
        html = response.read()
    except urllib2.URLError, e:
        if hasattr(e,"code"):
            print e.code
        if hasattr(e,"reason"):
            print e.reason

    content_pattern = re.compile('<a href=".*?.html"><img src="(.*?)"', re.S)
    content_list = re.findall(content_pattern, html)
    for item in content_list:
        print item

    
    for imgurl in content_list:
        urllib.urlretrieve("https://www.qisuu.com"+imgurl,'D:\E\%s.jpg' % x)
        x+=1

    input = raw_input()
    if input == "":
         print "ÏÂÒ»Ò³"
         continue
    else:
         print "½áÊø"
         break
