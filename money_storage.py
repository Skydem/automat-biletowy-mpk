import csv
import sys

class storage:
    """Klasaa odpowiadająca za obsługę pieniędzy"""
    def __init__(self):
        """Inicjalizacja słownika ze zmiennymi służącego później do obliczania."""
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

    def save_to_file(self, dict):
        """Metoda zapisu słownika z pieniędzmi do pliku (sejfu)"""
        try:
            with open(self.filename, 'w', newline='') as mf:
                for key, value in dict.items():
                    row = key, value
                    mf.write(str(key))
                    mf.write(',')
                    mf.write(str(value))
                    mf.write("\n")
        except:
            print('Błąd przy zapisie stanu monet do pliku!!')
            print(sys.exc_info()[:2])

    def add(self, value, count, save=False):
        """Metoda na dodanie pieniędzy do głównego słownika. Domyślnie nie zapisuje do pliku, można to zmienić dodająć True."""
        try:
            self.money[value] += count
        except KeyError:
            print("Nie istnieje taka moneta")
        except TypeError:
            print("Nieprawidłowa wartość zmiennej!")
        except:
            print(sys.exc_info()[:2])
        if save == True:
            self.save_to_file(self.money)
        
        
    def sub(self, value, count, save=False):
        """Metoda na odejmowanie pieniędzy głównego do słownika. Domyślnie nie zapisuje do pliku, można to zmienić dodająć True."""
        try:
            self.money[value] -= count
        except KeyError:
            print("Nie istnieje taka moneta")
        except TypeError:
            print("Nieprawidłowa wartość zmiennej!")
        except:
            print(sys.exc_info()[:2])
        if save == True:
            self.save_to_file(self.money)

    def return_sum(self):
        """Metoda zwracająca sumę wszystkich pieniędzy znajdujących się w głównym słowniku"""
        return sum([k*v for (k,v) in self.money.items()])

    def rest(self, inserted, price):
        """Metoda obliczająca czy możliwe jest wydane reszty. Za argumenty przyjmuje sumę pieniędzy wrzuconych do automatu i sumę ceny biletów. Zwraca False lub słownik z 
        możliwą kombinacją pieniędzy do wydania."""
        self.to_give = inserted - price # ile musi wydać
        self.given = 0 # ile już wydało
        self.given_money = {k:0 for k in self.money.keys()} # słownik nominał:ilość_monet=0
        self.sum_money = self.return_sum() # suma pieniędzy w pliku(sejfie)
        self.temp_money = self.money.copy() # kopia słownika głównego służąca że w razie niepowodzenia wydania reszty, główny słownik pozostaje bez zmian
        fuse = 0 # bezpiecznik służący do zatrzymania algorytmu

        if self.sum_money >= self.to_give: # jeżeli suma monet w pliku(sejfie) jest większa niż suma pieniędzy do wydania, wykonaj algorytm
            while self.to_give > 0: # dopóki jest co wydać, kontynuuj
                for key, value in reversed(self.temp_money.items()): #s łownik jest sprawdzany od tyłu, by wydać resztę jak najmniejszym nakładem ilośći pieniędzy
                    if int(value) > 0 and self.to_give - int(key) >= 0: # jeżeli jest moneta o danym nominale i suma do wydania - moneta >= 0 wykonaj poniżej
                        self.given += int(key)
                        self.to_give -= int(key)
                        self.given_money[int(key)] += 1 # dodaj 1 do ilośći monet do wydania do monety o nominale key
                        self.temp_money[key] -= 1
                        fuse = 0
                        break
                    else:
                        fuse+=1
                        if fuse == 1000: # w momencie gdy bezpiecznik osiągnie próg (ponieważ nie jest możliwe wydanie reszty) przerwij pętle
                            break
                if fuse == 1000:
                    break
            if fuse == 1000:
                return False
        else:
            return False

        return self.given_money # zwróc słownik z pieniędzmi do wydania (obsługiwany w module logic)
                    

    def return_keys(self):
        """Zwraca słownik monet nominał:0"""
        return {k:0 for k in self.money.keys()}
