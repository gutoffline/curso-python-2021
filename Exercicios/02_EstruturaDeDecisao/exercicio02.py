"""
Faça um Programa que peça um valor e mostre na tela se o valor é positivo, negativo ou zero.
"""
valor = int(input("Informe um número: "))

if valor == 0:
    print("Valor 0")
elif valor > 0:
    print("Positivo")
else:
    print("Negativo")
