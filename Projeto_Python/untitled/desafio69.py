while True:
    print(25*"-")
    print("   CADASTRE UMA PESSOA  ")
    print(25*"-")
    idade = int(input("Idade: "))
    sexo = str(input("Sexo: [M/F]").upper())
    if (sexo == 'M' or sexo == 'F'):
        sexo = str(input("Sexo: [M/F]").upper())
    print(25 * "-")
    totalmasc = 0
    totalpes18=0
    totalmul20=0
    if (idade > 18 ):
        totalpes18 += 1
    elif (sexo =="M"):
        totalmasc += 1
    elif (sexo=='F' and idade <20 ):
        totalmul20 += 1
    continuar = str(input("Quer continuar: [S/N]").upper())
    if (continuar != 'S' or continuar != 'N'):
        continuar = str(input("Quer continuar: [S/N]").upper())
    if continuar == 'N':
        print(25 * "=")
        print('FIM DO PROGRAMA')
        print(25 * "=")
        print(f'Total de pessoas com mais de 18 anos: {totalpes18}')
        print(f'Ao todo temos {totalmasc} homens cadastrados')
        print(f'E temos {totalmul20} mulheres com menos de 20 anos.')
        break
