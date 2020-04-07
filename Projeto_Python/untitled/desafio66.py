soma = 0
cont = 0
while True:
    n = int(input('Digite um numero(999 para finalizar): '))
    if n == 999:
        break
    cont += 1
    soma = soma + n
print(f'A soma dos {cont } numeros é {soma}')