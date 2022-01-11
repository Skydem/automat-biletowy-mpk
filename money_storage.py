import csv
import sys

class storage:
    def __init__(self):
        #init starting money
        self.money = {}
        try:
            with open("money.csv") as f:
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
    def add(self, value, count):
        try:
            self.money[value] += count
            
        except KeyError:
            print("Nie istnieje taka moneta")
        except TypeError:
            print("Nieprawidłowa wartość zmiennej!")
        except:
            print(sys.exc_info()[:2])




a = storage()
a.add(1, 1)
print(a.money)
