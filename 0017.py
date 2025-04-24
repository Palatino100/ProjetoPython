# Efetuar o cálculo de uma prestação em atraso, utilizando a fórmula:
# prestação=valor+(valor*(taxa/100)*tempo)

prestacao=float(input("Insira o valor da prestacão: "))
print(f"O valor da prestação é:{prestacao:.2f}")

tempo=int(input("Insira o tempo de atraso: "))
print("O tempo inserido foi:" , tempo, "meseses")

taxa=float(input("Insira a taxa de juros mensal: "))
print(f"O percentual inserido foi de: {taxa:.0%}")

cpa=prestacao+(prestacao*(taxa*tempo))

print(f"O valor da prestação em atraso é:{cpa:.2f}")
