import random

print("Bem vindo ao dUAMgeun, um RPG onde sua guilda deve chegar até a sala 9 para vencer o jogo")
print(
    "Você está na sala: 1\n Escolha seu caminho:\n [1] - Caminho vermelho\n [2] - Caminho Preto")

sala = 1
i = 0
while sala < 9:
    while sala < 6 :
        caminho = int(input(''))
        i = i + 1
        if caminho == 1:
            sala = sala + 1
            print(
                f"Você está na sala: {sala}\n Escolha seu caminho:\n [1] - Caminho vermelho\n [2] - Caminho Preto")
        elif caminho == 2:
            sala = sala + 2
            print(
                f"Você está na sala: {sala}\n Escolha seu caminho:\n [1] - Caminho vermelho\n [2] - Caminho Preto")
    while sala == 6:
        sala = sala + 2
        print(f"Você esta na sala: {sala} \n Escolha seu caminho:\n [1] - Caminho vermelho\n [2] - Caminho Preto")
    while sala == 7 :
        caminho = int(input(''))
        i = i + 1
        if caminho == 1:
           sala = sala + 1
           print(
               f"Você está na sala: {sala}\n Escolha seu caminho:\n [1] - Caminho vermelho\n [2] Caminho Preto")
        else:
            print('Parabéns você ganhou o jogo')
    while sala == 8 :
        caminho = int(input(''))
        
        i = i + 1
        if caminho == 2:
            print('Você entrou em um portal desconhecido dominado por criaturas místicas que dominam o tempo-espaço e será teletransportado para uma sala desconhecida')
            sala = random.randint(1, 5)
            print(f"Você está na sala: {sala}\n Escolha seu caminho:\n [1] - Caminho vermelho\n [2] - Caminho Preto")
        elif caminho == 1:
             print(' Parabéns você ganhou o jogo')   
if i > 7 :
    print('\nParabens voce conseguiu comprir o desafio')
else:
    print(f'\nInfelizmente voce não compriu o desafio por usar {i} interações, \ntente novamente utilizando menos de 7 interações')
