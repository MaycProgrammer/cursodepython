r1 = float(input('Primeiro seguimento'))
r2 = float(input('Segundo Seguimento'))
r3 = float(input('Terceiro Seguimento'))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    if r1 == r2  == r3:
        print('Ele é um triangulo Equilatero')
    elif r1 != r2 != r3 != r1:
        print('Ele é um triangulo Escaleno')
    else:
        print('Ele é um triangulo Isoceles')
else:
    print('Erro')