import alunos
import materias
import menu
import os

repetir = "s"
while repetir == "s":
    opcao = menu.ExibirMenu()

    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

    if opcao == 1:
        alunos.Cadastro()
    elif opcao == 2:
        alunos.Relatorio()
    elif opcao == 3:
        materias.Cadastro()
    elif opcao == 4:
        materias.Relatorio()
    else:
        print("O programa será finalizado. Até mais.")
        repetir = "n"