# Entrar com três números e imprimí-los em ordem descrecente de valor:

a=float(input("Insira o primeiro lado: "))
print(f"O numero inserido foi:{a:.2f}")
b=float(input("Insira o segundo lado: "))
print(f"O numero inserido foi:{b:.2f}")
c=float(input("Insira o terceiro lado: "))
print(f"O numero inserido foi:{c:.2f}")

if a<b+c and b<a+c and c<a+b:
    print("Podem ser lados de um triângulo!")
else:
    print("Não podem ser lados de um triângulo!")



