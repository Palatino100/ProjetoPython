#Exercício 6 - Cálculo do Custo Total
#Você foi contratado para desenvolver um programa que calcula o custo total
#de um produto após a aplicação de impostos e descontos. O usuário deve
#fornecer o preço original, a porcentagem de desconto, e a taxa de imposto. O
#programa deve calcular e exibir o preço final do produto

precox=float(input("Digite o preço original do produto: \n"))
precox_formatado=f'{precox:.2f}'
descontox=float(input("Digite o percentual de desconto: \n"))
taxa_impostox=float(input("Digite a taxa de imposto: \n"))


calcular_desconto=int(precox*(descontox/100))
calcular_desconto_formatado=f'{calcular_desconto:.2f}'
calcular_imposto=int(precox*(taxa_impostox/100))
calcular_imposto_formatado=f'{calcular_imposto:.2f}'
preco_final=int(precox+calcular_imposto-calcular_desconto)
preco_final_formatado=f'{preco_final:.2f}'

print("O preço é : \n", precox_formatado)
print("O desconto recebido foi: \n", calcular_desconto_formatado)
print("O imposto pago é: ", calcular_imposto_formatado)
print("O preço final do produto é: \n", preco_final_formatado)
