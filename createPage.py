#!/usr/bin/python
# -*- coding: UTF-8 -*-
import io
import sys
import json
import datetime
from Tkinter import *
from src.constants import NOTES_FILE_PATH
from src.fileUtil import FileUtil

reload(sys)
sys.setdefaultencoding("utf-8")


class CreatePage(object):
    def __init__(self, master):
        Button(master, text='Add Note', command=self.addNote).grid(row=3, column=1)
        Label(master, text='Title:').grid(row=0)
        self.title = Entry(master, width=60)
        self.title.grid(row=0, column=1)
        Label(master, text='Tags:').grid(row=1, column=0)
        self.tags = Entry(master, width=60)
        self.tags.grid(row=1, column=1)
        Label(master, text='Description:').grid(row=2, column=0)
        self.description = Text(master, width=100, height=15, bg='#E0FFFF')
        self.description.grid(row=2, column=1)

    def addNote(self):
        print 'added one note'
        curTime = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
        note = {'title': self.title.get(), 'tags': self.tags.get().strip().split(','), 'description': self.description.get(0.0, END), 'time': curTime}
        data = FileUtil.getNoteRecords()
        data.append(note)

        dic_json = json.dumps(data, ensure_ascii=False, indent=4)
        fw = io.open(NOTES_FILE_PATH, 'w', encoding='utf-8')
        fw.write(dic_json)
        fw.close()
