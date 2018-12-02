#!python3
# -*- coding: UTF-8 -*-
from importlib import reload
from tkinter import *
from tkinter.ttk import Combobox

from src.constants import WIN_WIDTH, WIN_HEIGHT

reload(sys)


class SearchPage(object):
    def __init__(self, master, data):
        self.searchResult = []
        self.frm = Frame(master, width=WIN_HEIGHT, height=WIN_HEIGHT)
        self.frm.place(x=0, y=0)
        self.lf1 = LabelFrame(self.frm, width=WIN_WIDTH/3, height=WIN_HEIGHT/3, text='Search')
        self.lf1.grid(row=0, column=0, padx=10, pady=5)

        self.titleLabel = Label(self.lf1, text='TiTle:').grid(row=0, column=0)
        self.titleEntry = Entry(self.lf1, width=33)
        self.titleEntry.grid(row=0, column=1, columnspan=5)

        self.tagLabel = Label(self.lf1, text='Tags:').grid(row=1, column=0)
        # 下拉框，用于选择tags
        self.tag = StringVar()
        self.tagChosen = Combobox(self.lf1, textvariable=self.tag)
        self.tagChosen.bind("<<ComboboxSelected>>", self.selectTags)
        self.tags = self.getTags(data)
        self.tagChosen['values'] = tuple(self.tags)
        self.tagChosen.grid(row=1, column=1)
        self.tagEntry = Entry(self.lf1, width=38)
        self.tagEntry.grid(row=2, column=0, columnspan=6)

        self.dateLabel = Label(self.lf1, text='Date:').grid(row=3, column=0)
        self.dateStartEntry = Entry(self.lf1, width=10)
        self.dateStartEntry.grid(row=3, column=1)
        self.dateStartEntry.insert(END, '2018-08-06')
        self.dateEndEntry = Entry(self.lf1, width=10)
        self.dateEndEntry.grid(row=3, column=2)
        self.dateEndEntry.insert(END, '2018-12-15')

        self.searchBtn = Button(self.lf1, text='Search', command=lambda: self.searchNotes(data)).grid(row=4, column=1)
        self.homeBtn = Button(self.lf1, text='Home Page', command=self.landingPage).grid(row=4, column=2)

        # labelFrame 用于盛放笔记列表
        self.lf2 = LabelFrame(self.frm, width=WIN_WIDTH/3+60, height=WIN_HEIGHT - 180, text='Note List')
        self.lf2.grid(row=1, column=0, padx=10)

        self.listb = Listbox(self.lf2, bg='#E0FFFF')  # list 用于放note 列表
        self.listb.place(x=0, y=0, width=WIN_WIDTH/3 + 50, height=WIN_HEIGHT - 230)
        self.countLabel = Label(self.lf2, bg='#E0FFFF')
        self.countLabel.place(x=140, y=375)
        self.updateCountLabel()
        yscrollbar = Scrollbar(self.listb, command=self.listb.yview)
        yscrollbar.pack(side=RIGHT, fill=Y)
        self.listb.config(yscrollcommand=yscrollbar.set)
        self.listb.bind('<<ListboxSelect>>', self.selectNote)  # 绑定响应函数


        # 显示笔记详细信息
        self.lf3 = LabelFrame(self.frm, width=WIN_WIDTH*2/3-100, height=WIN_HEIGHT-30, text='Note Details')
        self.lf3.grid(row=0, column=1, rowspan=2, padx=10, pady=10)
        self.detail = Text(self.lf3, bg='#E0FFFF', font=("宋体", 11, "normal"), state='disabled')
        self.detail.place(x=0, y=0, width=WIN_WIDTH*2/3-110, height=WIN_HEIGHT-50)

    # 点击笔记列表显示详细信息
    def selectNote(self, event):
        w = event.widget
        index = int(w.curselection()[0])
        editTime = self.searchResult[index]['time']
        timeStr = editTime[0:4] + '-' + editTime[4:6] + '-' + editTime[6:8] + ' ' + editTime[8:10] + ':' + editTime[10:12] + ':' + editTime[12:14]
        self.detail.config(state='normal')
        self.detail.delete('1.0', END)
        self.detail.insert(INSERT, '\t\t\t' + self.searchResult[index]['title'] + '\n')
        self.detail.insert(END, '\t\t' + ','.join(self.searchResult[index]['tags']) + '\n')
        self.detail.insert(END, '\t\t' + timeStr + '\n\n')
        self.detail.insert(END, self.searchResult[index]['description'])
        self.detail.config(state='disabled')

    # 得到所有的tags用于用户选择
    def getTags(self, data):
        tags = set('')
        for item in data:
            for tag in item['tags']:
                tags.add(tag)
        return tags

    # 根据title，tags，时间筛选记录
    def searchNotes(self, data):
        self.listb.delete(0, END)
        titleStr = self.titleEntry.get()
        startDate = self.dateStartEntry.get()
        endDate = self.dateEndEntry.get()
        tags = self.tagEntry.get()

        self.searchResult = []

        for item in data:
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
        self.updateCountLabel()

    # 选择tags
    def selectTags(self, *args):
        self.tagEntry.insert(END, self.tagChosen.get() + ' ')

    # 返回主界面
    def landingPage(self):
        self.frm.destroy()

    # 更新笔记列表下方搜索结果数量
    def updateCountLabel(self):
        self.countLabel['text'] = 'Total: ' + str(len(self.searchResult))
