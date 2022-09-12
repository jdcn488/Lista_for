from random import randint

from time import sleep

opcao = int(input("Digite um número [0] jogador x computador  [1] jogador x jogador [2] computador x computador :"))

if opcao == 0:

    pontosj = 0

    pontosc = 0

    itens = ("pedra", "papel", "tesoura")

    computador = randint(0, 2)

    print("Opções: [0] pedra [1] papel [2] tesoura")

    jogador = int(input("Digite um número: "))

    print("jo")
    sleep(1)

    print("ken")
    sleep(1)

    print("pô!!!!")
    sleep(1)

    print('-='*12)

    print("O computador escolheu {} " .format(itens[computador]))

    print("O voçê escolheu {} " .format(itens[jogador]))

    print('-='*12)

    if computador == 0: # compudador jogou pedra

        if jogador == 0:

            print("empate")

        elif jogador == 1:

            print("voçê venceu")

        elif jogador == 2:

            print("voçê perdeu")

        else:

            print("invalido")

    elif computador == 1: # compudador jogou papel

        if jogador == 0:

            print("voçê perdeu")

        elif jogador == 1:

            print("empate")

        elif jogador == 2:

            print("voçê venceu")

        else:

            print("invalido")

    elif computador == 2:# compudador jogou tesoura

        if jogador == 0:

            print("voçê venceu")

        elif jogador == 1:

            print("voçê perdeu")

        elif jogador == 2:

            print("empate")

        else:
            print("invalido")



elif opcao == 1:

    itens = ("pedra", "papel", "tesoura")

    print("jogador 1 Opções: [0] pedra [1] papel [2] tesoura")

    jogador = int(input("Digite um número jogador 1: "))

    print("jogador 2 Opções: [0] pedra [1] papel [2] tesoura")

    jogador2 = int(input("Digite um número jogador 2: "))

    print("jo")
    sleep(1)

    print("ken")
    sleep(1)

    print("pô!!!!")
    sleep(1)

    print('-=' * 12)

    print("O jogador 1 escolheu {} ".format(itens[jogador]))

    print("O jogador 2 escolheu {} ".format(itens[jogador2]))

    print('-=' * 12)

    if jogador2 == 0:   # jogador 2 jogou pedra

        if jogador == 0:

            print("empate")

        elif jogador == 1:

            print("jogador 1 venceu")

        elif jogador == 2:

            print("jogador 2 venceu")

        else:
            print("invalido")

    elif jogador2 == 1:  # jogador 2 jogou papel

        if jogador == 0:

            print("jogador 2 venceu")

        elif jogador == 1:

            print("empate")

        elif jogador == 2:

            print("jogador 1 venceu")

        else:
            print("invalido")

    elif jogador2 == 2:  # jogador 2 jogou tesoura

        if jogador == 0:

            print("jogador 1 venceu")

        elif jogador == 1:

            print("jogador 2 venceu")

        elif jogador == 2:

            print("empate")

        else:
            print("invalido")

elif opcao == 2:

    itens = ("pedra", "papel", "tesoura")

    computador = randint(0, 2)

    computador2 = randint(0, 2)

    print("jo")
    sleep(1)

    print("ken")
    sleep(1)

    print("pô!!!!")
    sleep(1)

    print('-=' * 12)

    print("O computador 1 escolheu {} ".format(itens[computador]))

    print("O computador 2 escolheu {} ".format(itens[computador2]))

    print('-=' * 12)

    if computador == 0:# compudador 1 jogou pedra

        if computador2 == 0:

            print("empate")

        elif computador2 == 1:

            print("computador 2 venceu")

        elif computador2 == 2:

            print("computador 1 venceu")

        else:
            print("invalido")

    elif computador == 1:  # compudador 1 jogou papel

        if computador2 == 0:

            print("computador 2 venceu")

        elif computador2 == 1:

            print("empate")

        elif computador2 == 2:

            print("computador 1 venceu")

        else:
            print("invalido")

    elif computador == 2:  # compudador 1 jogou tesoura

        if computador2 == 0:

            print("computador 1 venceu")

        elif computador2 == 1:

            print("computador 2 venceu")

        elif computador2 == 2:

            print("empate")

        else:
            print("invalido")

else:
    print("invalido")