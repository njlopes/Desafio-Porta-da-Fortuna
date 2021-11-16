from random import *

jogando = True
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

while jogando == True:

    print("\nEscolha uma porta (1, 2 ou 3):")

    portaEscolhida = input()
    portaEscolhida = int(portaEscolhida)

    portaCerta = randint(1,3)


    print("A porta escolhida foi a", portaEscolhida)
    print("A porta certa é a", portaCerta)

    if portaEscolhida == portaCerta:
        print("Parabéns!")
        score += 1
    else:
        score = 0
        print("Que peninha!")

    if portaEscolhida != portaCerta:
        score = 0

    print("Sua pontuação é:", score)
    print("\nVocê quer jogar de novo? (s/n)")
    resposta = input().lower()

    if resposta == 'n' or resposta == 'não':
        jogando = False

print("Obrigado por jogar.")
print("Sua pontuação final é de", score)
