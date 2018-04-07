
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

print("Wybierz operacje:")
print("1.Dodawanie")
print("2.Odejmowanie")
print("3.Mnozenie")
print("4.Dzielenie")

wybor = input("Wybierz(1/2/3/4): \n")

liczba1 = int(input("Podaj pierwsza wartosc: "))
liczba2 = int(input("Podaj pierwsza wartosc: "))

if wybor == '1':
   print(liczba1,"+",liczba2,"=", dodawanie(liczba1,liczba2))

elif wybor == '2':
   print(liczba1,"-",liczba2,"=", odejmowanie(liczba1,liczba2))

elif wybor == '3':
   print(liczba1,"*",liczba2,"=", mnozenie(liczba1,liczba2))

elif wybor == '4':
   print(liczba1,"/",liczba2,"=", dzielenie(liczba1,liczba2))
else:
   print("Wprowadzono bledne dane!")

