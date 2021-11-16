from random import *

jogando = True


print('''
Vinte e um!
==========
Tente fazer exatamente 21 pontos!
    ''')

while jogando == True:

    pontuação = randint(1,10)
    print("Seu próximo número é:", pontuação)

    print("\nVocê quer jogar de novo?(s/n)")
    resposta = input().lower

    if resposta == "n":
        jogando = false
    elif resposta == "s":
        pontuação = pontuação + pontuação

    if pontuação < 21:
        print("Sua pontuação atual é:", pontuação)

    elif pontuação == 21:
        print("Você venceu!")

    if pontuação > 21:
        print("Que pena.")

    

    

    


   

 
