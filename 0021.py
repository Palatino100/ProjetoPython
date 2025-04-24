# Verificar se dois numeros - (num1 e num2) são:

# Se num1 e menor que num2
# Se num1 é diferente de num2
# Se num1 é maior que num2
# Se num1 é igual a num2
# Se num2 e menor que num1
# Se num2 é maior que num1

numero01=float(input("Insira o primeiro número: "))
numero02=float(input("Insira o segundo número: "))

print("O primeiro numero inserido foi: ", numero01)
print("O segundo numero inserido foi: ", numero02)

if numero01<numero02:
    print("numero01 é menor que numero02!")

if numero01!=numero02:
    print("numero01 e numero02 são diferentes!")

if numero01>numero02:
    print("numero01 é maior que numero02!")

if numero01==numero02:
    print("Os numeros são iguais!")

if numero02<numero01:
    print("O numero02 é menor que o numero01!")

if numero02>numero01:
    print("O numero02 é maior que o numero01!")