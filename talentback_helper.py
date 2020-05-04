# -*- coding:utf-8 -*-
# yudengc

import base64
import logging
import json
import requests
import sys
import tkinter as tk


__VERSION__ = "1.0"

class Talentback:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("达人推客服助手")
        self.token = None
        self.width = 400
        self.heigth = 200
        self.now_frame = None
        self.now_select = None
        self.main_frame = None
        self.window.geometry('{}x{}'.format(self.width, self.heigth))
        # self.window.resizable(width=False, height=False)
        self.window.minsize(400, 200)
        self.window.maxsize(400, 800)
        self.base_url = "http://api.etest.darentui.com/"
        # self.base_url = "http://119.23.109.99:8083/"
        self.update()
        self.menu()
        self.login_face()
        # self.main_face()
        self.window.mainloop()

    def update(self):
        pass

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

    def get_wellcome(self):
        headers = {
            "Content-Type": "application/json",
            "Authorization": self.token
        }
        req_obj = requests.get(self.base_url+"api/v1/helper/get-wellcome/", headers=headers)
        return json.loads(req_obj.content)

    def create_method(self, method_list):
        func_template = '''def {func_name}(self):
            this_frame = tk.LabelFrame(self.main_frame, text='注销')
            this_frame.pack(side='left', expand='yes', fill='both')
            self.now_frame = this_frame                           
            args = {args}
            data = dict()
            row = 0
            column = 0
            all_arg_widget = dict()
            class follow_list(list):
                def get(self):
                    result = []
                    for i in self.__iter__():
                        result.append(i.get())
                    return result
            for arg in args:
                try:
                    arg_name = arg['arg_name']
                    tk_type_name = arg['type']
                    tips = arg["tips"]
                    if tk_type_name == '输入':
                        tk.Label(this_frame, text=tips).grid(row=row, column=column, pady=2, padx=2)
                        v = tk.StringVar()
                        arg_widget = tk.Entry(this_frame, textvariable=v)
                        arg_widget.grid(row=row, column=column+1, pady=2, padx=2)                    
                    elif tk_type_name == '单选':
                        o = tk.LabelFrame(this_frame, text=tips)
                        o.grid(row=row, column=column, pady=2, padx=2, columnspan=2, sticky=tk.EW)
                        arg_widget = tk.IntVar()
                        choice = arg['choice']
                        length = len(choice)
                        for i in range(length):
                            tk.Radiobutton(o, text=choice[i], variable=arg_widget, value=i).grid(column=0, row=i, sticky=tk.W)
                    elif tk_type_name == '多选':
                        o = tk.LabelFrame(this_frame, text=tips)
                        o.grid(row=row, column=column, pady=2, padx=2, columnspan=2, sticky=tk.EW)
                        choice = arg['choice']
                        length = len(choice)                        
                        arg_widget = follow_list()
                        for i in range(length):
                            this_name = "var_%d" %i
                            locals()[this_name] = tk.IntVar()
                            this_var = locals()[this_name]
                            arg_widget.append(this_var)
                            tk.Checkbutton(o, text=choice[i], variable=this_var).grid(column=0, row=i, sticky=tk.W)                        
                    else:
                        continue
                except Exception as e:
                    print('err:')
                    print(str(e))
                    logger.info(str(e))
                    continue
                all_arg_widget[arg_name] = arg_widget
                row += 1
            rep_data = tk.StringVar()
            var_usr_name = tk.StringVar()
            self.rep_label = tk.Label(this_frame, textvariable=rep_data, wraplength=220, fg='green')
            self.rep_label.grid(row=row, pady=5, rowspan=999, columnspan=999, sticky=tk.NSEW)
            def send_request():
                headers = dict()
                headers["Content-Type"] = "application/json"
                headers["Authorization"] = self.token           
                data = dict()
                for arg_name, arg_widget in all_arg_widget.items():
                    data[arg_name] = arg_widget.get()
                print(data)
                get_method = '{method}'
                get_url = '{url}'
                this_method = getattr(requests, get_method)
                rep = None
                if get_method == 'post':
                    rep = this_method(self.base_url+get_url, data=json.dumps(data), headers=headers)
                elif get_method == 'get':
                    rep = this_method(self.base_url+get_url, params=data, headers=headers)
                response_data = "请求失败, 找一下技术哥哥看看吧"      
                if not rep:
                    self.rep_label.config(fg='red')
                elif int(str(rep.status_code)[0]) > 4:
                    self.rep_label.config(fg='red')
                if rep is not None:                    
                    response_data = json.loads(rep.content).get("detail", response_data)
                rep_data.set(response_data)

            exec_button = tk.Button(this_frame, text='执行', command=send_request)
            exec_button.grid(row=0, column=3, pady=2, padx=5)'''

        i = 0
        for method in method_list:
            func_name = 'go_{}'.format(i)
            url = method['url']
            req_method = method['method'].lower()
            args = method['args']
            func_str = func_template.format(func_name=func_name, url=url, method=req_method, args=args)
            exec(func_str)
            func = locals()[func_name]
            setattr(self, func_name, func)
            i += 1
 

    def main_face(self):
        self.window.geometry('400x380')
        self.main_frame = tk.Frame(self.window)
        self.main_frame.pack(expand='yes', fill="both")
        method_list = self.get_method()
        wellcome_str = self.get_wellcome()
        self.create_method(method_list)

        def select_method(*args):
            if not listbox.curselection():
                return
            this_index = listbox.curselection()[0]
            if self.now_select == this_index:
                return
            self.now_select = this_index
            self.now_frame.destroy()
            this_func_name = 'go_{}'.format(this_index)
            this_func = getattr(self, this_func_name)
            this_func(self)
        

        left_frame = tk.LabelFrame(self.main_frame, text='选择功能')
        left_frame.pack(side='left', fill='both', padx=3)
        wellcome_frame = tk.LabelFrame(self.main_frame, text='操作')
        wellcome_frame.pack(side='left', expand='yes', fill='both')
        tk.Label(wellcome_frame, text=wellcome_str, font=('Arial', 11), wraplength=260, anchor='center').place(x=13, y=13)
        self.now_frame = wellcome_frame

        listbox = tk.Listbox(
            left_frame, width=12, font=('Arial', 10), 
            listvariable=tk.StringVar(value=[i['title'] for i in method_list]), 
            selectmode="browse"
        )
        listbox.pack(side='left', fill='both')
        listbox.bind("<<ListboxSelect>>", select_method)
        listbox.pack(side='left', fill='y')

        y_scr = tk.Scrollbar(left_frame)
        listbox.config(yscrollcommand=y_scr.set)
        y_scr.config(command=listbox.yview)
        y_scr.pack(side='right', fill='y')


if __name__ == "__main__":
    logger = logging.getLogger(__name__)
    logger.setLevel(level = logging.INFO)
    handler = logging.FileHandler("达人推助手日志.txt")
    handler.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    Talentback()