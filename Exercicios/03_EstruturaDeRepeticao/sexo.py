sexo = ''
while sexo.upper() != 'F' and sexo.upper() != 'M':
    sexo = input("Informe o sexo F ou M: ")
    if sexo.upper() != 'F' and sexo.upper() != 'M':
        print("Valor inválido")