primeiro = int(input('Digite o primeiro termo da P.A.: '))
razao = int(input('Digite a razão:'))
termo = primeiro
cont = 1
while cont <= 10:
    print('{} -> '.format(termo), end='')
    termo += razao
    cont += 1
print('Fim')