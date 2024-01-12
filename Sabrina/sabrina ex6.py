count= 0
total=0.0

while True: 

    inp=input("Enter a number or done to leave: ")
    if inp=="done":
        break

    try: # converter o valor para float

        finp= float(inp)

    except :    # caso o valor n seja "done" ou um numero imprime 'Invalid input!' e continua o codigo

        print("Invalid input!")
        continue

    count = count + 1
    total= total+finp
    average=total/count 
print("Finished countig numbers:", total, count,average)    # imprime o total a conta e a media dos valores 