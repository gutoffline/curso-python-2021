salario = 0
while salario <= 0:
    salario = input("Informe o salário: ")
    if salario.isdigit() == False:
        salario = 0
        print("Você digitou um valor inválido.")
    elif int(salario) <= 0:
        salario = int(salario)
        print("Você digitou um valor inválido.")
    else:
        salario = int(salario)