
lista = []

for j in range(0,6):

    n = int(input("digite um valor:"))

    if j != 0:

        pos = 0

        while pos < len(lista):

            if n <= lista[pos]:

                lista.sort(reverse=True)

                break

            pos = pos + 1

    else:

        lista.append(n)

print(lista)
