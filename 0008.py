#Exercício 8 - Conversão de Unidades: Você foi contratado para criar um programa que converte uma distância em
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