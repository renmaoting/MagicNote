#!/usr/bin/python
# -*- coding: UTF-8 -*-

from Tkinter import *
from ttk import Combobox

from src.constants import WIN_WIDTH, WIN_HEIGHT
from src.fileUtil import FileUtil

reload(sys)
sys.setdefaultencoding("utf-8")


class SearchPage(object):
    def __init__(self, master):
        self.data = FileUtil.getNoteRecords()
        self.searchResult = []
        self.lf1 = LabelFrame(master, width=WIN_WIDTH/2-20, height=WIN_HEIGHT/3-10, text='Search')
        self.lf1.grid(row=0, column=0, padx=10, pady=10)

        self.titleLabel = Label(self.lf1, text='TiTle:').grid(row=0, column=0)
        self.titleEntry = Entry(self.lf1, width=30)
        self.titleEntry.grid(row=0, column=1)

        self.tagLabel = Label(self.lf1, text='Tags:').grid(row=1, column=0)
        # 下拉框，用于选择tags
        self.tag = StringVar()
        self.tagChosen = Combobox(self.lf1, width=20, textvariable=self.tag)
        self.tagChosen.bind("<<ComboboxSelected>>", self.selectTags)
        self.tags = self.getTags()
        self.tagChosen['values'] = tuple(self.tags)
        self.tagChosen.grid(row=1, column=1)
        self.tagEntry = Entry(self.lf1, width=50)
        self.tagEntry.grid(row=2, column=0, columnspan=3)

        self.dateLabel = Label(self.lf1, text='Date:').grid(row=3, column=0)
        self.dateStartEntry = Entry(self.lf1, width=10)
        self.dateStartEntry.grid(row=3, column=1)
        self.dateStartEntry.insert(END, '2018-08-06')
        self.dateEndEntry = Entry(self.lf1, width=10)
        self.dateEndEntry.grid(row=3, column=2)
        self.dateEndEntry.insert(END, '2018-12-15')

        self.searchBtn = Button(self.lf1, text='Search', command=self.searchNotes).grid(row=4, column=1)

        # labelFrame 用于盛放笔记列表
        self.lf2 = LabelFrame(master, width=WIN_WIDTH/2-20, height=WIN_HEIGHT - 210, text='Note List')
        self.lf2.grid(row=1, column=0, padx=10)

        self.listb = Listbox(self.lf2, bg='#E0FFFF')  # list 用于放note 列表
        self.listb.place(x=0, y=0, width=WIN_WIDTH/2-30, height=WIN_HEIGHT - 230)
        yscrollbar = Scrollbar(self.listb, command=self.listb.yview)
        yscrollbar.pack(side=RIGHT, fill=Y)
        self.listb.config(yscrollcommand=yscrollbar.set)
        self.listb.bind('<<ListboxSelect>>', self.selectNote)  # 绑定响应函数

        # 显示笔记详细信息
        self.lf3 = LabelFrame(master, width=WIN_WIDTH/2-20, height=WIN_HEIGHT-30, text='Note Details')
        self.lf3.grid(row=0, column=1, rowspan=2, padx=10, pady=10)
        self.detail = Text(self.lf3, bg='#E0FFFF')
        self.detail.place(x=0, y=0, width=WIN_WIDTH/2-30, height=WIN_HEIGHT-50)

    # 点击笔记列表显示详细信息
    def selectNote(self, event):
        w = event.widget
        index = int(w.curselection()[0])
        self.detail.delete('1.0', END)
        self.detail.insert(INSERT, '\t\t\t' + self.searchResult[index]['title'] + '\n')
        self.detail.insert(END, '\t\t' + ','.join(self.searchResult[index]['tags']) + '\n')
        editTime = self.searchResult[index]['time']
        timeStr = editTime[0:4] + '-' + editTime[4:6] + '-' + editTime[6:8] + ' ' + editTime[8:10] + ':' + editTime[10:12] + ':' + editTime[12:14]
        self.detail.insert(END, '\t\t' + timeStr + '\n\n')
        self.detail.insert(END, self.searchResult[index]['description'])

    # 得到所有的tags用于用户选择
    def getTags(self):
        tags = set(' ')
        for item in self.data:
            for tag in item['tags']:
                tags.add(tag)
        return tags

    # 根据title，tags，时间筛选记录
    def searchNotes(self):
        self.listb.delete(0, END)
        titleStr = self.titleEntry.get()
        startDate = self.dateStartEntry.get()
        endDate = self.dateEndEntry.get()
        tags = self.tagEntry.get()

        self.searchResult = []

        for item in self.data:
            # 如果包含title数据，但是当前记录title和搜索条件不一致，则跳过此条记录
            if len(titleStr.strip()) != 0 and item['title'] != titleStr:
                continue

            # 如果包含时间条件并且时间不符合，则跳过次记录
            if len(startDate.strip()) !=0  and len(endDate.strip()) != 0:
                noteTime = int(item['time'][0:8])
                startTime = int(startDate.replace('-', ''))
                endTime = int(endDate.replace('-', ''))
                if not (startTime <= noteTime <= endTime):
                    continue

            # 根据tags筛选记录，如果有多个tags，则必须同时满足
            if len(tags.strip()) != 0:
                flag = 1
                for tag in tags.strip().split(' '):
                    if tag not in item['tags']:
                        flag = 0
                        break
                if flag == 0:
                    continue
            self.searchResult.append(item)
        for item in self.searchResult:  # 最近的数据在最前面
            self.listb.insert(END, item['title'])

    # 选择tags
    def selectTags(self, *args):
        self.tagEntry.insert(END, self.tagChosen.get() + ' ')
