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
        self.mainframe = Frame(self.master)
        self.mainframe.grid(column=0, row=0, sticky=(W, E))

        self.title = Label(self.mainframe, text='Automat Biletowy MPK', font=('bold', 14), pady=20).grid(row=0, column=0, sticky=(N,E,W), columnspan=3)

        #labels
        self.ulgowy = Label(self.mainframe, text='Ulgowy', padx=10).grid(row=1, column=0, sticky=W)
        self.normalny = Label(self.mainframe, text='Normalny', padx=10).grid(row=1, column=2, sticky=W)
        self.white_space = Label(self.mainframe, text=' ', padx=20).grid(row=2,column=1, sticky=W)

        #buttons
        self.u_20 = Button(self.mainframe, text='20 Minut 2,00 zł', padx=10, pady=10).grid(row=2, column=0, sticky=W)
        self.n_20 = Button(self.mainframe, text='20 Minut 4,00 zł', padx=10, pady=10).grid(row=2, column=2, sticky=W)

        self.u_40 = Button(self.mainframe, text='40 Minut 2,50 zł', padx=10, pady=10).grid(row=3, column=0, sticky=W)
        self.n_40 = Button(self.mainframe, text='40 Minut 5,00 zł', padx=10, pady=10).grid(row=3, column=2, sticky=W)

        self.u_60 = Button(self.mainframe, text='60 Minut 3,00 zł', padx=10, pady=10).grid(row=4, column=0, sticky=W)
        self.n_60 = Button(self.mainframe, text='60 Minut 6,00 zł', padx=10, pady=10).grid(row=4, column=2, sticky=W)

        self.platnosc = Button(self.mainframe, text='Przejdź do płatności', pady=10, padx=20, command=self.page2).grid(row=5, column=0, sticky=S, columnspan=3)

    def page2(self):
        
        self.mainframe.destroy()
        self.mainframe = Frame(self.master)
        self.mainframe.grid(column=0, row=0, sticky=(W,E))
        
        self.title = Label(self.mainframe, text='Automat Biletowy MPK', font=('bold', 14), pady=20).grid(row=0, column=0, sticky=(N,E,W), columnspan=3)

        self.tekst1 = Label(self.mainframe, text='Podsumowanie', pady=20).grid(row=1, column=0, sticky=W)

        #ilosc biletow

        
        self.p1_platnosc = Button(self.mainframe, text='Powrot', pady=10, padx=20, command=lambda:[self.mainframe.destroy(), self.page1()]).grid(row=5, column=0, sticky=S, columnspan=3)

    
        

        

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