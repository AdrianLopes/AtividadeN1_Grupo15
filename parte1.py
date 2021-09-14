import random
print("Bem vindo ao dUAMgeun, um RPG onde sua guilda deve chegar até a sala 9 para vencer o jogo")
print("Você está na sala: 1\n Escolha seu caminho:\n [1] - Caminho vermelho\n [2] - Caminho Preto")

#x = random.randint(1,5)
#print(f'{x}')

sala = 1
i = 1

while sala < 9:
    caminho = int(input(''))
    i = i + 1
    if caminho == 1:
        sala = sala + 1
        print(f"Você está na sala: {sala}\n Escolha seu caminho:\n [1] - Caminho vermelho\n [2] - Caminho Preto")
    elif caminho == 2:
        sala = sala + 2
        print(f"Você está na sala: {sala}\n Escolha seu caminho:\n [1] - Caminho vermelho\n [2] - Caminho Preto")
    else:
        print("Caminho inválido")
if i <= 7:
    print('\nParabens voce conseguiu comprir o desafio')
else:
    print(f'\nInfelizmente voce não compriu o desafio por usar {i} interações, \ntente novamente utilizando menos de 7 interações')
    
