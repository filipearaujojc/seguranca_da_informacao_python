import random
import string

tamanho = int(input('Digite o tamanho da senha que você deseja: '))

chars = string.ascii_letters + string.digits + '!@#$%&*()-+=,.:;/?'

rnd = random.SystemRandom() 

print(''.join(rnd.choice(chars) for i in range(tamanho)))
