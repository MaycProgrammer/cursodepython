totalgasto = 0
prok = 0
maisbaratonome = ''
maisbaratopreco = 0
while True:
    nome = str(input('Digite o nome do produto: '))
    preco= float(input('Digite o preço: R$  '))
    totalgasto = totalgasto + preco
    maisbaratonome=nome
    maisbaratopreco=preco
    if preco > 1000:
        prok += 1
    if preco < maisbaratopreco:
        maisbaratonome = nome
        maisbaratopreco = preco
    escolha = str(input('Quer continuar? [S/N]').upper())
    if escolha == 'N':
        print(20*'=')
        print(f'O total da compra foi R${totalgasto:.2f}')
        print(f'Temos {prok} produtos custando mais de R$1000.00')
        print(f'O produto mais barato foi {maisbaratonome} que custa R${maisbaratopreco:.2f}')
        print(20 * '=')
        break