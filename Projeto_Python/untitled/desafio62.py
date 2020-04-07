primeiro = int(input('Digite o primeiro termo da P.A.: '))
razao = int(input('Digite a razão:'))
termo = primeiro
cont = 1
mais = 10
total = 0
while mais != 0:
    total = total + mais
    while cont <= total:
        print('{} -> '.format(termo), end='')
        termo += razao
        cont += 1
    print('PAUSA')
    mais = int(input('Você quer mostrar mais quantos termos:'))
print('Progreção finalizada com {} termos exibidos.'.format(total))