
cont = 0

cont2 = 0

for l in range(1, 11):

    numero = int(input("Digite um número: "))

    if numero >= 10 and numero <= 20:

        cont = cont + 1

    else:

        cont2 = cont2 + 1

print("Tem " + str(cont) + " números no intervalo de (10,20) e tem "+str(cont2)+" números fora do intervalo")
