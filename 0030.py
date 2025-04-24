# Criar  um algoritimo que insira dois números e imprimir o quadrado do menor número
#  e a raiz quadrada do maior número:
import math
numero01=float(input("Insira o primeiro numero: "))
print(f"O numero inserido foi:{numero01:.2f}")
numero02=float(input("Insira o segundo numero: "))
print(f"O numero inserido foi:{numero02:.2f}")

if numero01>numero02:
    quadrado_menor=numero02*numero02
    raiz_quadrada = math.sqrt(numero01)

print(f"O numero elevado ao quadrado foi:{numero02:.2f}")
print(f"O quadrado é:{quadrado_menor:.2f}")

print(f"O número de onde será calculada a raiz quadrada é:{numero01:.2f}")
print(f"A raiz quadrada do número é:{raiz_quadrada:.2f}")

if numero02>numero01:
    quadrado_menor=numero01*numero01
    raiz_quadrada = math.sqrt(numero02)

    print(f"O numero elevado ao quadrado foi:{numero01:.2f}")
    print(f"O quadrado é:{quadrado_menor:.2f}")

    print(f"O número de onde será calculada a raiz quadrada é:{numero02:.2f}")
    print(f"A raiz quadrada do número é:{raiz_quadrada:.2f}")

if numero01==numero02: 
 print("Os números são iguais não é possível a reqlização de cálculos!")

 exit()   
