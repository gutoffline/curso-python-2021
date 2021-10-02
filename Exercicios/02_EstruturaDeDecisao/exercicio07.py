"""
Faça um Programa que leia três números e mostre o maior e o menor deles.
"""

numero_1 = int(input("Informe o primeiro número: "))
numero_2 = int(input("Informe o segundo número: "))
numero_3 = int(input("Informe o terceiro número: "))

if numero_1 > numero_2 and numero_1 > numero_3:
        print("O primeiro número é o maior: ", numero_1)
elif numero_2 > numero_1 and numero_2 > numero_3:
        print("O segundo número é o maior: ", numero_2)
elif numero_3 > numero_1 and numero_3 > numero_2:
        print("O terceiro número é o maior: ", numero_3)