import money_storage

class logic:
    def __init__(self):
        #id:cena
        self.tickets = {1: 200, 2:250, 3:300, 4:400, 5:500, 6:600}
        self.chosen_tickets = {k:0 for k in self.tickets.keys()}
        self.price = 0
        self.inserted = 0
        self.ms = money_storage.storage()
        self.inserted_coins = self.ms.return_keys()
    def add_ticket(self, id):
        self.chosen_tickets[id] += 1
        self.price += self.tickets[id]
    def remove_ticket(self, id):
        self.chosen_tickets[id] -= 1
        self.price -= self.tickets[id]
    def refresh_data(self):
        print('wip')
    def insert_coin(self, coin):
        self.inserted += coin
        self.inserted_coins[coin] += 1
        self.ms.add(coin, 1)
        
a = logic()
a.insert_coin(2)
