from string import ascii_letters, digits, punctuation
from random import SystemRandom
print(''.join([SystemRandom().choice("{}{}{}".format(ascii_letters, digits, punctuation)) for i in range(50)]))
