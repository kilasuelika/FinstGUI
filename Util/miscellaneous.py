#coding:UTF-8
#Author: Zhou Yao
#E-Mail: semeego@live.com
#Date:2017/7/28

from tkinter import *
from pandastable import Table
def show_dataframe_in_win(window,dataframe):
    pt = Table(window,dataframe=dataframe)
    pt.show()
    return