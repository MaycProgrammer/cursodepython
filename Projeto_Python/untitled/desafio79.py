numeros = []
while True:
    n=(int(input("Digite um valor: ")))
    if n not in numeros:
        numeros.append(n)
        print('Valor adicionado com sucesso.')
    else:
        print("Valor duplicado! Não vou adicionar...")
    r = str(input("Quer continuar? [S/N]").upper())
    if r =="N":
        break
numeros.sort()
print(f"Você digitou os valores {numeros}.")
print(f"O maoir valor digitado foi {max(numeros)}.")
print(f"O menor valor digitado foi {min(numeros)}.")