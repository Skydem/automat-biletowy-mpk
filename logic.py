import money_storage
import sys

class logic:
    def __init__(self):
        #id:cena
        self.tickets = {1: 200, 2:250, 3:300, 4:400, 5:500, 6:600}
        self.chosen_tickets = {k:0 for k in self.tickets.keys()}
        self.price = 0
        self.inserted = 0
        self.rest = 0
        self.ms = money_storage.storage()
        self.inserted_coins = self.ms.return_keys()
    def add_ticket(self, id, quantity=1):
        self.chosen_tickets[id] += quantity
        self.price += self.tickets[id]
        print("Dodano bilet!")
        print(self.chosen_tickets)
    def remove_ticket(self, id, quantity=1):
        self.chosen_tickets[id] -= quantity
        self.price -= self.tickets[id]
    def refresh_data(self):
        print('wip')
    def check_rest(self):
        print("----check rest----")
        b = self.ms.rest(self.inserted, self.price)
        if b:
            for key, value in b.items():
                self.inserted_coins[key] = 0
                if value > 0:
                    print("Wydaje: {}gr x{}".format(key, value))
            self.ms.save_to_file(self.ms.temp_money)
            self.inserted = 0
            self.chosen_tickets = {k:0 for k in self.tickets.keys()}
            self.rest = 0
            self.price = 0
            

        else:
            print("Nie można wydać reszty, tylko odliczona kwota")
            for key, value in self.inserted_coins.items():
                self.ms.sub(key, value, True)
                if value > 0:
                    print("Wydaje: {}gr x{}".format(key, value))
                self.inserted_coins[key] = 0
            self.inserted = 0
            self.rest = 0
    def insert_coin(self, coin, quantity=1):
        try:
            self.inserted_coins[coin] += quantity
            self.inserted += coin
            self.ms.add(coin, quantity, True)
            self.rest = self.inserted - self.price
            
            print("Do zapłaty {}, Wpłacono {}, Reszta {}".format(self.price, self.inserted, self.rest))
            if self.rest >= 0:
                
                self.check_rest()
                
        except:
            print("otrzymałem: ", coin)
            print(sys.exc_info()[:2])
            print("Nieznana moneta!")


# a = logic()
# a.add_ticket(1)
# a.insert_coin(500)
