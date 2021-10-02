"""
if teste lógico :
    o código deste bloco é executado se o teste for verdadeiro
    o teste lógico só retorna veradeiro ou falso

quando só o if, se o teste for falso, ele pula a execução do if

o operador not inverte o resultado do teste, se deu verdadeiro, ele muda para falso, se deu falso ele muda para verdadeiro

if imposto == '' é igual a if not imposto
"""

salario = float(input("Informe o salário: "))
imposto = input("Informe o imposto em % (Ex: 27.5): ")

if not imposto:
    imposto = 27.5
else:
    imposto = float(imposto)

salario_calculado = salario - (salario * (imposto * 0.01))

print("Valor salário: ", salario_calculado)

"""
imposto < 10 --> medio
imposto < 27.5 --> alto
imposto >= 27.5 --> muito alto
"""
if imposto < 10:
    print("Imposto médio")
elif imposto >= 10 and imposto <= 27:
    print("Imposto alto")
elif imposto > 27 and imposto < 100:
    print("Imposto muito alto")
else:
    print("Imposto inválido")