n = 0
cont = 0
soma = 0
while n != 999:
   n = int(input('Digite um numero: '))
   if n !=999:
       cont += 1
       soma = soma + n
print('Fim')
print('Foram digitados {} numeros.'.format(cont))
print('A soma dos numeros foi {} . '.format(soma))
