count= 0
total=0.0
while True:
    inp=input("Enter a number or done to leave: ")
    if inp=="done":
        break
    try:
        finp= float(inp)
    except :
        print("Invalid input!")
        continue

    count = count + 1
    total= total+finp
    average=total/count 
print("Finished countig numbers:", total, count,average)