import random
print("Bem vindo ao dUAMgeun, um RPG onde sua guilda deve chegar até a sala 9 para vencer o jogo.")
print("Para ganhar o jogo você deve ter menos de 7 interações.")
print(
    "Você está na sala: 1\n Escolha seu caminho:\n [1] - Caminho vermelho\n [2] - Caminho Preto")

sala = 1
i = 0
while sala < 9:
    caminho = int(input(''))
    i = i + 1
    if caminho == 1 and sala != 6:
        sala = sala + 1
        print(
            f"Você está na sala: {sala}\n Escolha seu caminho:\n [1] - Caminho vermelho\n [2] - Caminho Preto")
    elif caminho == 2 and sala != 8 or sala == 6:
        sala = sala + 2
        print(
            f"Você está na sala: {sala}\n Escolha seu caminho:\n [1] - Caminho vermelho\n [2] - Caminho Preto")
    else:
        sala = random.randint(1, 5)
        print('Você entrou em um portal desconhecido dominado por criaturas místicas que dominam o tempo-espaço e será teletransportado para uma sala desconhecida')
        print(
            f"Você está na sala: {sala}\n Escolha seu caminho:\n [1] - Caminho vermelho\n [2] - Caminho Preto")
if i < 7:
    print('\nParabens voce conseguiu comprir o desafio')
else:
    print(
        f'\nInfelizmente voce não compriu o desafio por usar {i} interações, \ntente novamente utilizando menos de 7 interações')

    
