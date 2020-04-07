resp = 'S'
soma = 0
media = 0
maior = 0
menor = 0
cont = 0
while resp == 'S' :
    n = float(input('digite um numero: '))
    cont += 1
    soma = soma + n
    if cont == 1:
        maior = n
        menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    resp = str(input('Que digitar outro numero?[S/N] ')).upper()
media = (soma / n)
print('A media dos numeros foi de {} '.format(media))
print('O maior numero digitado foi {} '.format(maior))
print('O menor numero digitado foi {} '.format(menor))