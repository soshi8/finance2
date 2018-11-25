# -*- coding: utf-8 -*-
import tkinter 
from sklearn.linear_model import LinearRegression
import pandas as pd
import tkinter.messagebox as msg 
from sklearn import utils
import numpy as np

stock_data = pd.read_csv('stockchart_20180908.csv')
count_s =  len(stock_data)
owarine = stock_data['終値'].values.tolist()
successive_data = []
answers = []
for i in range(4, count_s):
    successive_data.append([owarine[i-4], owarine[i-3], owarine[i-2], owarine[i-1]])
    answers.append(owarine[i] )
    
reg = LinearRegression().fit(successive_data, answers)


root = tkinter.Tk()
root.title(u'My First App')
root.geometry("600x450")

def calcNikkei(event):
    ret = True
    
    if ret:
        try:
            val1 = float(Entry1.get())
        except ValueError:
            msg.showerror(title = '４日前のエラー', message = u'４日前の値が数字ではありません')
            ret = False
    
    if ret:
        try:
            val2 = float(Entry2.get())
        except ValueError:
                msg.showerror(title = '３日前のエラー', message = u'３日前の値が数字ではありません')
                ret = False

    if ret:
        try:
            val3 = float(Entry3.get())
        except ValueError:
            msg.showerror(title = '２日前のエラー', message = u'２日前の値が数字ではありません')
            ret = False

    if ret:
        try:
            val4 = float(Entry4.get())
        except ValueError:
            msg.showerror(title = '１日前のエラー', message = u'１日前の値が数字ではありません')
            ret = False

    if ret:
        
        test_data = np.array([[val1,val2,val3,val4]])
#        print("test_data = " + test_data)

        predicted = reg.predict(test_data)
#        print("predict = " + predicted)
        label6["text"] = str(predicted.tolist()[0]) + "円"        
    else:    
        label6["text"] = "xxxxx円"

# 初期化ボタン
def clsAns(event):
    label6["text"] = "xxxxx円"

# 終了
def endCalc(event):
    root.destroy()


label1 = tkinter.Label(text=u'４営業日前:',font=8)
label1.place(x=50,y=50)

label2 = tkinter.Label(text=u'３営業日前:',font=8)
label2.place(x=50,y=100)

label3 = tkinter.Label(text=u'２営業日前:',font=8)
label3.place(x=50,y=150)

label4 = tkinter.Label(text=u'１営業日前:',font=8)
label4.place(x=50,y=200)

label5 = tkinter.Label(text=u'予想結果:',font=8)
label5.place(x=50,y=400)

label6 = tkinter.Label(text=u'xxxxx円',font=8)
label6.place(x=200,y=400)

Entry1 = tkinter.Entry(font=8)
Entry1.place(x=200,y=50)

Entry2 = tkinter.Entry(font=8)
Entry2.place(x=200,y=100)

Entry3 = tkinter.Entry(font=8)
Entry3.place(x=200,y=150)

Entry4 = tkinter.Entry(font=8)
Entry4.place(x=200,y=200)


Button1 = tkinter.Button(text=u'予測します。', font=8)
Button1.bind("<Button-1>", calcNikkei)        # ボタンが押されたときに実行される関数をバインドします
Button1.place(x=100,y=300)
root.bind('<Return>', calcNikkei) 

Button2 = tkinter.Button(text=u'クリア', font=8)
Button2.bind("<Button-1>", clsAns)        # ボタンが押されたときに実行される関数をバインドします
Button2.place(x=250,y=300)

Button3 = tkinter.Button(text=u'終了', font=8)
Button3.bind("<Button-1>", endCalc)        # ボタンが押されたときに実行される関数をバインドします
Button3.place(x=350,y=300)

#entry1 = ttk.Entry(frame1, textvariable=t) 
#button1 = ttk.Button(frame1, text='OK', command=foo)
#
#frame1.grid(row=0,column=0,sticky=(N,E,S,W))
#label1.grid(row=1,column=1,sticky=E)
#entry1.grid(row=1,column=2,sticky=W)
#button1.grid(row=2,column=2,sticky=W)
#
#for child in frame1.winfo_children():
#    child.grid_configure(padx=5, pady=5)

root.mainloop()
