# Criando um arquivo em python
# O "w+" significa leitura e escrita
file=open('abc.txt', 'w+')
file.write("Eu adoro salada! \n")
file.write("Eu gosto de pão! \n")
file.write("Eu adoro doce! \n")
# Posicionando o cursor no início do arquivo
file.seek(0, 0)
print("Lendo linhas!")
print(file.read())
print("---------------------------------------------")
file.seek(0, 0)
# Lê linha por linha
print(file.readline())
print(file.readline())
print("---------------------------------------------")
#Lê uma lista de linhas
file.seek(0, 0)
print(file.readlines())
# Fecha o arquivo
file.close()