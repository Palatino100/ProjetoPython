# Efetuar o cáculo da quantidade de litros de combustível gastos em uma viagem.
# Sabendo-se que o carro faz 12 km com um litro. Deverão ser fornecidos 
# o tempo gasto na viagem e a velocidade média

tempo=float(input("Insira o tempo da viagem:  "))
print(f"O tempo gasto na viagem foi:{tempo:.2f} ")

velocidade=float(input("Insira a velocidade média da viagem: "))
print(f"A velocidade média da viagem foi:{velocidade:.2f} ")

distancia=float(tempo*velocidade)
print(f"A distância percorrida foi de: {distancia:.2f}")

combustivel=float(distancia/12)

print(f"A quantidade de combustível utilizado é de:{combustivel:.2f} litros")
