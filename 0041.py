# Chico tem 1.50 metros e cresce dois centímetros por ano, enquanto Juca tem 1.10 e cresce três 
# centímetros por ano.
# Construir um algoritimo que calcule e imprima quantos anos serão necessários para que Juca seja 
# maior que Chico.

alt_chico=float(1.50)
alt_juca=float(1.10)
anos=int(0)

while alt_juca<=alt_chico:

    alt_chico=alt_chico+0.02
    alt_juca=alt_juca+0.03
    anos=anos+1


print("O número de anos que Juca levará para ser maior que Chico é de: ",anos)
print(f"A altura atual de Chico é:{alt_chico:.2f} ")
print(f"A altura atual de Juca é:{alt_juca:.2f} ")



