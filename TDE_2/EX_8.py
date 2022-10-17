
num = [[],[]]

valor = 0

for c in range(0,10):

    valor = int(input(f"Digite o {c}o, valor: "))

    if valor % 2 == 0:

        num[0].append(valor)

    else:

        num[1].append(valor)

print(num[0])

print(num[1])

