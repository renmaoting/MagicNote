#!/usr/bin/python
# -*- coding: UTF-8 -*-

from Tkinter import *

from src.constants import WIN_WIDTH, WIN_HEIGHT
from src.fileUtil import FileUtil

reload(sys)
sys.setdefaultencoding("utf-8")

class SearchPage(object):
    def __init__(self, master):
        self.lf1 = LabelFrame(master, width=WIN_WIDTH/2-20, height=WIN_HEIGHT/3-10, text='Search')
        self.lf1.grid(row=0, column=0, padx=10)



        self.lf2 = LabelFrame(master, width=WIN_WIDTH/2-20, height=WIN_HEIGHT*2/3, text='Note List')
        self.lf2.grid(row=1, column=0, padx=10)

        self.listb = Listbox(self.lf2)  # list 用于放note 列表
        data = FileUtil.getNoteRecords()
        for item in data:  # 第一个小部件插入数据
            self.listb.insert(0, item['title'])
        self.listb.place(x=0, y=0, width=WIN_WIDTH/2-30, height=WIN_HEIGHT*2/3-20)



        self.lf3 = LabelFrame(master, width=WIN_WIDTH/2-20, height=WIN_HEIGHT-40, text='Note Details')
        self.lf3.grid(row=0, column=1, rowspan=2, padx=10)
        self.detail = Text(self.lf3)
        self.detail.place(x=0, y=0, width=WIN_WIDTH/2-30, height=WIN_HEIGHT-50)



