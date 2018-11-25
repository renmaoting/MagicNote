#!/usr/bin/python
# -*- coding: UTF-8 -*-

from Tkinter import *

import jsonlines as jsonlines

from src.constants import NOTES_FILE_PATH
from src.fileUtil import FileUtil

reload(sys)
sys.setdefaultencoding("utf-8")

class SearchPage(object):
    def __init__(self, master):
        self.lf1 = LabelFrame(master, width=380, height=550, text='Search')
        self.lf1.grid(row=0, column=0, padx=15)



        self.listb = Listbox(self.lf1)  # 创建两个列表组件
        data = FileUtil.getNoteRecords()
        for item in data:  # 第一个小部件插入数据
            self.listb.insert(0, item['title'])
        self.listb.place(x=0, y=0, width=370, height=530)

        self.lf2 = LabelFrame(master, width=380, height=550, text='Details')
        self.lf2.grid(row=0, column=1, rowspan=2)
        self.detail = Text(self.lf2)
        self.detail.place(x=0, y=0, width=370, height=530)



