import math

# Entrar com um número e imprimir a raiz quadrada do número caso ele seja positivo e o quadrado do numero 
# caso ele seja negativo:
# ** Se o número inserido for 0 imprima a mensagem valor inválido

import math

numero = float(input("Entre com um número: "))

if numero >= 0:
    raiz_quadrada = math.sqrt(numero)
    print(f"A raiz quadrada de {numero} é {raiz_quadrada}")
else:
    quadrado = numero*numero
    print(f"O quadrado de {numero} é {quadrado}")