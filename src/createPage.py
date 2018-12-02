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
    def __init__(self, master, initialLandingPage, data):
        self.frm = Frame(master, width=WIN_HEIGHT, height=WIN_HEIGHT)
        self.frm.place(x=0, y=0)
        self.lf1 = LabelFrame(self.frm, width=WIN_WIDTH - 10, height=WIN_HEIGHT - 10, text='Create Note')
        self.lf1.grid(row=0, column=0, padx=40, pady=30)

        Label(self.lf1, text='Title:').grid(row=0)
        self.title = Entry(self.lf1, width=70)
        self.title.grid(row=0, column=1, columnspan=8, pady=6)

        Label(self.lf1, text='Tags:').grid(row=1, column=0)
        self.tags = Entry(self.lf1, width=70)
        self.tags.grid(row=1, column=1, columnspan=8, pady=6)
        Label(self.lf1, text='Description:').grid(row=2, column=0)
        self.description = Text(self.lf1, width=80, height=23, bg='#E0FFFF', font=("宋体", 14, "normal"))
        self.description.grid(row=2, column=1, columnspan=6, pady=6)

        Button(self.lf1, text='Import Existing Notes', command=lambda: self.chooseFile(data)).grid(row=3, column=2)
        Button(self.lf1, text='Submit New Note', command=lambda: self.addNote(data)).grid(row=3, column=3)
        Button(self.lf1, text='Home Page', command=lambda: self.landingPage(initialLandingPage, master, data)).grid(row=3, column=5)

    # 导入notes
    def chooseFile(self, data):
        path = askopenfilename()
        if len(path.strip()) == 0:
            return

        importedNotes = FileUtil.getNoteRecords(path)
        if len(importedNotes) == 0:
            return

        for item in importedNotes:
            data.append(item)
        FileUtil.setNoteRecords(data)
        messagebox.showerror('Succeed', 'Notes have been imported!')

    def addNote(self, data):
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

        self.title.delete(0, END)
        self.tags.delete(0, END)
        self.description.delete('1.0', END)

    def landingPage(self, initialLandingPage, master, data):
        self.frm.destroy()
        initialLandingPage(master, data)
