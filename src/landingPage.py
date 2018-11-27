#!/usr/bin/python
# -*- coding: UTF-8 -*-

from Tkinter import *

from src.constants import WIN_WIDTH, WIN_HEIGHT
from src.createPage import CreatePage
from src.fileUtil import FileUtil
from src.searchPage import SearchPage

reload(sys)
sys.setdefaultencoding("utf-8")


class LandingPage(object):
    def __init__(self, master):
        self.data = FileUtil.getNoteRecords()
        self.frm = Frame(master, width=WIN_HEIGHT, height=WIN_HEIGHT).place(x=0, y=0)
        self.lf1 = LabelFrame(self.frm , width=WIN_WIDTH/2-20, height=WIN_HEIGHT/3-10, text='Options')
        self.lf1.grid(row=0, column=0, padx=10, pady=10)

        self.createBtn = Button(self.lf1, text='Create Notes', command=lambda: self.createPage(master)).grid(row=0, column=0)
        self.searchBtn = Button(self.lf1, text='Search Notes', command=lambda: self.searchPage(master)).grid(row=0, column=1)

        # labelFrame 用于盛放笔记列表
        self.lf2 = LabelFrame(self.frm, width=WIN_WIDTH/2-20, height=WIN_HEIGHT - 210, text='Note List')
        self.lf2.grid(row=1, column=0, padx=10)

        self.listb = Listbox(self.lf2, bg='#E0FFFF')  # list 用于放note 列表
        self.listb.place(x=0, y=0, width=WIN_WIDTH/2-30, height=WIN_HEIGHT - 230)
        for item in self.data:
            self.listb.insert(END, item['title'])
        yscrollbar = Scrollbar(self.listb, command=self.listb.yview)
        yscrollbar.pack(side=RIGHT, fill=Y)
        self.listb.config(yscrollcommand=yscrollbar.set)
        self.listb.bind('<<ListboxSelect>>', self.selectNote)  # 绑定响应函数

        # 显示笔记详细信息
        self.lf3 = LabelFrame(self.frm, width=WIN_WIDTH/2-20, height=WIN_HEIGHT-30, text='Note Details')
        self.lf3.grid(row=0, column=1, rowspan=2, padx=10, pady=10)
        self.detail = Text(self.lf3, bg='#E0FFFF')
        self.detail.place(x=0, y=0, width=WIN_WIDTH/2-30, height=WIN_HEIGHT-50)

    # 点击笔记列表显示详细信息
    def selectNote(self, event):
        w = event.widget
        index = int(w.curselection()[0])
        self.detail.delete('1.0', END)
        self.detail.insert(INSERT, '\t\t\t' + self.data[index]['title'] + '\n')
        self.detail.insert(END, '\t\t' + ','.join(self.data[index]['tags']) + '\n')
        editTime = self.data[index]['time']
        timeStr = editTime[0:4] + '-' + editTime[4:6] + '-' + editTime[6:8] + ' ' + editTime[8:10] + ':' + editTime[10:12] + ':' + editTime[12:14]
        self.detail.insert(END, '\t\t' + timeStr + '\n\n')
        self.detail.insert(END, self.data[index]['description'])

    def searchPage(self, master):
        SearchPage(master)

    def createPage(self, master):
        CreatePage(master)
