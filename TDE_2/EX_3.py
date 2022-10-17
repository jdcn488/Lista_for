
vetor = int(input("Digite um tamanho para o vetor: "))

vetores = [0] * vetor

cont = 0

for j in range(vetor):

    vetores[j] = int(input("%do. número de %d:"%((j+1),vetor)))

print(vetores)

for a in vetores:

    if a > 5:

        cont = cont +1

print(cont)

for b in vetores:

    if b % 2 == 0:

        vetores.append(vetor)

    else:

        vetores.append(vetor)


print(sum(vetores))

