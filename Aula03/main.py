# import this

#operadores : + - / *
print(2 ** 4) # potência
print(10/3)
print(10 % 3)
print(10//3)

#help()
print(type(10))
print(type(10.0))
print(type('10'))
print(type(True))
print(type(False))

nome = "João Paulo"
print(type(nome))
#tipagem dinâmica -> a variável assume o tipo dependendo da informaçõa

print(nome)
print(nome[3])
print(nome[0:4])
print(nome[2:])
print(nome[:3])
print(len(nome))
print(nome.lower())
print(nome.upper())
print(nome.capitalize())
print("J" in nome)
print(nome.count("a") + nome.count("ã"))
print(nome.startswith("J"))
print(nome.endswith("o"))

#operadores relacionais
# > < >= <= != ==
print("Operadores relacionais")
print(10>5)
print(10>13)
# ____ > ____ --> True/False
print("10 < 10 " , 10<10)
print("10 == 10" , 10==10)
# == é o operador de comparação
# = é o operador de atribuição
print("10 <= 10", 10<=10)
print("10 != 10", 10!=10)
print("10 != 11", 10!=11)
idade = int(input("Qual sua idade? "))
#print("Maior de 18?" , idade > 18)
"""
Se a pessoa tiver 18 anos ou mais , exibir a mensagem de que ela pode se matricular nas aulas de carro e moto.
"""
