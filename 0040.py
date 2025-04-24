soma = 0

while True:
    # Solicita um número ao usuário
    numero = input("Digite um número para somar (ou '0' para sair): ")
    
    # Verifica se o usuário digitou '0' para sair
    if numero == "0":
        break
    
    # Tenta converter o input para um número
    try:
        numero = float(numero)  # Converte para float para permitir números decimais
        soma += numero  # Adiciona o número à soma
    except ValueError:
        print("Por favor, digite um número válido.")

# Exibe o resultado final
print(f"A soma dos números digitados é: {soma}")