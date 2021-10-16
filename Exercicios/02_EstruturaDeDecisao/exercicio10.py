print ("""Informe o turno em que voce estuda
[M]atutino
[V]espertino
[N]oturno""")
turno = input('Opcao escolhida: ').upper()

if (turno == 'M'):
    print ('Bom dia!')
elif (turno == 'V'):
    print ('Boa tarde!')
elif (turno == 'N'):
    print ('Boa noite!')
else:
    print ('Valor invalido')
