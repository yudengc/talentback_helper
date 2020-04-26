# -*- coding:utf-8 -*-

import logging
import json
import requests
import sys
import tkinter as tk



class Talentback:
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry('600x400')
        self.window.resizable(width=False, height=False)
        self.base_url = "http://api.etest.darentui.com/"
        self.login_face()
        self.get_method()
        self.main_face()
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
            face.place_forget()
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

    def get_method(self):
        pass



if __name__ == "__main__":
    logger = logging.getLogger(__name__)
    logger.setLevel(level = logging.INFO)
    handler = logging.FileHandler("达人推助手日志.txt")
    handler.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    Talentback()