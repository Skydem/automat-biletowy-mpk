from tkinter import *
from tkinter import font
from typing import Collection
import logic

class Application (Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.logic = logic()
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
        #new mainframe
        self.mainframe.destroy()
        self.mainframe = Frame(self.master)
        self.mainframe.grid(column=0, row=0, sticky=(W,E))
        
        #labels
        self.title = Label(self.mainframe, text='Automat Biletowy MPK', font=('bold', 14), pady=20).grid(row=0, column=0, sticky=(N,E,W), columnspan=3)
        self.tekst1 = Label(self.mainframe, text='Podsumowanie', pady=20, font=(12)).grid(row=1, column=0, sticky=W)

        #ilosc biletow
        self.bilet1_ilosc = 1
        self.bilet1 = Label(self.mainframe, text=(str(self.bilet1_ilosc)+"x 20 minut ulgowy")).grid(row=2,column=0, sticky=W)
        self.bilet1_dodaj = Button(self.mainframe, text="+",padx=5).grid(row=2,column=1,sticky=W)
        self.bilet1_usun = Button(self.mainframe, text="-",padx=5).grid(row=2,column=2,sticky=W)
        
        #suma
        self.suma_text = Label(self.mainframe, text="Łącznie: ").grid(row=3,column=0,sticky=W)
        self.suma_val = 0
        self.suma = Label(self.mainframe,text=(str(self.suma_val)+" zł")).grid(row=3,column=2,sticky=W)
        self.wrzucono_val = 0
        self.wrzucono_text = Label(self.mainframe,text="Wrzucono: ").grid(row=4,column=0,sticky=W)
        self.wrzucono = Label(self.mainframe,text=(str(self.wrzucono_val)+" zł")).grid(row=4,column=2,sticky=W)
        
        #wrzucanie monet
        self.white_space = Label(self.mainframe, text=' ', pady=10).grid(row=5,column=0, sticky=W)
        self.tekst2 = Label(self.mainframe, text='Wrzuć monety', font=(12)).grid(row=6, column=0, sticky=W)
        
        self.nazwy_monet = ["0.01 zł", "0.02 zł", "0.05 zł", "0.10 zł", "0.20 zł", "0.50 zł", "1.00 zł", "2.00 zł", "5.00 zł", "10.0 zł", "20.0 zł", "50.0 zł"]
        self.wartosci_monet = [1, 2, 5, 10, 20, 50, 100, 200, 500, 2000, 5000]

        row_moneta = 7
        i=0
        for moneta in self.nazwy_monet:
            print("row = "+str(row_moneta)+", column= "+str(i)) #debug
            Button(self.mainframe, text=moneta,padx=5).grid(row=row_moneta,column=i,sticky=(E, W),columnspan=1)
            
            i+=1
            if(i==6):
                row_moneta = 8
                i=0


        self.p1_platnosc = Button(self.mainframe, text='Powrot',pady=10, padx=20, command=lambda:[self.mainframe.destroy(), self.page1()]).grid(row=10, column=0, sticky=S, columnspan=6)

    
        


root = Tk()
app = Application(master=root)
app.mainloop()