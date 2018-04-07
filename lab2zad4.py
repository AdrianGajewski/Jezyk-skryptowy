from math import pi

def dodawanie(x, y):
   return x + y

def odejmowanie(x, y):
   return x - y

def mnozenie(x, y):
   return x * y

def dzielenie(x, y):
    if y == 0:
        return "Dzielisz przez 0!!!"
    else:
        return x / y

def polekola(r):
    return pi * r * r

def obwodkola(r):
    return 2 * pi * r

print("Wybierz operacje:")
print("1.Dodawanie")
print("2.Odejmowanie")
print("3.Mnozenie")
print("4.Dzielenie")
print("5.Obliczanie pola koła")
print("6.Obliczanie obwodu koła")

wybor = input("Wybierz(1/2/3/4/5/6): \n")

if wybor == '1':
   liczba1 = int(input("Podaj pierwsza wartosc: "))
   liczba2 = int(input("Podaj pierwsza wartosc: "))
   print(liczba1,"+",liczba2,"=", dodawanie(liczba1,liczba2))

elif wybor == '2':
     liczba1 = int(input("Podaj pierwsza wartosc: "))
     liczba2 = int(input("Podaj pierwsza wartosc: "))
     print(liczba1,"-",liczba2,"=", odejmowanie(liczba1,liczba2))

elif wybor == '3':
     liczba1 = int(input("Podaj pierwsza wartosc: "))
     liczba2 = int(input("Podaj pierwsza wartosc: "))
     print(liczba1,"*",liczba2,"=", mnozenie(liczba1,liczba2))

elif wybor == '4':
     liczba1 = int(input("Podaj pierwsza wartosc: "))
     liczba2 = int(input("Podaj pierwsza wartosc: "))
     print(liczba1,"/",liczba2,"=", dzielenie(liczba1,liczba2))

elif wybor == '5':
     r = int(input("Podaj wartosc r: "))
     print(polekola(r))

elif wybor == '6':
     r = int(input("Podaj wartosc r: "))
     print(obwodkola(r))
else:
   print("Wprowadzono bledne dane!")

