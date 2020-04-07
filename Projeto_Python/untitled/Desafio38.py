n1 = int(input('Digite um Numero?'))
n2 = int(input('Digite outro numero?'))
if n1 < n2 :
    print('O numero {} é menor que {}.'.format(n1, n2))
elif n1 > n2:
    print('O numero {} é maior {}'.format(n1, n2))
else:
    print('Os numeros {} e {} são iguais.'.format(n1, n2))
