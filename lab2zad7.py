import math

def rownanieKwadratowe(a, b, c):
    if a == 0 & b == 0:
        print("Podaj poprawne dane")
    else:
        delta = b * b - 4 * a * c
        if delta < 0:
            try:
                with open('results.txt', 'a') as f:
                    f.write("Rownanie nie ma rozwiazan w dziedzinie liczb rzeczywistych \n ")

            finally:
                f.close()

        elif delta == 0:
            try:
                x = (-b + math.sqrt(b * b - 4 * a * c)) / 2 * a
                with open('results.txt', 'a') as f:
                    f.write("Rownanie ma jedno rozwiazanie w dziedzinie liczb rzeczywistych: \n ")
                    f.write(str(x))
                    f.write("\n")
            finally:
                f.close()
                return x

        elif delta > 0:
            try:
                x1 = (-b+math.sqrt((b*b)-(4*(a*c))))/(2*a)
                x2 = (-b-math.sqrt((b*b)-(4*(a*c))))/(2*a)
                with open('results.txt', 'a') as f:
                    f.write("Rownanie ma dwa rozwiazania w dziedzinie liczb rzeczywistych: \n ")
                    f.write(str(x1) + " lub " + str(x2))
                    f.write("\n")
            finally:
                f.close()
                return x1, x2

a = int(input("Podaj a: \n"))
b = int(input("Podaj b: \n"))
c = int(input("Podaj c: \n"))

rownanieKwadratowe(a, b ,c)


