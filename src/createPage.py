#!python3
# -*- coding: UTF-8 -*-
import datetime
from importlib import reload
from tkinter import *

from tkinter import messagebox
from tkinter.filedialog import askopenfilename

from src.constants import WIN_HEIGHT, WIN_WIDTH
from src.fileUtil import FileUtil

reload(sys)


class CreatePage(object):
    def __init__(self, master, updateList, data):
        self.frm = Frame(master, width=WIN_HEIGHT, height=WIN_HEIGHT)
        self.frm.place(x=0, y=0)
        self.lf1 = LabelFrame(self.frm, width=WIN_WIDTH - 10, height=WIN_HEIGHT - 10, text='Create Note')
        self.lf1.grid(row=0, column=0, padx=30, pady=90)

        Label(self.lf1, text='Title:').grid(row=0)
        self.title = Entry(self.lf1, width=80)
        self.title.grid(row=0, column=1, columnspan=8, pady=10)

        Label(self.lf1, text='Tags:').grid(row=1, column=0)
        self.tags = Entry(self.lf1, width=80)
        self.tags.grid(row=1, column=1, columnspan=8, pady=10)
        Label(self.lf1, text='Description:').grid(row=2, column=0)
        self.description = Text(self.lf1, width=120, height=30, bg='#E0FFFF')
        self.description.grid(row=2, column=1, columnspan=10, pady=10)

        Button(self.lf1, text='Import Existing Notes', command=lambda: self.chooseFile(updateList, data)).grid(row=3, column=4)
        Button(self.lf1, text='Submit New Note', command=lambda: self.addNote(updateList, data)).grid(row=3, column=5)
        Button(self.lf1, text='Home Page', command=self.landingPage).grid(row=3, column=6)

    # 导入notes
    def chooseFile(self, updateList, data):
        path = askopenfilename()
        if len(path.strip()) == 0:
            return

        importedNotes = FileUtil.getNoteRecords(path)
        if len(importedNotes) == 0:
            return

        for item in importedNotes:
            data.append(item)
        FileUtil.setNoteRecords(data)
        updateList(data)
        messagebox.showerror('Succeed', 'Notes have been imported!')

    def addNote(self, updateList, data):
        curTime = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
        titleVal = self.title.get()
        tagsVal = self.tags.get().replace(' ', '').split(',')
        descriptionVal = self.description.get(0.0, END).strip()

        if len(titleVal) == 0 or len(descriptionVal) == 0:
            messagebox.showerror('Error', 'title or description can not be empty!')
            return

        note = {'title': titleVal, 'tags': tagsVal, 'description': descriptionVal, 'time': curTime}
        data.insert(0, note)

        FileUtil.setNoteRecords(data)
        messagebox.showerror('Succeed', 'Note has been added!')
        updateList(data)

        self.title.delete(0, END)
        self.tags.delete(0, END)
        self.description.delete('1.0', END)

    def landingPage(self):
        self.frm.destroy()
