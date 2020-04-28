# -*- coding:utf-8 -*-

import logging
import json
import requests
import sys
import tkinter as tk


FUNC_TEMPLATE = '''
def go_{button}():

'''

class Talentback:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("达人推客服助手")
        self.token = None
        self.width = 400
        self.heigth = 200
        self.window.geometry('{}x{}'.format(self.width, self.heigth))
        # self.window.resizable(width=False, height=False)
        self.window.minsize(400, 200)
        self.window.maxsize(400, 600)
        self.base_url = "http://api.etest.darentui.com/"        
        self.menu()
        # self.login_face()
        self.main_face()
        self.window.mainloop()

    def menu(self):
        menubar = tk.Menu(self.window)
        filemenu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label='点我', menu=filemenu)
        menubar.add_cascade(label='点我', menu=filemenu)
        menubar.add_cascade(label='点我', menu=filemenu)
        menubar.add_cascade(label='点我', menu=filemenu)        
        def do_job():
            pass
        filemenu.add_command(label='★', command=do_job)
        filemenu.add_command(label='邓', command=do_job)
        filemenu.add_command(label='钰', command=do_job)
        filemenu.add_command(label='可', command=do_job)
        filemenu.add_command(label='太', command=do_job)
        filemenu.add_command(label='帅', command=do_job)
        filemenu.add_command(label='了', command=do_job)
        filemenu.add_command(label='★', command=do_job)
        # filemenu.add_separator()  
        # filemenu.add_command(label='退出', command=self.window.quit)
        self.window.config(menu=menubar)


    def login_face(self):
        face = tk.Frame(self.window)
        face.pack(expand='yes', fill="both")

        tips = tk.StringVar()
        tk.Label(face, text='账户:', font=('Arial', 14)).place(x=13, y=20)
        tk.Label(face, text='密码:', font=('Arial', 14)).place(x=13, y=70)
        tk.Label(face, textvariable=tips, fg='red').place(x=100, y=150)

        var_usr_name = tk.StringVar()
        entry_usr_name = tk.Entry(face, textvariable=var_usr_name, font=('Arial', 14))
        entry_usr_name.place(x=120, y=20)
        
        var_usr_pwd = tk.StringVar()
        entry_usr_pwd = tk.Entry(face, textvariable=var_usr_pwd, font=('Arial', 14), show='*')
        entry_usr_pwd.place(x=120, y=70)

        def go_login():
            phone_str = entry_usr_name.get()
            password_str = entry_usr_pwd.get()
            if not phone_str or not password_str:
                tips.set('请输入账户密码')
                return 
                
            data = {
                "phone": entry_usr_name.get(),
                "password": entry_usr_pwd.get()
            }
            headers = {
                "Content-Type": "application/json"
            }
            req_obj = requests.post(self.base_url+"api/v1/accounts/login/", json=data, headers=headers)
            req_data = json.loads(req_obj.content)
            rc = req_obj.status_code            
            if str(rc).startswith('4'):
                tips.set(req_data.get("detail"))
                return
            else:
                self.token = req_data.get('token')
                face.destroy()
                self.main_face()
                logger.info(req_data)

        login_button = tk.Button(face, text='登录',  width=10, command=go_login)
        exit_button = tk.Button(face, text='退出',  width=10, command=self.window.destroy)
        login_button.place(x=100, y=110)
        exit_button.place(x=180, y=110)
        # {
        # "phone": "15717974490",
        # "password": "123"
        # }

    def get_method(self):
        headers = {
            "Content-Type": "application/json",
            "Authorization": self.token
        }
        req_obj = requests.get(self.base_url+"api/v1/helper/get-method/", headers=headers)
        req_data = json.loads(req_obj.content)
        # return req_data
        return range(20)

    def create_method(self, this_bt):
        return print(1)
        headers = {
            "Content-Type": "application/json",
            "Authorization": self.token
        }
        method = this_bt['method'].lower()
        this_method = getattr(requests, method)
        this_url = this_bt['url']
        # lista = ["funca","funcb","funcc"]
        
        # for fn in lista:
        #     exec(FUNC_TEMPLATE.format(func=fn))
        # local_vars = dict(locals().items())
        # funcs = [local_vars[f] for f in lista]
        eval(FUNC_TEMPLATE.format())
        rep_content = tk.Text(window, width=50, height=20)
        this_method(this_url, headers=headers)

    def main_face(self):        
        method_frame = tk.LabelFrame(self.window, width=12, background='red')
        method_frame.pack(side='left', fill='both')
        button_list = self.get_method()
        row = 0
        for this_bt in button_list:
            title = str(this_bt)
            # title = this_bt['title']
            # bt_method = self.create_method(this_bt)
            # if not bt_method:
            #     continue
            this_button = tk.Button(method_frame, text=title[:5],  width=10, height=2)
            this_button.grid(row=row, column=0)            
            row += 1
        
        effect_frame = tk.LabelFrame(self.window, text="哦哦", background='yellow')
        effect_frame.pack(side='right', padx=10, fill='both', expand='yes')


FUNC_TEMPLATE = '''
def go_{button}():
    face = tk.Frame(self.window)
    face.pack()
'''

if __name__ == "__main__":
    logger = logging.getLogger(__name__)
    logger.setLevel(level = logging.INFO)
    handler = logging.FileHandler("达人推助手日志.txt")
    handler.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    Talentback()