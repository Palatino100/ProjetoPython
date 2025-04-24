# Sabendo-se  que 100 quilowatts de energia custa um sétimo do salario minimo, fazer um
# algoritimo que rreceba o valor do salário mínimo e a quantidadee de quilowatts gasta 
# por uma residência e calcule e imprima:

# O valor em reais de cada quilowatts
# O valor em reais a ser pago
# O novo valor a ser pago por essa residência com desconto de 10%

sm=float(input("Insira o novo valor do salário mínimo: \n"))
sm_formatado=f'{sm:.2f}'

qq=float(input("Insira  aquantidade de quilowatts: \n"))
qq_formatado=f'{qq:.2f}'

kw=float((sm/7)/100)
kw_formatado=f'{kw:.2f}'
print("O valor  de um kw é: \n", kw_formatado)

vp=float(qq*kw)
vp_formatado=f'{vp:.2f}'
print("O valor a pagar é: \n", vp_formatado)

vd=float(qq*kw)*0.9
vd_formatado=f'{vd:.2f}'
print("O valor a pagar com desconto é: \n", vd_formatado)


