# Entrar com a base e a altura de um retângulo e imprimir a seguinte saída:

# Perímetro
# A area
# A diagonal

import math

base=float(input("Insira  o tamanho da base: \n"))
altura=float(input("Insira a altura: \n"))

perimetro=float(2 * (base + altura))
area=float(base*altura)
diagonal=float(base**2 + altura**2)**0.5

print(f"O perímetro do retangulo é: {perimetro:.2f}")
print(f"A area do retangulo é: {area:.2f}")
print(f"A diagonal do retângulo é: {diagonal:.2f}")
