"""
Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto, mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os descontos. O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
Desconto do IR:
Salário Bruto até 900 (inclusive) - isento
Salário Bruto até 1500 (inclusive) - desconto de 5%
Salário Bruto até 2500 (inclusive) - desconto de 10%
Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, dispostas conforme o exemplo abaixo. No exemplo o valor da hora é 5 e a quantidade de hora é 220.
        Salário Bruto: (5 * 220)        : R$ 1100,00
        (-) IR (5%)                     : R$   55,00
        (-) INSS ( 10%)                 : R$  110,00
        FGTS (11%)                      : R$  121,00
        Total de descontos              : R$  165,00
        Salário Liquido                 : R$  935,00
"""
horas = int(input("Informe as horas trabalhadas: "))
valor_hora = float(input("Informe o valor por hora: R$"))
salario_bruto = horas * valor_hora
sindicato = 0.03
fgts = 0.11
imposto_renda = 0

if salario_bruto <= 900:
    imposto_renda = 0
elif salario_bruto <= 1500:
    imposto_renda = 0.05
elif salario_bruto <= 2500:
    imposto_renda = 0.10
else:
    imposto_renda = 0.20

valor_sindicato = salario_bruto * sindicato
valor_fgts = salario_bruto * fgts
valor_imposto_renda = salario_bruto * imposto_renda
salario_liquido = salario_bruto - valor_sindicato - valor_imposto_renda
total_descontos = valor_sindicato + valor_imposto_renda
print(""" 
Salário Bruto: ({0} * {1})\t\t\t: R$ {2}
(-) IR ({3:.0%})\t\t\t\t\t\t\t: R$ {4}
(-) INSS ({5:.0%})\t\t\t\t\t\t: R$ {6}
FGTS ({7:.0%})\t\t\t\t\t\t\t: R$ {8}
Total de descontos\t\t\t\t\t: R$ {9}
Salário Liquido\t\t\t\t\t\t: R$ {10:.2f}
""".format(horas, valor_hora, salario_bruto, imposto_renda, valor_imposto_renda, sindicato, valor_sindicato, fgts, valor_fgts, total_descontos, salario_liquido))
