escolha = int(input('''
[1] Calcular Potência
[2] Calcular Corrente Elétrica
[3] Calcular Voltagem

[4] Calcular Resistência
[5] Calcular Corrente 
[6] Calcular Voltagem
[0] Sair

Sua escolha:
'''))
p = 0
ce = 0
v = 0
r = 0
ce1 = 0
v1 = 0
if escolha == 1:
    c = float(input("Informe a Corrente:(Em Amperes)"))
    v = float(input("Informe a Voltagem:(Em Volts)"))
    p = c * v
    print('A potencia maxima é de {:.0f} Watts'.format(p))
elif escolha == 2:
    p = float(input("Informe a Potencia:(Em Watts)"))
    v = float(input("Informe a Voltagem:(Em Volts)"))
    c = p / v
    print('A corrente é de {:.2f} Amperes'.format(c))
elif escolha == 3:
    p = float(input("Informe a Potencia:(Em Watts)"))
    c = float(input("Informe a Corrente:(Em Amperes)"))
    v = p / c
    print('A Voltagem é de {:.2f} Volts'.format(v))
elif escolha == 4:
    v1 = float(input("Informe a Voltagem:(Em Volts)"))
    ce1 = float(input("Informe a Corrente:(Em Amperes)"))
    r = v1 / ce1
    print('A resistência é de {:.2f} Ohms'.format(r))
elif escolha == 5:
    v1 = float(input("Informe a Voltagem:(Em Volts)"))
    r = float(input("Informe a Resistência:(Em Ohms)"))
    ce1 = v1 / r
    print('A corrente é de {:.3f} Amperes'.format(ce1))
elif escolha == 6:
    r = float(input("Informe a Resistência:(Em Ohms)"))
    ce1 = float(input("Informe a Corrente:(Em Amperes)"))
    v1 = r * ce1
    print('A Voltagem é de {:.2f} Volts'.format(v1))
else:
    print("Erro tente outro numero.")