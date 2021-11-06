#exceções

try:
    print(11/0)
except ZeroDivisionError:
    print("Divisão por 0 não pode acontecer")
finally:
    print("Finalizado")

try:
    print(x)
except NameError:
    print("Valor não encontrado")
finally:
    print("Finalizado")