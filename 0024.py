# Um quiosque de sorvete vende casquinhas somente nos sabores Chocolate - 
# "C" e morango - "M".
# Faça um algoritimo para imprimir uma mensagem nas seguintes situações:
# Sorvete de chocolate com mais de três bolas: desconto 10%
# Sorvete de chocolate com qualquer quantidade de bolas menor ou igual
# a 3: desconto 5%
# Sorvete de morango: desconto 0
# ** Calcule também o total a ser pago pelo cliente sabendo que o preço 
# por bola é R$ 2,00

sorvete=input("Digite C ou M ! :")

if sorvete=="c" or sorvete=="C":
    bolas=int(input("Digite a quantidade de bolas: "))

    if bolas>3:
        print("O desconto será de 10%!")

        ptotal=float(bolas*2*0.9)
        print(f"O preço a ser pago pelo cliente será de : {ptotal:.2f}")
    
    else:
        ptotal=float(bolas*2*0.95)
        print(f"O preço a ser pago pelo cliente será de :{ptotal:.2f}")
    
if sorvete=="m" or sorvete=="M":
        bolas=int(input("Digite a quantidade de bolas: "))  
        ptotal=float(bolas*2)
        
        print(f"O preço a ser pago pelo cliente será de :{ptotal:.2f}")
    
exit()
    


