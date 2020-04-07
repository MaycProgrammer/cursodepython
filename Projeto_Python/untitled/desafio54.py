from datetime import date
atual = date.today().year
maior = 0
menor = 0
for pess in range(1, 8):
    nasc = int(input('Qual a data de nascimento da {}° pessoa:'.format(pess)))
    idade = atual - nasc
    if idade >= 18:
        maior += 1
    else:
        menor += 1
print('A {} pessoas maiores de idade.' .format(maior))
print('A {} pessoas menor de idade.' .format(menor))