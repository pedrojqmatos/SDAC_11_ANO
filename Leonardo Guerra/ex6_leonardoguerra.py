total=0
contagem=0

while True:
    entrada = input (" Introduza um número (ou'done' para sair): ") 

    if entrada == "done":
        break

    try:
        numero = float (entrada)
        total += numero
        contagem = contagem + 1
    except ValueError:
        print("Erro: Introduza umm número válido") 

if contagem > 0 :
    media = total / contagem
    print ("total:" , total)
    print ("Contagem", contagem)
    print ("Média", media)
else :
    print("Nenhum número foi introduzido")