#!/usr/bin/python
# -*- coding: UTF-8 -*-

from Tkinter import *

import jsonlines as jsonlines

from src.constants import NOTES_FILE_PATH

reload(sys)
sys.setdefaultencoding("utf-8")


class BrowsePage(object):
    def __init__(self, master):
        self.lf1 = LabelFrame(master, width=380, height=550, text='Latest 20 Notes')
        self.lf1.grid(row=0, column=0, padx=15)

        self.li = ['C', 'python', 'php', 'html', 'SQL', 'java']
        self.listb = Listbox(self.lf1)  # 创建两个列表组件
        for item in self.li:  # 第一个小部件插入数据
            self.listb.insert(0, item)
        self.listb.place(x=0, y=0, width=370, height=530)

        self.lf2 = LabelFrame(master, width=380, height=550, text='Details')
        self.lf2.grid(row=0, column=1, rowspan=2)
        self.detail = Text(self.lf2)
        self.detail.place(x=0, y=0, width=370, height=530)


    def loadNoteFile(self):
        with open(NOTES_FILE_PATH, "r+") as f:
            for item in jsonlines.Reader(f):
                print(item)
