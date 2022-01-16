from email import message
from glob import glob
from tkinter import *
from tkinter import font
from tkinter import messagebox
from tokenize import String
from typing import Collection
import logic

class Application (Frame):
    """Klasa odpowiadająca za interfejs całej aplikacji."""
    def __init__(self, master):
        """Inicjalizacja parametrów okna a także zmiennych które będą używane w metodach poniżej. Klasa dziedziczy z Frame z modułu tkinter."""
        super().__init__(master)
        self.master = master
        self.logic = logic.logic(self.change_to_page1, self.show_window)
        master.title('Automat Biletowy MPK')
        master.geometry("150x400")
        master.minsize(height=500, width=400)
        self.nazwy_monet = ["0.01 zł", "0.02 zł", "0.05 zł", "0.10 zł", "0.20 zł", "0.50 zł", "1.00 zł", "2.00 zł", "5.00 zł", "10.0 zł", "20.0 zł", "50.0 zł"]
        #wartości podane są w groszach!
        self.wartosci_monet = [1, 2, 5, 10, 20, 50, 100, 200, 500, 1000, 2000, 5000]
        self.nazwy_biletow = ['20 Minut Ulgowy', '40 Minut Ulgowy', '60 Minut Ulgowy', '20 Minut Normalny', '40 Minut Normalny', '60 Minut Normalny']
        self.suma_val = StringVar()
        self.wrzucono_val = StringVar()
        self.page1()
    def page1(self):
        """Tworzenie widgetów służących do wyboru biletów"""
        #initi frame for this page
        self.mainframe = Frame(self.master)
        self.mainframe.grid(column=0, row=0, sticky=(W, E))
        self.title = Label(self.mainframe, text='Automat Biletowy MPK', font=('bold', 14), pady=20).grid(row=0, column=0, sticky=(N,E,W), columnspan=3)

        Button(self.mainframe, text="Testy", padx=5, command=lambda:[self.testy()]).grid(row=0, column=4, sticky=W) #wywołanie testów

        #labels - nagłówki
        self.ulgowy = Label(self.mainframe, text='Ulgowy', padx=10).grid(row=1, column=0, sticky=W)
        self.normalny = Label(self.mainframe, text='Normalny', padx=10).grid(row=1, column=2, sticky=W)
        self.white_space = Label(self.mainframe, text=' ', padx=20).grid(row=2,column=1, sticky=W)

        #buttons - przyciski służące do wyboru biletow 
        #20 minut
        self.u_20 = Button(self.mainframe, text='20 Minut 2,00 zł', padx=10, pady=10, command=lambda:[self.logic.add_ticket(1), self.page2()])
        self.u_20.grid(row=2, column=0, sticky=W)
        self.n_20 = Button(self.mainframe, text='20 Minut 4,00 zł', padx=10, pady=10, command=lambda:[self.logic.add_ticket(4), self.page2()])
        self.n_20.grid(row=2, column=2, sticky=W)

        #40 minut
        self.u_40 = Button(self.mainframe, text='40 Minut 2,50 zł', padx=10, pady=10, command=lambda:[self.logic.add_ticket(2), self.page2()])
        self.u_40.grid(row=3, column=0, sticky=W)
        self.n_40 = Button(self.mainframe, text='40 Minut 5,00 zł', padx=10, pady=10, command=lambda:[self.logic.add_ticket(5), self.page2()])
        self.n_40.grid(row=3, column=2, sticky=W)

        #60 minut
        self.u_60 = Button(self.mainframe, text='60 Minut 3,00 zł', padx=10, pady=10, command=lambda:[self.logic.add_ticket(3), self.page2()])
        self.u_60.grid(row=4, column=0, sticky=W)
        self.n_60 = Button(self.mainframe, text='60 Minut 6,00 zł', padx=10, pady=10, command=lambda:[self.logic.add_ticket(6), self.page2()])
        self.n_60.grid(row=4, column=2, sticky=W)

        #przycisk służący do przejścia do płatności jeżeli nie zdecydowaliśmy się na dodanie dodatkowych biletów
        self.platnosc = Button(self.mainframe, text='Przejdź do płatności', pady=10, padx=20, command=self.page2).grid(row=5, column=0, sticky=S, columnspan=3)

    def check_zero(self, key):
        """Metoda sprawdzająca czy podczas odejmowania biletów które wybraliśmy ilosć danego biletu nie osiągnęła 0.
        Służy by nie wprowadzić Zerowej lub ujemnej ilości biletów ponieważ odświeża ona proces kupowania"""
        if self.logic.chosen_tickets[key] == 0:
            self.mainframe.destroy()
            self.page1()

    def update_sum(self):
        """Metoda do odświeżania sumy cen biletów i reszty po: dodaniu biletu, odjeciu biletu, dodania monety"""
        self.suma_val.set((str(self.logic.price/100)+" zł"))
        self.wrzucono_val.set((str(self.logic.inserted/100)+ " zł"))

    def change_to_page1(self):
        """Metoda służąca do powrotu na stronę 1 (wybór biletów). Używana jest również jako argument przekyzwana do modułu logic by z poziomu logiki
        można wrócić do strony 1. Potrzebna jest ona w przypadku gdy reszta zostanie wydana tak więc transakcja została zakończona."""
        self.mainframe.destroy()
        self.page1()    

    def show_window(self, text, error=False):
        """Metoda służąca do pokazywania okna dialogowego np gdy automat wydaje resztę."""
        if error == False:
            messagebox.showinfo(title="Wydana reszta", message=text)
        else:
            messagebox.showerror(title="Nie można wydać", message=text)
        return

    def page2(self):
        """Tworzenie widgetów potrzebnych do sfinalizowania transakcji, tj: wybrane bilety, suma, pieniądze do wrzucenia"""
        #new mainframe
        self.mainframe.destroy()
        self.mainframe = Frame(self.master)
        self.mainframe.grid(column=0, row=0, sticky=(W,E))
        
        #labels
        self.title = Label(self.mainframe, text='Automat Biletowy MPK', font=('bold', 14), pady=20).grid(row=0, column=0, sticky=(N,E,W), columnspan=3)
        self.tekst1 = Label(self.mainframe, text='Podsumowanie', pady=20, font=(12)).grid(row=1, column=0, sticky=W)

        # ilosc biletow
        # dynamiczne dodawanie wybranych biletów na stronę
        # używana jest funkcja globals() służąca do tworzenia dynamicznych nazw zmiennych
        chosen_ticker_row = 2
        for key, value in self.logic.chosen_tickets.items():
            if value > 0:
                #label biletu
                globals()['ticket%s_text' % key] = StringVar()
                globals()['ticket%s_label' % key] = Label(self.mainframe, textvariable=(globals()['ticket%s_text' % key])).grid(row=chosen_ticker_row,column=0, sticky=W)
                globals()['ticket%s_text' % key].set((str(value)+"x "+self.nazwy_biletow[key-1]))

                #dodawanie i usuwanie biletow
                # w command używana jest lambda ze zmienną o nazwie key, by każdy przycisk inkrementacji i dekrementacji ilości biletów mógł wywołać kilka funkcji na raz
                # oraz by funkcje miały zachowane zmienne używane w funkcjach
                globals()['ticket%s_add' % key] = Button(self.mainframe, text="+", padx=5, command=lambda key=key:[self.logic.add_ticket(key), globals()['ticket%s_text' % key].set((str(self.logic.chosen_tickets[key])+"x"+self.nazwy_biletow[key-1])), self.update_sum()]).grid(row=chosen_ticker_row, column=1, sticky=W)
                globals()['ticket%s_sub' % key] = Button(self.mainframe, text="-", padx=5, command=lambda key=key:[self.logic.remove_ticket(key), globals()['ticket%s_text' % key].set((str(self.logic.chosen_tickets[key])+"x"+self.nazwy_biletow[key-1])), self.update_sum(), self.check_zero(key)]).grid(row=chosen_ticker_row, column=2, sticky=W)
                
                chosen_ticker_row += 1
        
        # suma cen biletów i wrzuconych pieniędzy
        self.suma_text = Label(self.mainframe, text="Łącznie: ").grid(row=3+6,column=0,sticky=W)
        self.suma = Label(self.mainframe,textvariable=self.suma_val).grid(row=3+6,column=2,sticky=W)
        
        self.wrzucono_text = Label(self.mainframe,text="Wrzucono: ").grid(row=4+6,column=0,sticky=W)
        self.wrzucono = Label(self.mainframe,textvariable=self.wrzucono_val).grid(row=4+6,column=2,sticky=W)

        self.update_sum()


        # wrzucanie monet
        # labels
        self.white_space = Label(self.mainframe, text=' ', pady=10).grid(row=5+6,column=0, sticky=W)
        self.tekst2 = Label(self.mainframe, text='Wrzuć monety', font=(12)).grid(row=6+6, column=0, sticky=W)
        

        row_moneta = 7+6
        i=0

        # by zaoszczędzić miejsce w kodzie przyciski dodawane są za pomocą pętli for
        # przyciski zawierają dwie funckje: Dodanie monety o podanym nominale i odświeżenie ceny i wartości wrzuconych monet
        # W pętli for używana jest funkcja zip która pozwala iterować przez dwie tablice, kończy swe działanie na krótszej z nich (w tym przypadku obie mają taką samą długość)
        for moneta, wartosc in zip(self.nazwy_monet, self.wartosci_monet):
            Button(self.mainframe, text=moneta,padx=5, command=lambda wartosc=wartosc: [self.logic.insert_coin(wartosc), self.update_sum()]).grid(row=row_moneta,column=i,sticky=(E, W),columnspan=1)            
            i+=1
            if(i==6):
                row_moneta = 8+6
                i=0

        #przycisk powrotu jeśli zażyczymy sobie dodanie innych biletów
        self.p1_platnosc = Button(self.mainframe, text='Powrot',pady=10, padx=20, command=lambda:[self.change_to_page1()]).grid(row=10+6, column=0, sticky=S, columnspan=6)
    
    def testy(self):
        """Metoda wywołująca testy na automacie. W konsoli widoczne będzie który test wykonuje się"""
        
        print("Test #1: Bilet kupiony za odliczoną kwotę")
        self.logic.add_ticket(2)
        self.logic.insert_coin(200)
        self.logic.insert_coin(50)

        print("Test #2: Bilet kupiony płacąc więcej")
        self.logic.add_ticket(2)
        self.logic.insert_coin(500)

        print("Test #3: Automat nie może wydać reszty")
        self.logic.add_ticket(2)
        self.logic.insert_coin(5000)
        self.logic.remove_ticket(2)

        print("Test #4: Zakup biletu płacąc 1 gr")
        self.logic.add_ticket(2)
        for i in range(249):
            self.logic.insert_coin(1)
        self.logic.insert_coin(1)

        print("Test #5: Kupno dwóch biletów")
        self.logic.add_ticket(2)
        self.logic.add_ticket(3)

        print("Oczekwiana suma: 5,50 zł, rzeczywista suma: ", self.logic.price)
        self.logic.insert_coin(500)
        self.logic.insert_coin(50)

        print("Test #6: Dodanie biletu, wrzucenie kilku monet, dodanie drugiego biletu")
        self.logic.add_ticket(4)
        #cena 4 zł
        self.logic.insert_coin(200)
        self.logic.add_ticket(5)
        #oczekwiana cena 9 zł
        self.logic.insert_coin(500)
        self.logic.insert_coin(200)

        print("Test #7 Próba wrzucenia ujemnej oraz niecałkowitej liczby monet")
        self.logic.add_ticket(1)
        self.logic.insert_coin(-1)
        #błąd
        self.logic.insert_coin(0.5)