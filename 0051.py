with open('arquivo.txt', 'w+') as file:
    file.write("Linha 01 \n")
    file.write("Linha 02 \n")
    file.write("linha 03 \n")
    file.seek(0,0)
    print(file.read())
