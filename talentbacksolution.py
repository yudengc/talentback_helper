
from tkinter import *
 
# 初始化Tk()
myWindow = Tk()
# 设置标题
myWindow.title('Python GUI Learning')
myWindow.geometry("%dx%d+%d+%d"%(400, 200, 200, 200))
# 创建Checkbutton
checkVar = IntVar()
check = Checkbutton(myWindow, text="Checkbutton test", variable=checkVar)
check.grid(row=0, column=0, sticky=W, padx=2 ,pady=5)
# 定义按钮点击事件
def button_Click(event=None):
    print(checkVar.get(), type(checkVar.get()))
 
# 创建两个按钮
b1 =Button(myWindow, text='click me' , relief='raised', width=8, height=1, command=button_Click)
b1.grid(row=0, column=2, sticky=W, padx=2 ,pady=10)
 
# 进入消息循环


myWindow.mainloop()

