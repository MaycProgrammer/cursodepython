lista=[]
for cont in range(0,5):
    lista.append(int(input("Digite um valor: ")))
print(f'O maior valor Digitado foi {max(lista)}.')
print(f'O maior valor Digitado foi {min(lista)}.')
for c,v in enumerate(lista):
    print(f'O valor {c} foi encontrado na {v} posição.')
