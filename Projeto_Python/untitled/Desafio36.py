
casa = float(input('Qual o valor da casa que você que comprar?R$'))
salario = float(input('Qual o valor do seu salário?R$'))
anos = int(input('Em quantos anos você que pagar a casa?'))
prestacao = casa / (anos * 12 )
minimo = (salario * 30 / 100)
print('Para pagar uma casa de R${:.2f} em {} anos'.format(casa,anos))
print('A prestação sera de R${:.2f}'.format(prestacao))
if prestacao <= minimo:
    print('Imprestimo concedido')
else:
    print('Imprestimo negado')