# -*- coding: utf-8 -*-
import json;
import urllib.parse
import urllib.request

page = 1
weiboId = 4099122430616799
fpath = 'D:/学习/Python学习/微博评论.txt'

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
}

comments = []

for page in range(1, 50):
    # 格式化URL
    dataURL = 'http://m.weibo.cn/api/statuses/repostTimeline?id=%d&page=%d' % (weiboId, page);
    # 通过一个特定的请求头请求一个Response对象
    req = urllib.request.Request(dataURL, headers=headers)
    response = urllib.request.urlopen(req)
    # 得到json原始数据
    jsonString = response.read()
    # 对原始数据进行解析
    jsonObject = json.loads(jsonString.decode('utf8'))
    for data in jsonObject['data']:
        try:
            text = data['text']
            # 跳过'转发微博'的评论内容
            if(text=='转发微博'):
                continue
            comments.append(text)
        except:
            print("")
    
with open(fpath, 'a', encoding='utf-8') as f:
    for i in range(len(comments)):
        f.write(comments[i]+'\n')