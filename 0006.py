#Exercício 6 - Conversão de Moedas: Você foi contratado para criar um programa que converte um valor em reais
#(BRL) para dólares americanos (USD). O usuário deve fornecer o valor em
#reais e o programa deve exibir o valor correspondente em dólares

reaisx=float(input("Digite quantos reais quer converter: \n"))
dolarx=float(reaisx/5)
dolarx_formatado=f'{dolarx:.2f}'
print("O valor convertido em dolares é : \n", dolarx_formatado, "dólares")
