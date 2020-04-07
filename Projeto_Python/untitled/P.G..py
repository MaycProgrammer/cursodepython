primeiro = float(input('Digite o primeiro termo da P.G.:'))
razao = float(input('Digite a razão da P.G.:'))
termo  = primeiro
cont = 1
mais = 10
total = 0
while mais != 0:
    total = total + mais
    while cont <= total:
        print('{} -> '.format(termo), end='' )
        termo *= razao
        cont += 1
    print('Pausa')
    mais = float(input('Você deseja mostrar mais quantos termos:'))
print('Progressão finalizada com {} termos exibidos.'.format(total))
