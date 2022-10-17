

numeros = []

cont = 0

while cont < 20:

    n = int(input("digite um valor:"))

    if n not in numeros:

        numeros.append(n)

        cont = cont + 1

    else:

        print("valor já inserido")

print(numeros)