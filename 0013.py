# Entrar com o lado de um quadrado  e imprimir:
# Perímetro
# A area
# A diagonal

import math

lado=float(input("Insira o lado do quadrado: \n"))

perimetro=float(lado*4)
area=float(lado*lado)
diagonal=float(lado * math.sqrt(2))

print(f"O perímetro do quadrado é:  {perimetro:.2f}")
print(f"A área  do quadrado é:  {area:.2f}")
print(f"A diagonal  do quadrado é:  {diagonal:.2f}")
