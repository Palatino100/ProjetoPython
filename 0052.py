with open('arquivo.txt', 'a+') as file:
# O "a+ Adiciona o conteúdo a última linha do arquivo"
    file.write("Linha 04 \n")
    file.seek(0)
    print(file.read())
