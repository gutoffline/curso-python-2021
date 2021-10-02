"""
OPERADORES LÓGICOS
    not --> negação, se a operação resultar em verdadeiro, ele nega e transforma em falso, se resultar em falso, ele nega e transforma em verdadeiro
    and --> e, todos os resultados devem ser verdadeiros para resultar verdadeiro, se apenas um for falso, a expressão inteira será falsa
    10 < 20 --> verdadeiro
    30 > 10 --> verdadeiro
    10 < 20 and 30 > 10 --> verdadeiro
    10 < 20 and 30 > 40 --> falso

    nota >= 5 and faltas < 10

    or --> ou, apenas um resultado precisa ser verdadeiro para a expressão retornar verdadeiro, mas se todos forem falsos a empressão será falsa
    10 < 20 --> verdadeiro
    30 > 10 --> verdadeiro
    10 < 20 or 30 > 10 --> verdadeiro
    10 < 20 or 30 > 40 --> verdadeiro
    10 < 7 or 30 > 10 ---> verdadeiro
    10 < 7 or 30 > 40 ---> falso
"""
nota = 3
faltas = 13
print(nota >=5 or faltas < 10)