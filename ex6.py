# Inicialização das variáveis total e contagem
total = 0
contagem = 0

# Loop principal que continua até que o utilizador introduza "done"
while True:
    # Solicita ao utilizador que introduza um número ou "done"
    entrada = input("Introduza um número (ou 'done' para sair): ")

    # Verifica se o utilizador quer sair do programa
    if entrada == 'done':
        break

    try:
        # Tenta converter a entrada para um número
        numero = float(entrada)

        # Se a conversão for bem-sucedida, soma o número ao total e incrementa a contagem
        total += numero
        contagem += 1

    except ValueError:
        # Se a conversão falhar, imprime uma mensagem de erro e continua para a próxima iteração
        print("Erro: Introduza um número válido.")

# Verifica se pelo menos um número foi introduzido antes de calcular e imprimir o resultado
if contagem > 0:
    # Calcula a média dos números
    media = total / contagem

    # Imprime o total, a contagem e a média
    print("Total:", total)
    print("Contagem:", contagem)
    print("Média:", media)
else:
    # Caso nenhum número tenha sido introduzido, imprime uma mensagem indicando isso
    print("Nenhum número foi introduzido.")