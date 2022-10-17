
import random

vetor1 = [0] * 50

for j in range (50):
    vetor1[j] = random.randint(0, 20)

soma_vetores = sum(vetor1)

print(vetor1)

print("a:A soma dos vetores é: ",soma_vetores)

cont = 0

for vetor in vetor1:

    if (vetor == 9):

        cont = cont + 1

print("b: O número 9 aparece: ",cont)

menor = min(vetor1)

print("c:O menor valor é: ",menor)

maior = max(vetor1)

print("d:O maior valor é: ",maior)
