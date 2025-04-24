# Fazer um algoritimo para ler quatro notas de um aluno em uma 
# disciplina, e depois imprimir a média aritimética das notas e 
# a situação do aluno a partir dos seguintes critérios:
# MÉDIA<50:REPROVADO
# MÉDIA ENTRE 50 E 69,9:RECUPERAÇÃO
# MÉDIA>=70:APROVADO 

aluno=input("Nome do aluno: ")
print("O nome do aluno é: ", aluno)

nota01=float(input("Insira a primeira nota: "))
print(f"A nota inserida foi:{nota01:.2f}")

nota02=float(input("Insira a segunda nota: "))
print(f"A nota inserida foi:{nota02:.2f}")

nota03=float(input("Insira a terceira nota: "))
print(f"A nota inserida foi:{nota03:.2f}")

nota04=float(input("Insira a quarta nota: "))
print(f"A nota inserida foi:{nota04:.2f}")

total_notas=float(nota01+nota02+nota03+nota04)
media_notas=float(nota01+nota02+nota03+nota04)/4

print(f"O total de pontos do aluno é:{total_notas:.2f}")
print(f"A média de pontos do aluno é:{media_notas:.2f}")

if media_notas<50:
    print("O aluno esta reprovado!")

if media_notas>=50  and media_notas<70:
    print("O aluno esta de recuperação!")

if media_notas>=70 and media_notas<100:
    print("O aluno esta aprovado!")

if media_notas>100:
    print("Foram inseridas notas inválidas!")
exit()