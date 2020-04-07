expre = str(input('Digite uma expepressão: '))
pilha= []
for sím in expre:
    if sím == '(':
        pilha.append('(')
    elif sím == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressão é valida')
else:
    print('Sua expressão é invalida')
