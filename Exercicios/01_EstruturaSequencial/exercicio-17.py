"""
17. Faça um Programa para uma loja de tintas.
O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam RS 25,00.
Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
comprar apenas latas de 18 litros;
comprar apenas galões de 3,6 litros;
misturar latas e galões, de forma que o desperdício de tinta seja menor.

Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.
"""
import math

print("PROGRAMA LOJA DE TINTA")
tamanho = float(input("Qual o tamanho, em metros quadrados da área a ser pintada? "))
litros = (tamanho/6) * 1.1
latas = math.ceil(litros / 18)
galoes = math.ceil(litros / 3.6)

mix_latas = int(litros/18)
latas_faltantes = litros/18 - mix_latas
litros_faltantes = latas_faltantes * 18
mix_galoes = math.ceil(litros_faltantes / 3.6)

preco_latas = latas * 80
preco_galoes = galoes * 25
preco_mix = mix_latas * 80 + mix_galoes * 25

print(latas , "latas x 80,00 =" , preco_latas)
print("OU")
print(galoes , "galões x 25 =" , preco_galoes)
print("OU")
print(mix_latas , "latas +" , mix_galoes , "galões =", preco_mix)
