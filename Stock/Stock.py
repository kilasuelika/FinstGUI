#coding:UTF-8
#Author: Zhou Yao
#E-Mail: semeego@live.com
#Date:2017/7/28

import numpy as np
import pandas as pd
import tkinter as tk
from tkinter import LabelFrame,Entry,Label,Button,Listbox,Frame,Scrollbar

font=("Courier", 12)
def descrip_sta(data):
    shp=data.shape
    obs=np.tile(shp[0],shp[1])
    mean=np.mean(data)
    var=np.var(data)
    hvar=np.power(max(0,data-np.tile(mean,(shp[1],1))),2)/shp[0]
    min=np.min(data)
    max=np.max(data)
    df=pd.DataFrame(np.array(obs,mean,var,hvar,min,max))
    df.set_index([])
    return()

def descrip_window(self):
    window=tk.Toplevel(self)


    #LabfelFrame for data file input.
    lbf1=LabelFrame(window,text='Input file',padx = 5, pady = 5)
    lbf1.grid(row=0,padx=5,pady=5)
    ipte=Entry(lbf1).pack(side='left',padx=5,pady=5)
    iptb=Button(lbf1,text='...').pack(side='left',padx=5,pady=5)
    ipt_cal=Button(lbf1,text='Calculation').pack(side='left',padx=5,pady=5)
    ipt_corr=Button(lbf1,text="Person Corr").pack(side='left',padx=5,pady=5)
    ipt_show=Button(lbf1,text="Show Data").pack(side='left',padx=5,pady=5)


    #LabelFrame for selecting variables.
    lbf2=LabelFrame(window,text='Select Variables',padx = 5, pady = 5 )
    lbf2.grid(row=1,sticky='nsew',padx=5,pady=5)
    lbf2.grid_columnconfigure(0, weight=3)
    lbf2.grid_columnconfigure(1, weight=1)
    lbf2.grid_columnconfigure(2, weight=3)

    listframe1=Frame(lbf2)
    listframe1.grid(row=0,column=0,sticky='nswe')

    #listframe1.place(rely=1.0, relx=1.0,anchor='w')
    scrollbar1=Scrollbar(listframe1)
    listbox1 = Listbox(listframe1,yscrollcommand=scrollbar1.set)
    listbox1.pack(side='left', fill='both',expand=True)
    scrollbar1.pack(side='right',fill='both')

    button_frame=Frame(lbf2)
    button_frame.grid(row=0,column=1)
    selectbtn1=Button(button_frame,text='>>').grid(row=0,padx=5,pady=5)
    selectbtn2=Button(button_frame,text='>>>').grid(row=1,padx=5,pady=5)
    selectbtn3=Button(button_frame,text='<<').grid(row=2,padx=5,pady=5)
    selectbtn4=Button(button_frame,text='<<<').grid(row=3,padx=5,pady=5)

    listframe2 = Frame(lbf2)
    listframe2.grid(row=0,column=2,sticky='nswe')
    scrollbar2=Scrollbar(listframe2)
    listbox2 = Listbox(listframe2, yscrollcommand=scrollbar2.set)
    listbox2.pack(side='left', fill='both',expand=True)
    scrollbar2.pack(side='right',fill='y')


    #LabelFrame for show calculation results.
    lbf3=LabelFrame(window,text='Calculation Results',padx=5,pady=5)
    lbf3.grid(row=2,sticky='nswe')
    btn1=Button(lbf3,text='Save to File')
    btn2=Button(lbf3,text='Save to Clipboard')
    btn1.pack(side='left',padx=5,pady=5)
    btn2.pack(side='left',padx=5,pady=5)
