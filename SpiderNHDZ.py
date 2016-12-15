#!/usr/bin/python
# -*- coding:utf-8 -*-
import urllib
import urllib2
import re
import sys

reload(sys)
sys.setdefaultencoding('utf8')

page = 2
url = 'http://www.qiushibaike.com/hot/page/' + str(page)
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = {'User-Agent': user_agent}
try:
    request = urllib2.Request(url, headers=headers)
    response = urllib2.urlopen(request)
    content = response.read().decode('utf-8')
    pattern = re.compile('<div.*?class="author.*?>.*?<a.*?</a>.*?<a.*?>.*?<h2>(.*?)<.*?>.*?</a>.*?<div.*?class' +
                         '="content.*?<span>(.*?)</span>.*?<div.*?class="main-text.*?>(.*?)<div', re.S)
    # 将</br>替换为\t
    replaceBr = re.compile('<br/>')

    items = re.findall(pattern, content)

    for item in items:
        # haveImg = re.search("img",item[3])
        # if not haveImg:
        print '昵称 ' + item[0]
        str = item[1]
        str = re.sub(replaceBr, "\n", str)
        print '内容:\n' + str  # item[1]
        print '神评论 ' + item[2]
except urllib2.URLError, e:
    if hasattr(e, "code"):
        print e.code
    if hasattr(e, "reason"):
        print e.reason
