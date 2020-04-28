# -*- coding:utf-8 -*-

import logging
import json
import requests
import sys
import tkinter as tk



class Talentback:
    def __init__(self):
        self.window = tk.Tk()
        self.token = None
        self.window.geometry('600x400')
        self.window.resizable(width=False, height=False)
        self.base_url = "http://api.etest.darentui.com/"
        self.login_face()
        self.window.title = "达人推后台助手"
        self.window.mainloop()       


    def login_face(self):
        face = tk.Frame(self.window)
        face.pack()
        # 第一行
        l_username = tk.Label(face,text='用户名：')
        l_username.grid(row=0)
        username = tk.Entry(face)
        username.grid(row=0,column=1)
        # 2
        l_password = tk.Label(face,text='密码：')
        l_password.grid(row=1)
        password = tk.Entry(face, show='*')
        password.grid(row=1, column=1)
        # 3
        l_msg = tk.Label(face, text='')
        l_msg.grid(row=4)

        def go_login():
            phone_str = username.get()
            password_str = password.get()
            if not phone_str or not password_str:
                l_msg['text'] = '请输入账户密码'
                return 
                
            data = {
                "phone": username.get(),
                "password": password.get()
            }
            headers = {
                "Content-Type": "application/json"
            }
            req_obj = requests.post(self.base_url+"api/v1/accounts/login/", json=data, headers=headers)
            req_data = json.loads(req_obj.content)
            rc = req_obj.status_code            
            print(str(rc), type(rc))
            if rc == 404 or rc == 400:
                l_msg['text'] = req_data.get("detail")
                return
            else:
                self.token = req_data.get('token')
                face.forget()
                self.main_face()
                logger.info(req_data)

        login_button = tk.Button(face, text='登录',  width=10, command=go_login)
        exit_button = tk.Button(face, text='退出',  width=10, command=self.window.destroy)
        login_button.grid()
        exit_button.grid()
        # {
        # "phone": "15717974490",
        # "password": "123"
        # } 
        # 4
        
    def main_face(self):
        face = tk.Frame(self.window)
        face.pack()
        button_list = self.get_method()
        for this_bt in button_list:
            this_button = tk.Button(face, text=this_bt,  width=10)
            this_button.grid()        
            
        

    def get_method(self):
        # headers = {
        #     "Content-Type": "application/json",
        #     # "Authorier": self.token
        # }
        # req_obj = requests.get(self.base_url+"api/v1/oss/helper_method/", headers=headers)
        # req_data = json.loads(req_obj.content)
        # return [req_data]
        # {'title': '注销', 'api/v1/asfasdf/', 
        # 'canshu':{
        #     "username": 'text',
        #     "ss"
        # }
        # }
        # post api/v1/asfasdf/  {
        #     "username": username.get()
        #     "ss": ss.get()
        # }
        return ['测试1', '测试2', '测试3','1','2','3','4','5','6','7','8','9','11','22','21','22','33','411']


if __name__ == "__main__":
    logger = logging.getLogger(__name__)
    logger.setLevel(level = logging.INFO)
    handler = logging.FileHandler("达人推助手日志.txt")
    handler.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    Talentback()