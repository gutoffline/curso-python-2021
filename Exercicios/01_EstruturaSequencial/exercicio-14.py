peso = float(input('Informe o peso dos peixes pescados:'))
multaPorQuilo = 4.0
pesoMaximo = 50.0

if (peso > pesoMaximo):
    excesso = peso - pesoMaximo
    print('Excesso de peso:', excesso)
    multa_pagar = excesso * multaPorQuilo
    print('Valor da multa por excesso', multa_pagar)
else:
    print('Nao houve excesso de peso')
