num = int(input('Digite um numero que você quer ver a tabuada:'))
for con in range(1, 11):
    print('{} X {:2} = {} '.format(num, con, num*con))