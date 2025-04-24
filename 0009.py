#Exercício 9 - Cálculo do Volume de uma Caixa: Você foi contratado para desenvolver um programa que calcula o volume de
#uma caixa retangular. O usuário deve fornecer as medidas de comprimento,
#largura e altura, e o programa deve calcular e exibir o volume

altura=int(input("Digite a altura da caixa: "))
largura=int(input("Digite a largura da caixa: "))
comprimento=int(input("Digite o comprimento da caixa: "))
	
vol = altura*largura*comprimento 

print("O volume da caixa é  é:", vol)
