from tkinter import *
from tkinter import font
from typing import Collection

class Application (Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        master.title('Automat Biletowy MPK')
        master.geometry("150x400")
        master.minsize(height=200, width=400)
        self.page1()
    def page1(self):
        #initi frame for this page
        self.p1_frame = Frame(self.master)
        self.p1_frame.grid(column=0, row=0, sticky=(W, E))

        self.p1_title = Label(self.p1_frame, text='Automat Biletowy MPK', font=('bold', 14), pady=20).grid(row=0, column=0, sticky=(N,E,W), columnspan=3)

        #labels
        self.p1_ulgowy = Label(self.p1_frame, text='Ulgowy', padx=10).grid(row=1, column=0, sticky=W)
        self.p1_normalny = Label(self.p1_frame, text='Normalny', padx=10).grid(row=1, column=2, sticky=W)
        self.p1_white_space = Label(self.p1_frame, text=' ', padx=20).grid(row=2,column=1, sticky=W)
        
        #buttons
        self.p1_u_20 = Button(self.p1_frame, text='20 Minut 2,00 zł', padx=10, pady=10).grid(row=2, column=0, sticky=W)
        self.p1_n_20 = Button(self.p1_frame, text='20 Minut 4,00 zł', padx=10, pady=10).grid(row=2, column=2, sticky=W)

        self.p1_u_40 = Button(self.p1_frame, text='40 Minut 2,50 zł', padx=10, pady=10).grid(row=3, column=0, sticky=W)
        self.p1_n_40 = Button(self.p1_frame, text='40 Minut 5,00 zł', padx=10, pady=10).grid(row=3, column=2, sticky=W)

        self.p1_u_60 = Button(self.p1_frame, text='60 Minut 3,00 zł', padx=10, pady=10).grid(row=4, column=0, sticky=W)
        self.p1_n_60 = Button(self.p1_frame, text='60 Minut 6,00 zł', padx=10, pady=10).grid(row=4, column=2, sticky=W)

        self.p1_platnosc = Button(self.p1_frame, text='Przejdź do płatności', pady=10, padx=20).grid(row=5, column=0, sticky=S, columnspan=3)

        

root = Tk()
app = Application(master=root)
app.mainloop()





# window=Tk()
# window.title("test")

# mainframe = Frame(window)
# mainframe.grid(column=0,row=0,sticky=W)

# frame2 = Frame(window)
# frame2.grid(column=1,row=0,sticky=E,padx=30)


# button1 = Button(mainframe,text='kappa')
# button1.grid(column=0,row=0)
# button3 = Button(mainframe,text='POGGERS')
# button3.grid(column=1,row=0)

# button2 = Button(frame2,text='kappucino')
# button2.grid(column=0,row=0)

# # mainframe.destroy()

# window.geometry("700x300")

# window.mainloop()