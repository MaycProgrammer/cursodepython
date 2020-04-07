matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
spar= 0
maior= 0
scol=0
for l in range(0, 3):
    for c in range(0, 3):
        matrix[l][c] = int(input(f'Digite um valor para [{l} , {c}]: '))
print(30*'-=')
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matrix[l][c]:^5}]', end='')
        if matrix[l][c] % 2 == 0:
            spar += matrix[l][c]
    print()
print(30*'-=')
print(f'A soma dos numeros pares é {spar}')
for l in range(0,3):
    scol += matrix[l][2]
print(f'A soma dos valores da terceira coluna é {scol}')
for c in range(0,3):
    if c == 0:
        maior = matrix[1][c]
    elif matrix[1][c] > maior:
        maior = matrix[1][c]
print(f'O maior valor da segunda linha é {maior}')
