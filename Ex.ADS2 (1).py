#-*-coding:utf8;-*-
#qpy:console
#Exercício 1 - Você foi contratado para desenvolver um programa que calcula
#a média aritmética de três notas fornecidas pelo usuário. O programa deve
#calcular a média e exibir o resultado

print("Vamos calcular sua media")
nota1=float(input("Digite a primeira nota: "))
nota2=float(input("Digite a segunda nota: "))
nota3=float(input("Digite a terceira nota: "))
media=(nota1+nota2+nota3)/3
print("Sua media é: ", media)

#Exercício 2 - Você foi contratado para criar um programa que pede ao
#usuário para inserir 3 números. Esses números devem ser adicionados a
#uma lista, e o programa deve calcular e exibir a soma dos elementos da
#lista

num1=int(input("Digite um numero: "))
num2=int(input("Digite um numero: "))
num3=int(input("Digite um numero: "))
list=[num1,num2,num3]
lista=num1+num2+num3
print("os numeros da lista são:",list,"A soma destes numeros é:",lista)

#Exercício 3 - Você foi contratado para implementar um programa que
#converte a temperatura de Celsius para Fahrenheit. O usuário insere a
#temperatura em Celsius, e o programa deve exibir a temperatura em
#Fahrenheit.

graus=float(input("Digite a temperatura em Celsius: "))
print("Digite 1 se quer converter de Celsius para Fahrenheit: ")
    
temp =graus*1.8+32
    	
print(f"{temp:.1f}" "Fahrenheit")

#Exercício 4 - Você foi contratado para escrever um programa que calcula a
#área e o perímetro de um retângulo. O usuário fornece as medidas dos
#lados (largura e altura), e o programa calcula e exibe a área e o perímetro

altura=int(input("Digite a altura do retangulo: "))
largura=int(input("Digite a largura do retangulo: "))
area=largura*altura
perimetro= 2*(altura+largura)
print("A area do triangulo é:", area)
print("O perimetro do triangulo é:",perimetro)

#Exercício 5 - Conversão de Moedas: Você foi contratado para criar um programa que converte um valor em reais
#(BRL) para dólares americanos (USD). O usuário deve fornecer o valor em
#reais e o programa deve exibir o valor correspondente em dólares

reais=float(input("Digite quantos reais quer converter: "))
dolar=5.79*reais
print("o valor convertido é:",dolar, "dólares")

#Exercício 6 - Cálculo do Custo Total
#Você foi contratado para desenvolver um programa que calcula o custo total
#de um produto após a aplicação de impostos e descontos. O usuário deve
#fornecer o preço original, a porcentagem de desconto, e a taxa de imposto. O
#programa deve calcular e exibir o preço final do produto

preco=float(input("Digite o preço do produto: "))
desconto=float(input("Digite o valor do desconto em porcentagem(ex: 10=10%): "))
imposto=float(input("Digite o valor do imposto em porcentagem(ex: 10=10%): "))
desc=preco*(desconto/100)
impos=preco*(imposto/100)
custo=preco+impos-desc
print(custo,"reais")

#Exercício 7 - Conversão de Unidades: Você foi contratado para criar um programa que converte uma distância em
#quilômetros para metros e centímetros. O usuário deve fornecer a distância
#em quilômetros, e o programa deve calcular e exibir a distância equivalente
#em metros e centímetros

km=float(input("Digite quantos quilometros quer converter: "))
escolha=int(input("Digite 1 para metros ou 2 para centimetros:"))
if escolha == 1:
  metros=km*1000
  print(metros,"metros")
if escolha==2:
  centimetros= km*100000
  print(centimetros,"centimetros")

#Exercício 8 - Cálculo do Volume de uma Caixa: Você foi contratado para desenvolver um programa que calcula o volume de
#uma caixa retangular. O usuário deve fornecer as medidas de comprimento,
#largura e altura, e o programa deve calcular e exibir o volume

altura=int(input("Digite a altura da caixa "))
largura=int(input("Digite a largura da caixa: "))
comprimento= int(input("Digite o comprimento da caixa: "))
	
vol = altura*largura*comprimento 

print("O volume da caixa é  é:", vol)
