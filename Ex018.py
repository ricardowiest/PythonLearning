import math
ang=float(input('Digite o ângulo: '))
#math.radian transforma o número em radianos, senão ficará com valor errado.
seno=math.sin(math.radians(ang))
cos=math.cos(math.radians(ang))
tan=math.tan(math.radians(ang))
print('Este ângulo possui seno de {:.2f}, cosseno {:.2f} e tangente {:.2f}.'.format(seno,cos,tan))
