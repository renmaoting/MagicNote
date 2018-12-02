#!python3
# -*- coding: UTF-8 -*-
from tkinter import *

from tkinter import messagebox

from src.constants import WIN_HEIGHT, WIN_WIDTH
from src.fileUtil import FileUtil
from src.landingPage import LandingPage


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
        self.lf1.grid(row=0, column=0, padx=350, pady=150)

        self.entry = Entry(self.lf1, show='*')
        self.entry.grid(row=0, column=0)

        self.submit = Button(self.lf1, text='Submit', command=self.verifyPassword)
        self.submit.grid(row=1, column=0)

        self.lf2 = LabelFrame(self.frm, width=WIN_WIDTH - 10, height=WIN_HEIGHT - 10, text='Tech Support')
        self.lf2.grid(row=1, column=0)
        self.authorInfo = Text(self.lf2, width=25, height=5, bg='#E0FFFF')
        self.authorInfo.grid(row=0, column=0)
        self.authorInfo.insert(END, 'Author: 小榕流光\n')
        self.authorInfo.insert(END, 'Email: rmtustc@gmail.com\n')
        self.authorInfo.insert(END, 'Wechat: Jonah-Ren\n\n')
        self.authorInfo.insert(END, 'All Rights Reserved')
        self.authorInfo.config(state='disabled')

        # 预加载数据，减少数据量大时的卡顿
        self.data = FileUtil.getNoteRecords()

    def verifyPassword(self):
        userInput = str(self.entry.get())
        if FileUtil.getPassword().strip() == userInput.strip():
            self.frm.destroy()
            self.frm = Frame(self.root, width=self.width, height=self.height)
            self.frm.place(x=0, y=0)
            LandingPage(self.root, self.data)
        else:
            messagebox.showerror('Error', 'Invalid Password!')

    def getMainWinSize(self):
        screenwidth = self.root.winfo_screenwidth()
        screenheight = self.root.winfo_screenheight()
        return '%dx%d+%d+%d' % (self.width, self.height, (screenwidth - self.width) / 2, (screenheight - self.height) / 2)


def main():
    MagicNote()
    mainloop()


if __name__ == '__main__':
    main()
