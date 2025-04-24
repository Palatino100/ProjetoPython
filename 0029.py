# Entrar com dois números e imprimí-los em ordem crescente:
numero01=float(input("Insira o primeiro numero: "))
print(f"O numero inserido foi:{numero01:.2f}")
numero02=float(input("Insira o primeiro numero: "))
print(f"O numero inserido foi:{numero02:.2f}")

if numero01>numero02:
    print(f":{numero02:.2f}")
    print(f":{numero01:.2f}")
if numero02>numero01:
    print(f":{numero01:.2f}")
    print(f":{numero02:.2f}")
if numero02==numero01:
    print("Os números são iguais!" )
  