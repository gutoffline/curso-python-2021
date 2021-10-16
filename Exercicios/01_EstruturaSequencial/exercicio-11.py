import math

numInt1 = int(input('Informe um numero inteiro: '))
numInt2 = int(input('Informe outro numero inteiro: '))
numReal = float(input('Informe um numero real: '))

dobro =  (2 * numInt1) / (numInt2 / 2.0)
triplo = (3 * numInt1) + numReal
elevado = math.pow(numReal, 3)
print ('O dobro do primeiro vezes a metade do segundo é', dobro)

print('A soma do triplo do primeiro com o terceiro é', triplo)
print('O terceiro elevado ao cubo é', elevado)
