#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Tkinter import *

from src.browsePage import BrowsePage
from src.createPage import CreatePage
from src.fileUtil import FileUtil
from src.searchPage import SearchPage


class MagicNote(object):
    def __init__(self):
        self.width = 800
        self.height = 600
        self.root = Tk()
        self.root.title('Magic Note')
        self.root.geometry(self.getMainWinSize())
        self.frm = Frame(self.root, width=self.width, height=self.height, bg='green')
        self.frm.place(x=0, y=50)
        Label(self.frm, text='Input Password:').place(x=200, y=200, anchor='nw')

        self.entry = Entry(self.frm, width=10)
        self.entry.place(x=310, y=200)

        self.submit = Button(self.frm, text='Submit', command=self.verifyPassword)
        self.submit.place(x=420, y=200)

    def verifyPassword(self):
        userInput = str(self.entry.get())
        if FileUtil.getPassword() == userInput:
            self.frm.destroy()
            self.frm = Frame(self.root, width=self.width, height=self.height)
            self.frm.place(x=0, y=0)
            SearchPage(self.frm)

        else:
            print 'no'

    def getMainWinSize(self):
        screenwidth = self.root.winfo_screenwidth()
        screenheight = self.root.winfo_screenheight()
        return '%dx%d+%d+%d' % (self.width, self.height, (screenwidth - self.width) / 2, (screenheight - self.height) / 2)

    def createMenu(self):
        menubar = Menu(self.root)
        menubar.add_command(label='Create Notes', command=self.createNoteWin)
        menubar.add_command(label='Search Notes', command=self.createSearchWin)
        self.root.config(menu=menubar)
        mainloop()

    def createSearchWin(self):
        self.frm.destroy()
        self.frm = Frame(self.root, width=self.width, height=self.height)
        self.frm.place(x=0, y=0)

    def createNoteWin(self):
        self.frm = Frame(self.root, width=self.width, height=self.height)
        self.frm.place(x=0, y=0)
        CreatePage(self.frm)

def main():
    note = MagicNote()
    mainloop()
    pass


if __name__ == '__main__':
    main()
