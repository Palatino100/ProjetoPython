# Ler a temperatura em graus Centígrados e apresenta-lá em graus Fahrenheit:

centigrados=int(input("Digite o valor da temperatura em graus centigrados: "))
print("A temperatura digita em graus centigrados foi: ", centigrados)

fahrenheit=((9*centigrados)+160)/5

print(f"A temperatura em Fahrenheit é:{fahrenheit:.2f} ")
