from random import randint
from time import sleep
print('====Vamos jogar====')
sleep(1)
computador = randint(0, 10)
print('Pensei em um numero de (0, 10) tente adivinhar? ')
jogador = int(input('Digite seu numero: '))
tentativa = 1
while jogador  != computador:
    jogador = int(input('Você errou. Tente novamente :'))
    tentativa += 1
print('\033[0;32mParabens você acertou com {} tentativas.\033[m'.format(tentativa))