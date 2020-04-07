numeros = []
par= []
impar= []
while True:
    n = int(input('Digite um numero: '))
    numeros.append(n)
    r = str(input('Quer continuar?[S/N] ').upper())
    while True:
        if n % 2 == 0:
            par.append(n)
            break
        else:
            impar.append(n)
            break
    if r == 'N':
        break
print(f'Todos os valores {numeros}')
print(f'Os numeros pares{par}')
print(f'Os numeros impares {impar}')