import time
import random
print('=-=-=-=-=-=-=-=')
print('    JOKENPO    ')
print('=-=-=-=-=-=-=-=')
print("""Pense na sua opção:
[0] PEDRA
[1] PAPEL
[2] TESOURA """)
jogador = int(input('Sua escolha:'))
print('O computador esta pensando...')
computador = random.randint(0,2)
print('JO...')
time.sleep(1)
print('KEN...')
time.sleep(1)
print('PO.')
print(computador)
if computador == 0:
    if computador == 0 and jogador == 0:
        print('EMPATE')
    elif computador == 0 and jogador == 1:
        print('Jogador VENCE')
    elif computador == 0 and jogador == 2:
        print('Computador VENCE')
elif computador == 1:
    if computador == 1 and jogador == 0:
        print('Computador VENCE')
    elif computador == 1 and jogador == 1:
        print('EMPATE')
    elif computador == 1 and jogador == 2:
        print('Jogador VENCE')
elif computador == 2:
    if computador ==2 and jogador == 0:
        print('Jogador VENCE')
    elif computador == 2 and jogador == 1:
        print('Computador VENCE')
    elif computador == 2 and jogador == 2:
        print('EMPATE')
else:
    print('Opção invalida tente novamente.')