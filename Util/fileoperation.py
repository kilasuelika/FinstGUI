#coding:UTF-8
#Author: Zhou Yao
#E-Mail: semeego@live.com
#Date:2017/7/28

import os
from tkinter.filedialog import askopenfilename

def load_file():
    fname = askopenfilename(filetypes=(("CSV files", "*.csv"),
                                       ("Excel files", "*.xls;*.xlsx")))
    ext= os.path.splitext(fname)[1]
    if ext=='.csv':
        data=
    elif ext=='.xls' or ext=='xlsx':
        data=
    return data

def save_file(data,)