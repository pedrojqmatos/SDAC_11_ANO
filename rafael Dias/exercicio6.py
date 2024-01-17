counter = 0
total = 0.0
While true :
    svalue = input("Enter a number: ")
    if svalue == "done" :
        break
    try :
        fvalue = float(svalue)
    except :
        print("Invalid input! Please, enter a valid number")
        continue
    counter =counter + 1
    total = total + fvalue
print ("finished counting numbers", total, counter, total / counter)