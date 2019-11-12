#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time   : 2017/5/3 14:27
# @Author : Lyrichu
# @Email  : 919987476@qq.com
# @File   : save_images.py
'''
@Description:保存知乎某个问题下所有答案的图片
'''
from __future__ import print_function  # 使用python3的print方法
from zhihu_oauth import ZhihuClient
import re
import os
import urllib.request

client = ZhihuClient()
# 登录
client.load_token('token.pkl')  # 加载token文件
id = 24400664  # https://www.zhihu.com/question/24400664(长得好看是一种怎么样的体验)
question = client.question(id)
print(u"问题:", question.title)
print(u"回答数量:", question.answer_count)
# 建立存放图片的文件夹
os.mkdir(question.title + u"(图片)")
path = question.title + u"(图片)"
index = 1  # 图片序号
for answer in question.answers:
    content = answer.content  # 回答内容
    re_compile = re.compile(r'<img src="(https://pic\d\.zhimg\.com/.*?\.(jpg|png))".*?>')
    img_lists = re.findall(re_compile, content)
    if (img_lists):
        for img in img_lists:
            img_url = img[0]  # 图片url
            urllib.request.urlretrieve(img_url, path + u"/%d.jpg" % index)
            print(u"成功保存第%d张图片" % index)
            index += 1
