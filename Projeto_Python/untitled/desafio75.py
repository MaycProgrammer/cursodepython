numeros = (int(input("Digite um numero: ")), int(input("Digite outro numero: ")),
           int(input("Digite mais um numero: ")), int(input("Digite o ultimo numero: ")))
print(f"os valores digitados foram {numeros}")
print(f"O numero 9 apareceu {numeros.count(9)} Vezes")
if 3 in numeros:
    print(f"O numero 3 está na {numeros.index(3)+1}° posição.")
else:
    print(f"O numero 3 não foi encontrado em nenhuma  posição.")
print(f"Os valores pares digitados foram ", end=" ")
for n in numeros:
    if n % 2 ==0:
        print(n, end=' ')
