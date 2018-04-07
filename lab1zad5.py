print("Prosty Kalkulator")

x = int(input("Podaj pierwszą liczbę:"))
y = int(input("Podaj drugą liczbę:"))
z = input("Wybierz operację(+,-,*,/,**)")

operators = {"+": x+y, "-": x-y, "*": x*y, "/": x/y, "**": x**y}

if z == "+":
    print(operators["+"])
elif z == "-":
    print(operators["-"])
elif z == "*":
    print(operators["*"])
elif z == "/":
    print(operators["/"])
elif z == "**":
    print(operators["**"])
else:
    print("BŁĄD!!!)")