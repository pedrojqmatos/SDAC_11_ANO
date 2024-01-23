#Definição das variávies (contador,toatal)
contador = 0
total= 0.0

#iniciar o loop (ciclo repetitivo)
while True:

#iniciar o input
    svalue = input("Enter a number: ")

#estrutura condicional com try para verificar os valores em float
    if svalue == "done":
        break
    try:
        fvalue=float(svalue)
    except:
        print("Invalid input!")
    continue

#realizar os calculos
cnt=contador+1
ttl=total+fvalue

#mostrar os resultados
print(ttl,cnt,ttl/cnt)