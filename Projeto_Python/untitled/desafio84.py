temp= []
princ = []
maior = 0
menor = 0
while True:
    temp.append(str(input("Nome: ")))
    temp.append(int(input("Peso: ")))
    if len(princ) == 0:
        maior = menor = temp[1]
    else:
        if temp[1] > maior:
            maior = temp[1]
        if temp[1] < menor:
            menor = temp[1]
    princ.append(temp[:])
    temp.clear()
    r = str(input('Quer continuar?[S/N] ').upper())
    if r == 'N':
        break
print(f'Foram codastradas {len(princ)} pessoas.')
print(f'O maior peso foi de {maior:.2f}Kg. Peso de ', end='')
for p in princ:
    if p[1] == maior:
        print(f'[{p[0]}]', end='')
print()
print(f'O menor peso foi de {menor:.2f}Kg.Peso de ', end='')
for p in princ:
    if p[1] == menor:
        print(f'[{p[0]}]', end='')
print()