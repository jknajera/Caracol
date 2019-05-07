import math

def suma(lista):
    if lista == []:
        return 0
    return lista[0] + suma(lista[1:])
def opMa2Vec():
    x = open('matriz.txt','r')
    mensaje = x.read()
    a = mensaje.split()
    return a
def printMatrizGusano(a):
    tam = int(len(a))
    if a != []:
        for i in range (int(math.sqrt(len(a)))):
            print a[i]
        a = a[(int(math.sqrt(len(a)))): len(a)]
        """print a"""
    if a != []:
        for i in range (1, int(math.sqrt(tam))):
            print(a[int(i*math.sqrt(tam))-1])
        for i in range (1, int(math.sqrt(tam))):
            a.pop(int(i*(math.sqrt(tam)-1)))
        """print a"""
    if a != []:
        for i in range (1, int(math.sqrt(tam))):
            print a[len(a)-1]
            a.pop()
        """print a"""
    if a != []:
        for i in range (int((math.sqrt(tam)-1))-2, -1,-1):
            print(a[int(i*int(math.sqrt(tam)-1))])
            a.pop(int(i*int(math.sqrt(tam)-1)))
        """print a"""
    if a != []:
        printMatrizGusano(a)
    else:
        return 0
a = opMa2Vec()
printMatrizGusano(a)

