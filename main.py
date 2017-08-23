#coding:UTF-8
#Author: Zhou Yao
#E-Mail: semeego@live.com
#Date:2017/7/26

import tkinter as tk
from tkinter import PanedWindow,messagebox,Button
from tkinter import LabelFrame
from Stock.Stock import descrip_window

#create main window.
def main():

    root = tk.Tk()
    root.title('Financial Instruments - Main')
    root.geometry('720x444')
    root.configure(background='white')

    st = LabelFrame(root, text='Stock', width=200, height=100,bg='white', padx=5, pady=5)
    st.grid_propagate(False)
    st.grid(row=0,padx=5,pady=5)
    st_desp=Button(st,text='Statistics',font=('Candara',14), padx=5, pady=5,command=lambda: descrip_window(root))
    st_desp.grid(column=0)
    derv = LabelFrame(root, text='Derivative', width=200, height=100,bg='white', padx=5, pady=5)
    derv.grid(row=1,padx=5,pady=5)
    root.mainloop()

if __name__=='__main__':
    main()