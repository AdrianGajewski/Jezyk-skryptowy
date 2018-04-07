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
    try:
        poleKola = pi * r * r
        with open('results.txt', 'a') as f:
            f.write("Pole kola: \n ")
            f.write(str(pi) + " * " + str(r) + " * " + str(r) + " = " + ('%f' % poleKola))
            f.write("\n")
    finally:
        f.close()
        return r

def obwodkola(r):
    try:
        obwodKola = 2 * pi * r
        with open('results.txt', 'a') as f:
            f.write("Obwod kola: \n ")
            f.write(str(2) + " * " + str(pi) + " * " + str(r) + " = " + ('%f' % obwodKola))
            f.write("\n")
    finally:
        f.close()
        return r

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
   print(liczba1,"+",liczba2,"=", dodawanie(liczba1, liczba2))

elif wybor == '2':
     liczba1 = int(input("Podaj pierwsza wartosc: "))
     liczba2 = int(input("Podaj pierwsza wartosc: "))
     print(liczba1,"-",liczba2,"=", odejmowanie(liczba1, liczba2))

elif wybor == '3':
     liczba1 = int(input("Podaj pierwsza wartosc: "))
     liczba2 = int(input("Podaj pierwsza wartosc: "))
     print(liczba1,"*",liczba2,"=", mnozenie(liczba1, liczba2))

elif wybor == '4':
     liczba1 = int(input("Podaj pierwsza wartosc: "))
     liczba2 = int(input("Podaj pierwsza wartosc: "))
     print(liczba1,"/",liczba2,"=", dzielenie(liczba1, liczba2))

elif wybor == '5':
    r = int(input("Podaj wartosc r: "))
    polekola(r)
    print("Pole Kola wynosi: " +str(polekola(r)))

elif wybor == '6':
    r = int(input("Podaj wartosc r: "))
    obwodkola(r)
    print("Obwod kola wynosi: " + str(obwodkola(r)))
else:
   print("Wprowadzono bledne dane!")















