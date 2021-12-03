try:
    n = int(input('Digite um número:'))
    multiplicador = 1
    while multiplicador < 11 :
        print("{0} x {1} = {2}".format(n, multiplicador, n*multiplicador))
        multiplicador = multiplicador+1
except ValueError:
    print("Not a number")
