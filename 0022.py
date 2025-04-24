# Ler a idade de uma pessoa e imprimir a mensagem "você é maior de idade" se ela tiver 18 anos ou mais.

idade=float(input("Insira a idade: "))

print("A idade inserida foi: ", idade)

if idade>=18:

    print("Ele é maior de idade!")

else:

    print("Ele é menor de idade!")