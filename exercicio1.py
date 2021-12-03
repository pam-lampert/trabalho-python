try:
    n = int(input('Digite um número:'))
    print("Número anterior {0} e número posterior {1}".format(n-1, n+1))
except ValueError:
    print("Not a number")
