# Automat Biletowy MPK - projekt na JS

Projekt miał na celu stworzenie aplikacji automatu biletowego MPK w języku Python. 

## Rozdziały:
* [Założenia](#założenia)
* [Ogólny opis kodu](#ogólny-opis-kodu)
* [Sukcesy i problemy](#sukcesy-i-problemy)
* [Istotne fragmenty kodu](#istotne-fragmenty-kodu)

## Założenia
* Projekt ma być aplikacją okienkową.
* Automat przechowuje informacje o monetach i banknotach znajdujących się w nim.
* Do wybrania było 6 typów biletów w wariantach uglowym i normalnym:
    * 20 minutowy
    * 40 minutowy
    * 60 minutowy
* Możliwość wybrania więcej niż jednego rodzaju biletu. Możliwość wprowadzenia liczby biletów.
* Automat ma wydawać resztę. Jeżeli nie może, powinien poinformować o możliwości wrzucenia tylko odliczonej kwoty

## Ogólny opis kodu
Projekt został podzielony na 3 moduły, który każdy z nich odpowiada za swoją część. Projekt zawiera plik `money.csv` który zawiera wystarczającą ilość monet by wykonać testy. 
* ### Moduł interfejsu:
    Nazwa pliku: `interface.py`
    
    Komponent aplikacji który renderuje widgety (elementy na stronie). Dzięki niemu możemy z łatwością odnaleźć się w aplikacji bez pamietania funkcji które musiałyby być wywołane w konsoli interpretera. Interfejs składa się łącznie z dwóch głownych stron: strony z wyborem biletów i strony gdzie znajduje się podsumowanie i możemy dokonać płatności.
* ### Moduł logiki:
    Nazwa pliku: `logic.py`

    Komponent odpowiadający za logikę odbywającą się za dodawaniem biletów, wrzucaniem pieniędzy, sprawdzaniem czy transakcja została zakończona pomyślnie i wydawaniem reszty.

* ### Moduł obsługi pieniędzy:
    Nazwa pliku: `money_storage.py`

    Komponent odpowiadający za obsługę pieniędzy zapisanych w pliku (sejfie). Dodaje pieniądze do pliku, odejmuje i również zawiera algorytm który wydaje resztę w odpowiednich monetach/banknotach.

## Sukcesy i problemy
### Sukcesy
* Pomyślnie zaimplenetowano wszystkie wymagania co do projektu. 
* Użyto własnego algorytmu wydawania pieniędzy.
* Wszystkie testy zakończone powodzeniem.
* Dodano istotne fragmenty kodu znajdujące się w wymaganiach.
### Problemy
* Obsługa groszy.

## Istotne fragmenty kodu
### Lambda-wyrażenia:
* [Obsługa przycisków wrzucania monet](https://github.com/Skydem/automat-biletowy-mpk/blob/bb03119df47fdf52e92f35707688318f31744bbf/interface.py#L142)
* [Dodawanie i odejmowanie biletów](https://github.com/Skydem/automat-biletowy-mpk/blob/bb03119df47fdf52e92f35707688318f31744bbf/interface.py#L114-L115)
* [Powrót do strony głównej](https://github.com/Skydem/automat-biletowy-mpk/blob/bb03119df47fdf52e92f35707688318f31744bbf/interface.py#L149)
### List comprehensions
* [Link](https://github.com/Skydem/automat-biletowy-mpk/blob/bb03119df47fdf52e92f35707688318f31744bbf/logic.py#L10)
* [Link](https://github.com/Skydem/automat-biletowy-mpk/blob/bb03119df47fdf52e92f35707688318f31744bbf/money_storage.py#L68)
* [Link](https://github.com/Skydem/automat-biletowy-mpk/blob/bb03119df47fdf52e92f35707688318f31744bbf/money_storage.py#L106)
### Klasy
* [Interfejs](https://github.com/Skydem/automat-biletowy-mpk/blob/bb03119df47fdf52e92f35707688318f31744bbf/interface.py#L10)
* [Logika](https://github.com/Skydem/automat-biletowy-mpk/blob/bb03119df47fdf52e92f35707688318f31744bbf/logic.py#L5)
* [Obsługa pieniędzy](https://github.com/Skydem/automat-biletowy-mpk/blob/bb03119df47fdf52e92f35707688318f31744bbf/money_storage.py#L4)
### Wyjątki
* [Link](https://github.com/Skydem/automat-biletowy-mpk/blob/bb03119df47fdf52e92f35707688318f31744bbf/logic.py#L63)
* [Link](https://github.com/Skydem/automat-biletowy-mpk/blob/bb03119df47fdf52e92f35707688318f31744bbf/money_storage.py#L11)
* [Link](https://github.com/Skydem/automat-biletowy-mpk/blob/bb03119df47fdf52e92f35707688318f31744bbf/money_storage.py#L41)

### Moduły
* [Moduł interfejsu](https://github.com/Skydem/automat-biletowy-mpk/blob/bb03119df47fdf52e92f35707688318f31744bbf/interface.py)
* [Moduł logiki](https://github.com/Skydem/automat-biletowy-mpk/blob/bb03119df47fdf52e92f35707688318f31744bbf/logic.py)
* [Moduł Obsługi pieniędzy](https://github.com/Skydem/automat-biletowy-mpk/blob/bb03119df47fdf52e92f35707688318f31744bbf/money_storage.py)