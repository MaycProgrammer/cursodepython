dn = int(input('Informe a sua data de nascimento:'))
idade = 2018 - dn
if idade < 18 :
    tempo1 = 18 - idade
    print('Você deve se alistar daqui {}.'.format(tempo1))
elif idade == 18 :
    print('Você deve ser alistar esse ano.')
elif idade > 18 :
    tempo2 = idade - 18
    print('Você ja passou {} do tempo de se alistar.'.format(tempo2))
