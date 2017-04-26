# 爬取SDCS学院招聘信息
import requests
import bs4
from bs4 import BeautifulSoup

def getHTMLText(url):
    try:
        # 使用get方法获取response对象
        r = requests.get(url, timeout = 30)
        # 抛出异常
        r.raise_for_status() 
        # 编码转换
        r.encoding = r.apparent_encoding 
        return r.text
    except:
        return ""
        
def parsePage(msgList, dateList, html):
    try:
        soup = BeautifulSoup(html, "html.parser")
        # 找到<div class="full-page-list">标签
        msgInfo = soup.find('div', attrs = {'class':'full-page-list'})
        # 在msgInfo中找到所有的<a>标签
        titleInfo = msgInfo.find_all('a')
        # 在msgInfo中找到所有的<span class="p-fl-time">标签
        dateInfo = msgInfo.find_all('span', attrs = {'class':'p-fl-time'})
        # 将所有标签的信息添加到列表中
        for i in range(len(titleInfo)):
            try:
                msgList.append(titleInfo[i].string)
                dateList.append(dateInfo[i].string)
            except:
                continue
    except:
        return ""

def printMsg(msgList, dateList):
    try:
        print('招聘信息')
        for i in range(len(msgList)):
            print(dateList[i])
            print(msgList[i])
    except:
        print("printMsg Error!")

def main():
    # 存储标题列表
    msgList = [] 
    # 存储日期列表
    dateList = [] 
    try:
        # 待爬取的url
        url = 'http://sdcs.sysu.edu.cn/orientation/recruitmentinfo' 
        # 获取HTML页面内容
        html = getHTMLText(url) 
        # 解析返回的HTML页面内容
        parsePage(msgList, dateList, html) 
        # 打印爬取的信息
        printMsg(msgList, dateList) 
    except:
        print("error")
        
main()