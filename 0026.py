# Crie um programa para calcular o IMC de uma pessoa e 
# informar faixa de peso a qual a mesma se enquadra.
import math

peso=int(input("Informe o seu peso: "))
print("O peso informado foi : ",peso)

altura=float(input("Informe a sua altura: "))
print("A altura informada foi: ",altura)

imc=peso/math.pow(altura,2)

if imc<18.5:
    print("Voce esta abaixo do peso ideal!")
if imc>=18.5 and imc<25:
    print("Parabéns voce esta no seu peso ideal!")
if imc>=25 and imc<30:
    print("Você esta acima do peso!")
if imc>=30 and imc<35:
    print("Cuidado -  Obsidade grau 1")
if imc>=35 and imc<40:
    print("Cuidado - Obsidade grau 2")
if imc>40:
    print("Muito cuidado - Obsidade Móbida!")
exit()