import csv
import sys

class storage:
    def __init__(self):
        #init starting money
        self.money = {}
        self.filename = "money.csv"
        try:
            with open(self.filename) as f:
                money_file = csv.reader(f, delimiter=',')
                
                for key, value in money_file:
                    self.money[int(key)] = int(value)
        except IOError:
            print("Nie można otworzyć pliku")
        except PermissionError:
            print("Brak praw dostępy do pliku")
        except:
            print("Something went wrong")
            print(sys.exc_info()[:2])

    def save_to_file(self):
        try:
            with open(self.filename, 'w', newline='') as mf:
                for key, value in self.money.items():
                    row = key, value
                    mf.write(str(key))
                    mf.write(',')
                    mf.write(str(value))
                    mf.write("\n")
        except:
            print('Błąd przy zapisie stanu monet do pliku!!')
            print(sys.exc_info()[:2])

    def add(self, value, count):
        try:
            self.money[value] += count
        except KeyError:
            print("Nie istnieje taka moneta")
        except TypeError:
            print("Nieprawidłowa wartość zmiennej!")
        except:
            print(sys.exc_info()[:2])

        self.save_to_file()
        
        
    def sub(self, value, count):
        try:
            self.money[value] -= count
        except KeyError:
            print("Nie istnieje taka moneta")
        except TypeError:
            print("Nieprawidłowa wartość zmiennej!")
        except:
            print(sys.exc_info()[:2])

        self.save_to_file()

    def rest(self, inserted, price):
        self.to_give = inserted - price
        self.given = 0
        self.given_money = {k:0 for k in self.money.keys()}
        self.sum_money = sum([k*v for (k,v) in self.money.items()])
        if self.sum_money > self.to_give:
            while self.to_give > 0:
                for key, value in reversed(self.money.items()):
                    if int(value) > 0 and self.to_give - int(key) >= 0:
                        self.given += int(key)
                        self.to_give -= int(key)
                        self.given_money[int(key)] += 1
                        self.sub(key, 1)
                        break
        elif self.sum_money == self.to_give:
            print("a")
        else:
            print("Tylko odliczona kwota!")
                
                    
        print(self.given_money)
        print(self.given)




a = storage()
# a.add(1, 1)
# a.add(2, 2)
# a.add(5, 5)
# a.add(10, 10)
# a.add(20, 20)
a.rest(410, 210)
#print(a.money)
