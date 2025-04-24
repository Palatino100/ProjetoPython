
print("********************")
print("* CALCULADORA * " )
print("********************")
print("Digite + para somar \n")
print("Digite - para subtrair \n")
print("Digite * para multiplicar \n")
print("Digite / para dividir \n")

opcao=input("Digite a operacao: \n")

if(opcao=="+"):
    numero01=float(input("Digite o primeiro número: \n" ))
    numero02=float(input("Digite o primeiro número: \n" ))

    calcular=numero01+numero02

    print(f"O valor da soma é:{calcular:.2f}")

if(opcao=="-"):
    numero01=float(input("Digite o primeiro número: \n" ))
    numero02=float(input("Digite o primeiro número: \n" ))

    calcular=numero01-numero02
    print(f"O valor da subtração é:{calcular:.2f}")

if(opcao=="*"):
    numero01=float(input("Digite o primeiro número: \n" ))
    numero02=float(input("Digite o primeiro número: \n" ))

    calcular=numero01*numero02
    print(f"O valor da multiplçicação é:{calcular:.2f}")

if(opcao=="/"):
    numero01=float(input("Digite o primeiro número: \n" ))
    numero02=float(input("Digite o primeiro número: \n" ))

    calcular=numero01/numero02
    print(f"O valor da divisao é:{calcular:.2f}")
    exit()