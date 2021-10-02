"""
Faça um Programa que verifique se uma letra digitada é vogal ou consoante.
"""
letra = input("Informe uma letra: ")

letra = letra.upper()

if "AEIOU".find(letra) >= 0:
    print("Vogal")
else:
    print("Consoante")