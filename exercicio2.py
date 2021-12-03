import math
try:
    n = float(input('Digite um número:'))
    print("Número ao quadrado {0}".format(n**2))
    print("Número ao cubo {0}".format(n**3))
    print("Raiz quadrado do Número {0}".format(math.sqrt(n)))
except ValueError:
    print("Not a number")
