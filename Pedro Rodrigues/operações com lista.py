numlist = list()
while True :
    inp = input("Enter a number: ")
    if inp == "done":
        break
    try :
        value = float(inp)
    except :
        print("Insert a valid number")
        continue

    numlist.append(value)
#soma dos numeros da lista e divide pelo numero de numeros da lista
    average = sum(numlist) / len(numlist)
print("The average of the list is ", numlist, average)