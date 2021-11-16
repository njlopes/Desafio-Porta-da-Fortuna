from random import *
score = 0
print('''
Porta da Fortuna!
==========

Existe um super prêmio atrás de uma destas 3 portas!
Adivinhe qual é a porta certa para ganhar o prêmio!

      _____     _____     _____
     |     |   |     |   |     |
     | [1] |   | [2] |   | [3] |
     |     |   |     |   |     |
     |_____|   |_____|   |_____|
    ''')

for attempt in range(3):

    print("\nEscolha uma porta (1, 2 ou 3):")
          
    portaEscolhida = input()
    portaEscolhida = int(portaEscolhida)

    portaCerta = randint(1,3)


    print("A porta escolhida foi a", portaEscolhida)
    print("A porta certa é a", portaCerta)

    if portaEscolhida == portaCerta:
        score += 1
        print("Parabéns!")
    else:
        score += 0
        print("Que peninha!")

if score == 3:
    print(f'score = {score}')
    print('Muito bem! Você chegou a pontuação máxima!')
elif score == 2:
    print(f'score = {score}')
    print('Quase lá!')
elif score == 1:
    print(f'score = {score}')
    print('Tente novamente')
else:
    print('Você errou todas as portas.')

