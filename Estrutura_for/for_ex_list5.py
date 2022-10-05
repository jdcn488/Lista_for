
cont = 0

cont2 = 0

for l in range(1, 11):

    numero = int(input("Digite um número: "))

    if numero % 2 == 0:

        cont = cont + 1

    else:

        cont2 = cont2 + 1

print("Tem " + str(cont) + " numeros pares e tem "+str(cont2)+" numeros impares")

