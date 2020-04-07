numeros = []
while True:
    n = int(input('Digite um numero: '))
    numeros.append(n)
    r = str(input('Quer continuar? [S/N]').upper())
    if r == 'N':
        break
print(f'Foram digitados {len(numeros)} numeros.')
numeros.sort(reverse=True)
print(f'Os numeros digitados em ordem decrecente foram {numeros}')
if 5 in numeros:
    print('O numero 5 está na lista.')
else:
    print('O numero 5 não está na lista.')
