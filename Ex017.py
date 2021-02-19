#import math
from math import hypot
co=float(input('Digite o valor do cateto oposto: '))
ca=float(input('Digite o valor do cateto adjacente: '))
hip=hypot(co,ca)
print('A hipotenusa é {:.2f}.'.format(hip))
