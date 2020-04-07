nomepeso = []
pessoas = []
while True:
    nomepeso.append(str(input("Nome: ")))
    nomepeso.append(int(input("Peso: ")))
    pessoas.append(nomepeso[:])
    r = str(input('Quer continuar?[S/N] ').upper())
    if r == 'N':
        break

print(f'Foram codastradas {len(pessoas)} pessoas.')