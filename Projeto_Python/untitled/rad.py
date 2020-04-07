num = int(input('Informe em graus a posição no arco:'))
resu = 0
rest = 0
if num > 360:
    resu = num // 360
    rest = num % 360
print(resu)
print(rest)
