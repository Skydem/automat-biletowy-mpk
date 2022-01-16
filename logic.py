import money_storage
import sys
import interface

class logic:
    """Klasa odpowiadająca za logikę w systemie. Jest połączeniem pomiędzy interfejsem a modułem obsługujacym pieniądze w maszynie."""
    def __init__(self, fn, fn2):
        """Inicjalizacja zmiennych."""
        self.tickets = {1: 200, 2:250, 3:300, 4:400, 5:500, 6:600} # id:cena(w groszach)
        self.chosen_tickets = {k:0 for k in self.tickets.keys()} # słownik z wybranymi biletami ID_biletu:0 
        self.price = 0 # łączna cena biletów
        self.inserted = 0 # suma wrzuconych pieniędzy
        self.rest = 0 # reszta do wydania
        self.change_page = fn # funkcja służąca do zmiany strony po zakończonej transakcji
        self.window = fn2 # funkcja do wyświetlania okien dialogowych
        self.ms = money_storage.storage() # moduł obsługi pieniędzy
        self.inserted_coins = self.ms.return_keys() # wrzucone pieniądze Nominał:ilość=0

    def add_ticket(self, id, quantity=1):
        """Dodanie biletu o podanym ID i podanej ilośći(domyślnie 1), zaktualizowanie łącznej ceny biletów"""
        self.chosen_tickets[id] += quantity
        self.price += self.tickets[id]
    def remove_ticket(self, id, quantity=1):
        """Usunięcie biletu o podanym ID i danej ilośći(domyślnie 1), zaktualizowanie łącznej ceny biltów"""
        self.chosen_tickets[id] -= quantity
        self.price -= self.tickets[id]
    def check_rest(self):
        """Metoda sprawdzająca czy reszta może być wydana, jeżeli tak, wydaj resztę pokazując okno dialogowe, jeżli nie, wyświetl komunikat o możliwośći zapłaty
        tylko odliczoną kwotą i zwróć wrzucone pieniądze"""

        b = self.ms.rest(self.inserted, self.price) # zmienna przechowujaca False lub słownik z możliwą kombinacją pieniedzy do wydania które jest zwracane z modułu obsługi pieniędzy
        temp_text = "Wydaje: \n"
        temp_error = "Nie można wydać reszty! Tylko odliczona kwota!\nOddaję:"
        if b:
            for key, value in b.items():
                self.inserted_coins[key] = 0
                if value > 0:
                    temp_text += f'{key/100}zł x{value}\n'
                    self.ms.sub(key, value, True)
            # transakcja zakończona sukcesem, zerowanie poniższych zmiennych
            self.inserted = 0 
            self.chosen_tickets = {k:0 for k in self.tickets.keys()}
            self.rest = 0
            self.price = 0
            self.window(temp_text)
            self.change_page()
            return True # return używany do testów
            
        else:
            # nie można wydać reszty, oddaj pieniądze lecz nie zeruj wybranych biletów
            for key, value in self.inserted_coins.items():
                self.ms.sub(key, value, True)
                if value > 0:
                    temp_error += f'{key/100}zł x{value}\n'
                self.inserted_coins[key] = 0
            self.inserted = 0
            self.rest = 0
            self.window(temp_error, True)
            return False # return używany do testów
    def insert_coin(self, coin, quantity=1):
        """Metoda dodająca monetę do systemu. Jest ona wrzucana do 'sejfu', suma wrzuconych pieniędzy zostaje aktualizwana, obliczana jest reszta.
        W momencie gdy zwracana reszta jest większa lub równa 0, wywołaj metodę sprawdzającą czy z wrzuconych pieniędzy można wydać resztę."""
        try:
            self.inserted_coins[coin] += quantity
            self.inserted += coin
            self.ms.add(coin, quantity, True) # True odpowiada za zapis monet do pliku(sejfu), dzięki czemu jesteśmy w stanie wydać resztę z pieniędzy użytkownika jeśli wrzuci np znacznie za dużo
            self.rest = self.inserted - self.price
            
            if self.rest >= 0:
                self.check_rest()
                
        except:
            # Obsługa błędu
            print("otrzymałem: ", coin)
            print(sys.exc_info()[:2])
            print("Nieznana moneta!")
