sexo = str(input('Digite outra vez [M/F] :')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Dados inválidos. Po favor, informe seu sexo: ')).strip().upper()[0]
print('Dados cadastrados com sucesso.')