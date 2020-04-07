import emoji
import time
nome = 'jennifer'
print('Carregando')
time.sleep(0.5)
print('.',end='')
time.sleep(0.5)
print('.',end='')
time.sleep(0.5)
print('.')
resp = str(input('Faça sua pergunta:'))
print('pensando')
time.sleep(1)
print('...')
print(emoji.emojize('A esta é facil é Jennifer :heart:', use_aliases=True))
