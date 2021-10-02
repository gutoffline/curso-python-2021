"""
Se a pessoa tiver 18 anos ou mais , exibir a mensagem de que ela pode se matricular nas aulas de carro e moto.
"""
print("AUTO ESCOLA \nPREENCHA SUAS INFORMAÇÕES \n")
idade = int(input("Qual sua idade? "))

if idade >= 18 :
    print("Parabéns")
    print("você pode se matricular na aula de carro e moto")
else:
    print("Volte em", 18-idade, "anos")

print("\n\nFIM DO PROGRAMA")