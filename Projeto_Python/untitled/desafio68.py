import random
vitorias=0
while True:
    print(15*'=-')
    print('VAMOS JOGAR PAR OU ÍMPAR')
    print(15*'=-')
    jogador = int(input('Digite um valor: '))
    escolhajogador= str(input('Par ou Ímpar? [PAR/IMPAR] ').upper())
    computador = random.randint(0,10)
    escolhacomputador=''
    valor=jogador + computador
    vencedor=''
    if escolhajogador =='IMPAR':
        escolhacomputador ="PAR"
    elif escolhajogador == 'PAR':
        escolhacomputador = "IMPAR"
    if (valor%2)==0:
         vencedor='PAR'
    elif (valor%2)==1:
        vencedor = 'IMPAR'
    print(25*'-')
    print(f'Você jogou {jogador} e o computador {computador}. Total de {valor} DEU {vencedor}')
    print(25*'-')
    if escolhajogador == vencedor:
        print('Jogador VENCEU')
        print('Vamos jogar novamente...')
        vitorias += 1
        print(25 * '*-')
    elif escolhacomputador == vencedor:
        print('Computador VENCEU')
        print(f'GAME OVER! Você venceu {vitorias} vezes.')
        print(25 * '*-')
        break