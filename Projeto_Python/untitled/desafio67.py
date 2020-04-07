
while True:
    tab = int(input("Quer ver a tabuada de qual valor? "))
    cont = 0
    if tab < 0:
        break
    while cont <= 10 :
        resul = (tab*cont)
        print(f'{tab} X {cont} = {resul}')
        cont += 1
