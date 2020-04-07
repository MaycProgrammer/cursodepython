print('=-=-=-=-=-=-=-=-=-=-=-=-')
print('        Natação         ')
print('=-=-=-=-=-=-=-=-=-=-=-=-')
ano = int(input('Qual o seu ano de Nascimento?'))
idade = 2018 - ano
if idade <= 9:
    print('Você esta na categoria MIRIM')
elif idade > 9 and idade <= 14:
    print('Você esta na categoria INFANTIL')
elif idade > 14 and idade <= 19:
    print('Você esta na categoria JUNIOR')
elif idade > 19 and idade <= 20:
    print('Você esta na categoria SÊNIOR')
elif idade > 20:
    print('Você esta na categoria MASTER')