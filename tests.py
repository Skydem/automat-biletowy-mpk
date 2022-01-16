from interface import *
from logic import *
from tkinter import *
import unittest

root = Tk()
app = Application(master=root)


class Test(unittest.TestCase):
    def test1(self):
        # cena 2zł, wrzucamy 1x 2zł, oczekiwana reszta 0 zł
        app.logic.add_ticket(1)
        self.assertEqual(app.logic.insert_coin(200, 1, False), 0)
    def test2(self):
        # cena 2 zł, wrzucamy 1x 5zł, oczekiwana reszta 3zł (300 gr)
        app.logic.add_ticket(1)
        self.assertEqual(app.logic.insert_coin(500, 1, False), 300)
    def test3(self):
        # cena 2 zł, wrzucamy 100x 50zł, oczekiwany błąd i tablica [5000, 100] ([nominał, ilosć])
        app.logic.add_ticket(1)
        a, b = app.logic.insert_coin(5000, 100, False)
        self.assertFalse(a)
        self.assertEqual(b, [5000, 100], 'Test #3: Nie można zwrócić reszty')
        app.logic.remove_ticket(1)
    def test4(self):
        # cena 2 zł, wrzucamy 200x 1gr, oczekiwana reszta 0 zł
        app.logic.add_ticket(1)
        self.assertEqual(app.logic.insert_coin(1, 200, False), 0)
    def test5(self):
        # cena 2zł+2,50zł=4,50zł, wrzucamy 9x 50gr, oczekiwana reszta 0 zł
        app.logic.add_ticket(1)
        app.logic.add_ticket(2)
        self.assertEqual(app.logic.insert_coin(50, 9, False), 0)
    def test6(self):
        app.logic.add_ticket(1) # bilet 2 zł
        app.logic.insert_coin(20, 3, False) # 3x 20gr = 60 gr
        app.logic.insert_coin(50, 1, False) # 1x 50 gr, Suma: 1,10 zł
        app.logic.add_ticket(2) # bilet 2,5 zł, suma 4,5 zł
        app.logic.insert_coin(200, 1, False) # 1x 2zł, Suma: 3,10 zł
        app.logic.insert_coin(100, 1, False) # 1x 1zł, Suma: 4,10
        self.assertEqual(app.logic.insert_coin(20, 2, False), 0) #2x 20 gr, Suma 4,50, Oczekiwany brak reszty
    def test7(self):
        with self.assertRaises(Exception, msg="Nieznana moneta -1!"):
            app.logic.insert_coin(-1, 1,False)
        with self.assertRaises(Exception, msg="Nieznana moneta 0.5!"):
            app.logic.insert_coin(0.5, 1, False)

unittest.main(verbosity=True)

# app.logic.add_ticket(1)
# app.logic.add_ticket(2)
# print(app.logic.chosen_tickets)
# app.logic.insert_coin(500, 1, False)
# print(app.logic.insert_coin(50, 1, False))