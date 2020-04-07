num = int(input('Digite um numero inteiro qualquer?'))
print('''Escolha uma das bases da conversão:
[ 1 ] Converter em BINÁRIO
[ 2 ] Converter em OCTAl
[ 3 ] Converter em HEXADECIMAL''')
opcao = int(input('Sua opição: '))
if opcao == 1:
    print('{} convertido para BINARIO é igual a {}'.format(num,bin(num)[2:]))
elif opcao == 2:
    print('{} convertido para OCTAL é igual a {}'.format(num,oct(num)[2:]))
elif opcao == 3:
    print('{} convertido para HEXADECIMAL é igual a {}'.format(num,hex(num)[2:]))
else:
    print('Essa opção não existe!')