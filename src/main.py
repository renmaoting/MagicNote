#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Tkinter import *

from tkinter import messagebox

from src.constants import WIN_HEIGHT, WIN_WIDTH
from src.createPage import CreatePage
from src.fileUtil import FileUtil
from src.searchPage import SearchPage


class MagicNote(object):
    def __init__(self):
        self.width = WIN_WIDTH
        self.height = WIN_HEIGHT
        self.root = Tk()
        self.root.title('Magic Note')
        self.root.geometry(self.getMainWinSize())
        self.frm = Frame(self.root, width=self.width, height=self.height)
        self.frm.place(x=0, y=0)

        self.lf1 = LabelFrame(self.frm, width=WIN_WIDTH - 10, height=WIN_HEIGHT - 10, text='Verify Password')
        self.lf1.grid(row=0, column=0, padx=350, pady=300)

        self.entry = Entry(self.lf1)
        self.entry.grid(row=0, column=0)

        self.submit = Button(self.lf1, text='Submit', command=self.verifyPassword)
        self.submit.grid(row=1, column=0)

    def verifyPassword(self):
        userInput = str(self.entry.get())
        if FileUtil.getPassword() == userInput:
            self.frm.destroy()
            self.frm = Frame(self.root, width=self.width, height=self.height)
            self.frm.place(x=0, y=0)
            #SearchPage(self.frm)
            CreatePage(self.frm)
            #self.createMenu()

        else:
            messagebox.showerror('Error', 'Invalid Password!')

    def getMainWinSize(self):
        screenwidth = self.root.winfo_screenwidth()
        screenheight = self.root.winfo_screenheight()
        return '%dx%d+%d+%d' % (self.width, self.height, (screenwidth - self.width) / 2, (screenheight - self.height) / 2)

    def createMenu(self):
        menubar = Menu(self.root)
        menubar.add_command(label='Create Notes', command=CreatePage)
        menubar.add_command(label='Search Notes', command=SearchPage)
        self.root.config(menu=menubar)
        mainloop()


def main():
    MagicNote()
    mainloop()


if __name__ == '__main__':
    main()
