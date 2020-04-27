#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
import time
import json
import requests
import logging

import tkinter as tk  # 使用Tkinter前需要先导入
 
# # 第1步，实例化object，建立窗口window
# window = tk.Tk()
 
# # 第2步，给窗口的可视化起名字
# window.title('达人推小帮手')
 
# # 第3步，设定窗口的大小(长 * 宽)
# window.geometry('500x300')  # 这里的乘是小x
 
# # 第4步，在图形界面上设定输入框控件entry框并放置
# e = tk.Entry(window,width=12, show = None)#显示成明文形式
# e.place(x=10, y=15)
 
# # 第5步，定义两个触发事件时的函数insert_point和insert_end（注意：因为Python的执行顺序是从上往下，所以函数一定要放在按钮的上面）
# def insert_point(): # 在鼠标焦点处插入输入内容
#     var = e.get()
#     t.insert('insert', var)
# def insert_end():   # 在文本框内容最后接着插入输入内容
#     var = e.get()
#     t.insert('end', var)
# def insert_time():   # 在文本框内容最后接着插入输入内容
    
#     t.insert('end', time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())+'\n' )
 
# # 第6步，创建并放置两个按钮分别触发两种情况
# b1 = tk.Button(window, text='商家检查', width=10, height=2, command=insert_point)
# b1.place(x=10, y=100)
# b2 = tk.Button(window, text='达人检查', width=10,   height=2, command=insert_end)
# b2.place(x=10, y=150)
# b2 = tk.Button(window, text='关系修复', width=10,   height=2, command=insert_time)
# b2.place(x=10, y=200)
 
# # 第7步，创建并放置一个多行文本框text用以显示，指定height=3为文本框是三个字符高度
# t = tk.Text(window, width=50,height=20)
# t.place(x=120, y=15)
 
# # 第8步，主窗口循环显示
# window.mainloop()


class TalentHelper:
    def __init__(self):
        
        self.window = tk.Tk()
        self.base_url = 'http://api.etest.darentui.com/' # api/v1/home/statistic/
        self.token = None
        self.window.title('达人推小帮手')
        self.window.geometry('500x300')      
        self.login()
        self.window.mainloop()

    def send_post(self, url, data):        
        headers = {
            "Content-Type": "application/json"
        }
        req_obj = requests.post(url, data=json.dumps(data), headers=headers)
        logger.info(json.loads(req_obj.content))
        logger.info(json.dumps(data))

    def login(self):
        url = self.base_url + 'api/v1/accounts/login/'
        username = tk.Entry(self.window, width=20, show = None)
        password = tk.Entry(self.window, width=20, show = None)
        submit = tk.Button(self.window, text='登录确定', width=10, height=1)
        username.place(x=244, y=60)
        password.place(x=244, y=80)
        submit.place(x=244, y=120)

    def get_method(self):
        pass

    def logout(self):
        pass    



if __name__ == '__main__':    
    # root = tk.Tk()
    logger = logging.getLogger(__name__)
    logger.setLevel(level = logging.INFO)
    handler = logging.FileHandler("talentback_help_log.txt")
    handler.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    TalentHelper()
