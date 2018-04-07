
def sumowanieLiczb(lista):
    print(sum(lista))

def listaZpliku(sumlist):
    plik = open(sumlist, "r")
    lista = []

    for line in plik:
        lista.append(int(line))

    return lista

sumowanieLiczb(listaZpliku("sumlist.txt"))
