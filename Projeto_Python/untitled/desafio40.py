nota1 = float(input('Informe sua primeira nota:'))
nota2 = float(input('Informe sua segunda nota:'))
media = (nota1 + nota2) / 2
if media < 5.0 :
    print('Você esta Reprovado.')
elif media >= 5.00 and media < 6.9 :
    print('Você esta de recuperação')
elif media >= 7.0 :
    print('Você esta aprovado.')