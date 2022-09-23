import requests
from time import sleep
import os
import string
import re

#存储字符
def recordone(data):
    fp=open('./MedicineData/finalData.txt',mode='a',encoding='utf-8')
    fp.write(data)

#存储数据
def record(data):
    fp = open('./MedicineData/finalData.txt',mode='a',encoding='utf-8')

    fp.write(data+"\n")

#User-Agent
headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
         'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36 Edg/85.0.564.41',
}

# 正则
ex1 = '<div id="PageContent">(.*?)'
name_ex = '<div class="PatentBlock" style="min-height: 180px;max-width: 1080px;">.*?MC=(.*?)/>.*?</a>'
auther_ex1='申请人：<a href=.*?target=_blank>(.*?)<font class='
auther_ex2="申请人：<a href=.*?target=_blank>.*?<font class='rh'>中药</font>(.*?)</a>"
right_ex1='当前权利人：.*?target=_blank>(.*?)<font class'
right_ex2='当前权利人：.*?</font>(.*?)</a>'
application_date_ex='申请日：(.*?)-'
classification_ex='主分类号：.*?Code/(.*?)target'
maindata_ex='摘要:(.*?)<br></span>'

# response = requests.get(url=url4,headers=headers)
# page_origin = response.txet
# response = open('./final.txt',mode='r',encoding='utf-8')
# print(response)

#从零开始，依次增加十
url="http://www.soopat.com/Home/Result?SearchWord=%E4%B8%AD%E8%8D%AF&FMZL=Y&SYXX=Y&WGZL=Y&FMSQ=Y&PatentIndex="
url2="http://www.soopat.com/Home/Result?Sort=&View=&Columns=&Valid=&Embed=&Db=&Ids=&FolderIds=&FolderId=&ImportPatentIndex=&Filter=&SearchWord=%E4%B8%AD%E8%8D%AF&FMZL=Y&SYXX=Y&WGZL=Y&FMSQ=Y"
url3="http://127.0.0.1/index.html"
url4="http://iantang.gitee.io/blog/python/"

#目录
index=0
index=int(index)

while index<=10000:
    response=requests.get(url=url+str(index),headers=headers)
    page_origin=response.text

    print("第"+str(index//10+1)+"页")
    sleep(3)
    index=index+10
    # #本地读取调试
    # with open('final.txt','r',encoding='utf-8') as f:
    #     page_origin=f.read()

    # 保存
    # with open('./final.txt', 'w', encoding='utf-8') as fp:
    #      fp.write(page_origin)
    # print(page_origin)

    name_list = re.findall(name_ex, page_origin, re.S)
    auther_list1 = re.findall(auther_ex1, page_origin, re.S)
    auther_list2 = re.findall(auther_ex2, page_origin, re.S)
    right_list1 = re.findall(right_ex1, page_origin, re.S)
    right_list2 = re.findall(right_ex2, page_origin, re.S)
    application_date_list = re.findall(application_date_ex, page_origin, re.S)
    classification_list = re.findall(classification_ex, page_origin, re.S)
    maindata_list = re.findall(maindata_ex, page_origin, re.S)

    i = 0
    i = int(i)
    for maindata_one in maindata_list:
        maindata_one = str(maindata_one)
        maindata_one = maindata_one.replace("<font class='rh'>", "")
        maindata_one = maindata_one.replace("</font>", "")
        # record(maindata_one)
    # exit(0)

    # print(name_list)
    # exit(0)

    for one_name in name_list:
        one_name = str(one_name)
        one_name = one_name.replace("'", "")
        record("专利名称：" + one_name)

        record("申请人：" + auther_list1[i] + '中药' + auther_list2[i])
        # record("当前权利人："+right_list1[i]+'中药'+right_list2[i])
        record("申请日期：" + application_date_list[i])
        record("分类号：" + classification_list[i])

        maindata_one = str(maindata_list[i])
        maindata_one = maindata_one.replace("<font class='rh'>", "")
        maindata_one = maindata_one.replace("</font>", "")


        record("摘要：" )
        pos = 0
        pos = int(pos)
        while (pos < len(maindata_one)):
            recordone(maindata_one[pos])
            pos = pos + 1
            if (pos % 50 == 0):
                recordone("\n")
        recordone("\n")
        record(
            "-----------------------------------------------------------------------------------------------------------")
        i = i + 1
        print("ok,记录了" + str(i+index-10) + "条")
        # exit(0)  # test

    # print(name_list)




