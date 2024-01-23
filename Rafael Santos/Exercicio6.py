#Sum, Count and Average

counter = 0
total = 0.0

# Loop
while True :                             
    svalue = input("Enter a number: ")   # Solicita um número ao usuário
    if svalue == "done" :                # Se o usuário digitar "done", o loop é encerrado
        break
    # Tenta converter o valor inserido em float
    try :
        fvalue = float(svalue)
    except :
        print("invalid input! please, enter a valid number")
        continue             # Volta para o início do loop para solicitar um novo número
    counter = counter + 1    # Acrescenta +1 à variavel counter
    total = total + fvalue   #
print("Finished counting numbers -" , "Total:", total, " Counter:", counter, " Average:", total / counter)