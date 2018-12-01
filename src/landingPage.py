#!/usr/bin/python
# -*- coding: UTF-8 -*-
import datetime
from importlib import reload
from tkinter import *

from src.constants import WIN_WIDTH, WIN_HEIGHT
from src.createPage import CreatePage
from src.fileUtil import FileUtil
from src.searchPage import SearchPage

reload(sys)


class LandingPage(object):
    def __init__(self, master, data):
        self.initial(master, data)

    def initial(self, master, data):
        self.data = data
        self.selectedItemIndex = -1
        self.frm = Frame(master, width=WIN_HEIGHT, height=WIN_HEIGHT)
        self.frm.place(x=0, y=0)
        self.lf1 = LabelFrame(self.frm, width=WIN_WIDTH / 2 - 20, height=WIN_HEIGHT / 3 - 10, text='Options')
        self.lf1.grid(row=0, column=0, padx=10, pady=10)

        self.createBtn = Button(self.lf1, text='Create Notes', command=lambda: self.createPage(master)).grid(row=0,
                                                                                                             column=0)
        self.searchBtn = Button(self.lf1, text='Search Notes', command=lambda: self.searchPage(master)).grid(row=0,
                                                                                                             column=1)

        # labelFrame 用于盛放笔记列表
        self.lf2 = LabelFrame(self.frm, width=WIN_WIDTH / 2 - 20, height=WIN_HEIGHT - 100, text='Note List')
        self.lf2.grid(row=1, column=0, padx=10)

        self.listb = Listbox(self.lf2, bg='#E0FFFF')  # list 用于放note 列表
        self.listb.place(x=0, y=0, width=WIN_WIDTH / 2 - 30, height=WIN_HEIGHT - 155)

        self.deleteBtn = Button(self.lf2, text='Delete Note', command=self.deleteNote)
        self.deleteBtn.place(x=160, y=452)
        self.countLabel = Label(self.lf2, bg='#E0FFFF')
        self.updateCountLabel()
        self.countLabel.place(x=65, y=452)
        self.updateNoteList(self.data)

        yscrollbar = Scrollbar(self.listb, command=self.listb.yview)
        yscrollbar.pack(side=RIGHT, fill=Y)
        self.listb.config(yscrollcommand=yscrollbar.set)
        self.listb.bind('<<ListboxSelect>>', self.selectNote)  # 绑定响应函数

        # 显示笔记详细信息
        self.lf3 = LabelFrame(self.frm, width=WIN_WIDTH / 2 - 20, height=WIN_HEIGHT - 30, text='Note Details')
        self.lf3.grid(row=0, column=1, rowspan=2, padx=10, pady=10)
        self.detail = Text(self.lf3, bg='#E0FFFF')
        self.detail.place(x=0, y=0, width=WIN_WIDTH / 2 - 30, height=WIN_HEIGHT - 78)
        self.saveBtn = Button(self.lf3, text='Save', command=self.saveNote).place(x=170, y=522)

    # 点击笔记列表显示详细信息
    def selectNote(self, event):
        w = event.widget
        self.selectedItemIndex = int(w.curselection()[0])
        self.detail.delete('1.0', END)
        self.detail.insert(INSERT, '\t\t\t' + self.data[self.selectedItemIndex]['title'] + '\n')
        self.detail.insert(END, '\t\t' + ','.join(self.data[self.selectedItemIndex]['tags']) + '\n')
        editTime = self.data[self.selectedItemIndex]['time']
        timeStr = editTime[0:4] + '-' + editTime[4:6] + '-' + editTime[6:8] + ' ' + editTime[8:10] + ':' + editTime[10:12] + ':' + editTime[12:14]
        self.detail.insert(END, '\t\t' + timeStr + '\n\n')
        self.detail.insert(END, self.data[self.selectedItemIndex]['description'])

    def searchPage(self, master):
        SearchPage(master, self.data)

    def createPage(self, master):
        CreatePage(master, self.updateNoteList, self.initial, self.data)
        self.frm.destroy()

    def updateNoteList(self, data):
        self.listb.delete(0, END)
        for item in data:
            self.listb.insert(END, item['title'])
        self.updateCountLabel()

    def updateCountLabel(self):
        self.countLabel['text'] = 'Total: ' + str(len(self.data))

    def deleteNote(self):
        if 0 > self.selectedItemIndex >= len(self.data):
            return

        self.data = self.data[:self.selectedItemIndex] + self.data[self.selectedItemIndex+1:]
        if len(self.data) > 0:
            FileUtil.setNoteRecords(self.data)
        else:
            FileUtil.clearNote()  # 清空文件
        self.updateNoteList(self.data)
        self.selectedItemIndex = -1

    def saveNote(self):
        detailVal = self.detail.get(0.0, END).split('\n')
        if len(detailVal) < 5:  # 至少包含5行才是合法数据
            print("invalid data!")
            return
        curTime = datetime.datetime.now().strftime('%Y%m%d%H%M%S')

        titleVal = detailVal[0].strip()
        tagsVal = detailVal[1].strip().split(',')
        descriptionVal = ''.join(detailVal[4:])

        if len(titleVal) == 0 or len(tagsVal) == 0 or len(descriptionVal.strip()) == 0:
            print("invalid data!")
            return

        note = {'title': titleVal, 'tags': tagsVal, 'description': descriptionVal, 'time': curTime}
        self.data[self.selectedItemIndex] = note
        FileUtil.setNoteRecords(self.data)
        self.updateNoteList(self.data)
