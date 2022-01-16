import money_storage
import sys
import interface

class logic:
    def __init__(self, fn, fn2):
        #id:cena
        self.tickets = {1: 200, 2:250, 3:300, 4:400, 5:500, 6:600}
        self.chosen_tickets = {k:0 for k in self.tickets.keys()}
        self.price = 0
        self.inserted = 0
        self.rest = 0
        self.change_page = fn
        self.window = fn2
        self.ms = money_storage.storage()
        self.inserted_coins = self.ms.return_keys()
    def add_ticket(self, id, quantity=1):
        self.chosen_tickets[id] += quantity
        self.price += self.tickets[id]
    def remove_ticket(self, id, quantity=1):
        self.chosen_tickets[id] -= quantity
        self.price -= self.tickets[id]
    def check_rest(self):
        b = self.ms.rest(self.inserted, self.price)
        temp_text = "Wydaje: \n"
        temp_error = "Nie można wydać reszty! Tylko odliczona kwota!\nOddaję:"
        if b:
            for key, value in b.items():
                self.inserted_coins[key] = 0
                if value > 0:
                    temp_text += f'{key/100}zł x{value}\n'
                    self.ms.sub(key, value, True)
            self.inserted = 0
            self.chosen_tickets = {k:0 for k in self.tickets.keys()}
            self.rest = 0
            self.price = 0
            self.window(temp_text)
            self.change_page()
            return True
            
        else:
            for key, value in self.inserted_coins.items():
                self.ms.sub(key, value, True)
                if value > 0:
                    temp_error += f'{key/100}zł x{value}\n'
                self.inserted_coins[key] = 0
            self.inserted = 0
            self.rest = 0
            self.window(temp_error, True)
            return False
    def insert_coin(self, coin, quantity=1):
        try:
            self.inserted_coins[coin] += quantity
            self.inserted += coin
            self.ms.add(coin, quantity, True)
            self.rest = self.inserted - self.price
            
            if self.rest >= 0:
                self.check_rest()
                
        except:
            print("otrzymałem: ", coin)
            print(sys.exc_info()[:2])
            print("Nieznana moneta!")
