import math
m = float(input('Informe a massa em KG: '))
g = float(input('Informe a aceleração da gravidade: '))
h = float(input('Informe a altura: '))
v = (m / 2)
v2 = (m * g * h)
v3 = (v2 / v)
r = v3 ** (1/2)
print(f'A resposta final é {r:.2f}')