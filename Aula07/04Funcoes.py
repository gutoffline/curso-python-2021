def mensagem(nome):
    print("Boa tarde", nome)
    print("Estamos quase terminando a aula de hoje.")

def conta(num1, num2=0):
    return num1*num2

def calculo_inss(salario):
    valor = 0
    if salario > 3000:
        valor = salario * 0.15
    else:
        valor = salario * 0.1

    return valor


salario_bruto = 4000
valor_inss = calculo_inss(salario_bruto)
valor_ir = calculo_ir(salario_bruto)
valor_convenio = calculo_convenio(salario_bruto)
salario_liquido = salario_bruto - (valor_convenio + valor_ir + valor_inss)





nome = "Guto"
mensagem(nome)
resultado = conta(13,2)
print(resultado)