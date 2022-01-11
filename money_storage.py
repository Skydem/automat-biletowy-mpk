import csv
import sys
from tempfile import NamedTemporaryFile
import shutil

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


        try:
            filename = "money.csv"
            tempfile = NamedTemporaryFile('w+t', newline='', delete=False)

            with open(filename, 'r', newline='') as csvFile, tempfile:
                #reader = csv.reader(csvFile, delimiter=',')
                writer = csv.writer(tempfile, delimiter=',')

                for key, value in self.money.items():
                    writer.writerow({key, value})
            
            shutil.move(tempfile.name, filename)
        except:
            print('error!')
            print(sys.exc_info()[:2])




a = storage()
a.add(1, 1)
a.add(2, 2)
a.add(5, 5)
a.add(10, 10)
a.add(20, 20)
print(a.money)
