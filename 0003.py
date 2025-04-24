#-*-coding:utf8;-*-
#qpy:console

#Exercício 3 - Você foi contratado para criar um programa que pede ao
#usuário para inserir 3 números. Esses números devem ser adicionados a
#uma lista, e o programa deve calcular e exibir a soma dos elementos da
#lista:
print("Insira três numeros! \n")
num01=int(input("Digite o primeiro numero: \n"))
num02=int(input("Digite o primeiro numero: \n"))
num03=int(input("Digite o primeiro numero: \n"))

list=[num01,num02,num03]
soma=num01+num02+num03

print("Os numeros da lista são:\n", list , "\n 1A soma dos números é: ", soma)
