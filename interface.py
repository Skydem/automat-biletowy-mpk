from tkinter import *
from tkinter import font

class Application (Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        master.title('Automat Biletowy MPK')
        master.geomtry("700x400")
        master.minsize(height=200, width=400)
        self.page1()
    def page1(self):
        print("placeholder")