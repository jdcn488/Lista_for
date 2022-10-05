
loop = 0

num_idade = 4

for l in range(1, 5):

    idade = int(input("Digite uma idade: "))

    loop += idade

    media = (loop)/num_idade

print("A media das idades é: "+ str(media))