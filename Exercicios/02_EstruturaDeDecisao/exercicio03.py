"""
Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, O - Outros, Opção Inválida.
"""
opcao_selecionada = input("Informe uma opção:\nF - Feminino\nM - Masculino\nO - Outros\nEscolha: ")

opcao_selecionada = opcao_selecionada.upper()

if opcao_selecionada == "F":
    print("Feminino")
elif opcao_selecionada == "M":
    print("Masculino")
elif opcao_selecionada == "O":
    print("Outros")
else:
    print("Opção inválida")
