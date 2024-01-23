#Definir variáveis (contagem, total)
total = 0.0
contagem = 0
#iniciar ciclo repetitivo
while True:
#iniciar o input
    #pedir ao utilizador que meta um número para começar ou 'done'
    entrada = input("Enter a number:" )
    #caso o utilizador quiser terminar é so escrever um 'done'
    if entrada == "done":
        break
    try:
        number = float(entrada)
    except ValueError:
        print("Erro: Introduza um número válido.")
        continue
#Realizar as operaçoes
    total = total + number
    contagem = contagem + 1
print ("Termina de contar os números", "Total:", total, "Contagem:" ,contagem, "Média:" ,total / contagem)
        
