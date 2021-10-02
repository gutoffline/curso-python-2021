"""
Faça um Programa que peça dois números e imprima o maior deles.
"""

numero_1 = int(input("Informe o primeiro número: "))
numero_2 = int(input("Informe o segundo número: "))

if numero_1 > numero_2:
    print("O maior número é o primeiro: ", numero_1)
else:
    if numero_1 == numero_2:
        print("Os números são iguais")
    else:
        print("O maior número é o segundo: ", numero_2)
