"""
Faça um Programa que leia três números e mostre o maior deles.
"""
numero_1 = int(input("Informe o número 1: "))
numero_2 = int(input("Informe o número 2: "))
numero_3 = int(input("Informe o número 3: "))

if numero_1 > numero_2 and numero_1 > numero_3:
    print("Número 1 é o maior")
elif numero_2 > numero_1 and numero_2 > numero_3:
    print("Número 2 é o maior")
elif numero_3 > numero_1 and numero_3 > numero_2:
    print("Número 3 é o maior")
else:
    print("Números são iguais")