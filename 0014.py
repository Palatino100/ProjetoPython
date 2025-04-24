# Entrar com os valores dos catetos e imprimir o valor da hipotenusa

import math

# Solicita ao utilizador os valores dos catetos
cateto1 = float(input("Digite o valor do primeiro cateto: "))
print("O valor do cateto1 é: ", cateto1)
cateto2 = float(input("Digite o valor do segundo cateto: "))
print("O valor do cateto2 é: ", cateto2)
# Calcula a hipotenusa usando o teorema de Pitágoras
hipotenusa = math.sqrt(cateto1**2 + cateto2**2)
# Imprime o resultado
print(f"A hipotenusa é: {hipotenusa}")