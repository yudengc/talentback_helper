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
        self.now_frame = None
        self.window.geometry('{}x{}'.format(self.width, self.heigth))
        # self.window.resizable(width=False, height=False)
        self.window.minsize(400, 200)
        self.window.maxsize(800, 400)
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
        return req_data
        # return ['达人关系修复{}'.format(i) for i in range(20)]

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
        eval(FUNC_TEMPLATE.format())
        rep_content = tk.Text(window, width=50, height=20)
        this_method(this_url, headers=headers)

    def main_face(self):
        main_frame = tk.Frame(self.window)
        main_frame.pack(expand='yes', fill="both")
        button_list = self.get_method()

        def select_method(*args):
            this_index = listbox.curselection()[0]
            if self.now_select == this_index:
                return
            else:
                self.now_select = this_index
            print(button_list[this_index])
            print(listbox.curselection()[0])

        left_frame = tk.LabelFrame(main_frame, text='选择功能')
        left_frame.pack(side='left', fill='both', padx=3)
        wellcome_frame = tk.LabelFrame(main_frame, text='操作')
        wellcome_frame.pack(side='left', expand='yes', fill='both')
        tk.Label(wellcome_frame, text='没事多请技术部喝奶茶\n不然出事了我们才不会理你呢', font=('Arial', 14)).place(x=13, y=60)
        self.now_frame = wellcome_frame

        listbox = tk.Listbox(
            left_frame, width=12, font=('Arial', 10), 
            listvariable=tk.StringVar(value=[i['title'] for i in button_list]), 
            selectmode="browse"
        )
        listbox.pack(side='left', fill='both')
        listbox.bind("<<ListboxSelect>>", select_method)
        listbox.pack(side='left', fill='y')

        y_scr = tk.Scrollbar(left_frame)
        listbox.config(yscrollcommand=y_scr.set)
        y_scr.config(command=listbox.yview)
        y_scr.pack(side='right', fill='y')




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