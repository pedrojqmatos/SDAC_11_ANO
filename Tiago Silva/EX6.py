#Define as variáveis
count=0
total=0.0
#
while True:
    ent=input("Enter a number")
    if ent == "done":
        break
    try:
        fvalue= float(ent)
    except:
        print("Invalid number!")
        continue
    #Realiza as operações
    count= count + 1
    total= total + fvalue

print("Finished counting numbers", total, count, total / count)

