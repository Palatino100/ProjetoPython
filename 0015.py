# Criar um algoritimo que efetue o cálculo do salário liquidode um professor.
# Os dados fornecidos serão:

# Nome do professor (np)
# Valor da hora aula (vha)
# Numero de aulas dadas no mês (nhm)
# Percentual de desconto do INSS (inss)
# Salário liquido

np=input("Nome do professor: ")
print("O nome do professor é: ", np)

vha=float(input("Insira o valor da hora aula:  "))
print(f"O valor da hora aula é: {vha:.2f}")

nhm=int(input("Insira o numero de aulas dadas no mês: "))
print("O numero de aulas dades no mês é: ",nhm)

inss=float(input("Insira o percentual do INSS: "))
print(f"O percentual inserido foi de: {inss:.0%}")

sb=float(vha*nhm)
vinss=float(sb*inss)
sl=float(sb-vinss)

print(f"O valor do salário líquido é: {sl:.2f} ")

