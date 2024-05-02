total=0
counter =0

while True:
    uss= input ("Enter a number: ")
    if uss == "done":
        break
    try:
        number= float(uss)
    except:
        print("invalid")
        continue
    counter = counter + 1
    total = total + number
    
print ("Finished counting numbers", total, counter, total / counter)

        
    