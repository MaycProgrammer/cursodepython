numeros = [[], [], []]
for cont in range(0,7):
    n = int(input(f'Digite o {cont + 1}° valor: '))
    if n%2 == 0:
        numeros[1].append(n)
    else:
        numeros[2].append(n)
    numeros.append(n)
    cont =+ 1
numeros[1].sort()
numeros[2].sort()

print(f'Os valores pares digitados foram {numeros[1]}.')
print(f'Os valores impares digitados foram {numeros[2]}.')