print(20*'=')
print('  BANCO DO MAYCON ')
print(20*'=')
valor = int(input('Qual o valor a ser sacado:R$'))
total = valor
ced = 50
totalced = 0

while True:
    if total >= ced:
        total -= ced
        totalced +=1
    else:
        if totalced > 0:
            print(f'Total de {totalced} cedulas de R${ced} ')
        if ced ==50:
            ced=20
        elif ced ==20:
            ced=10
        elif ced ==10:
            ced=1
        totalced = 0
        if total == 0:
            break
print(20*'=')
print('Volte sempre')