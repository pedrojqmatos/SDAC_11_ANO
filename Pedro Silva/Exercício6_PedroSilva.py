count = 0
total = 0.0

while True:
    number = input("Enter Number:")

    if number == "done":
        break
    try: 
        num = float(number)
    except: 
        print("Invalid input")
        continue

    count = count + 1
    total = total + num 
    media = total / count

print("Finished counting number", total, count, media)
#com o while true o input fica a perguntar em loop, quanto receber um done soma todos o valor começando pelo 0 daí a variaval total, se não for colocado um numero ira dar um mesagem
#de erro ,tambem calculara a quantidade de numeros colocaste e tambem irá fazer a média dos numeros