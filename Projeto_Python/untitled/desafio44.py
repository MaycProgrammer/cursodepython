preco = float(input('Qual o preço do produto?'))
print("""
Forma de pagamento: 
[1] Á vista Dinheiro/Chequer.
[2] Á vista no Cartão.
[3] 2x no Catão.
[4] 3x ou mais.""")
fdp = int(input('Sua escolha:'))
if fdp == 1:
    desc = preco * 0.9
    print('Você ganhou um desconto de 10% no produto R${:.2f}'.format(desc))
elif fdp == 2:
    desc = preco * 0.95
    print('Você ganhou um desconto de 5% R${:.2f}'.format(desc))
elif fdp == 3:
    par = preco / 2
    print('Você tera que pagar duas parcelas de R${:.2f}'.format(par))
elif fdp == 4:
    npar = int(input('Informe o numero de parcelas:'))
    jur = preco * 1.2
    vpar = jur / npar
    print('Foi acresentado 20% de JUROS, você vai pagar {} parcelas de R${}'.format(npar, vpar))
else:
    print('Erro Tente Novamente.')
