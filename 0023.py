# Ler um número inteiro e dizer se ele é par ou impar

numero=float(input("Insira um numero: "))
print("O numero inserido foi: ", numero )

resto=float(numero%2)

if resto==0:
    print("Esse numero é par!")
else:
    print("Esse numero é impar!")