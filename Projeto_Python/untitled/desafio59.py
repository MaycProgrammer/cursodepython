from time import sleep
escolha = 0
n1 = float(input('Digite um numero: '))
n2 = float(input('Digite outro numero: '))
while escolha != 5:
    escolha = int(input('''
    =-=-=-=-=-=-=-=-=-=-=-=-=
    [1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Novos numeros
    [5] Sair do programa.
    =-=-=-=-=-=-=-=-=-=-=-=-=
    ==>Sua escolha: '''))
    sleep(1)
    soma = n1 + n2
    multi = n1 * n2
    maior = 0
    if n1 > n2:
        maior = n1
    elif n2 > n1:
        maior = n2
    if escolha == 1:
        print('A soma dos numeros  {} + {} = {}'.format(n1, n2, soma))
    elif escolha == 2:
        print('A multiplicação de {} X {} = {}'.format(n1, n2, multi))
    elif escolha == 3:
        print('O maior numero entre {} e {} é {}'.format(n1, n2, maior))
    elif escolha == 4:
        n1 = int(input('Digite um numero:'))
        n2 = int(input('Digite outro numero:'))
    else:
        print('Opção invalida! ')
print('Finalizando...')
sleep(1)
print('Fim')