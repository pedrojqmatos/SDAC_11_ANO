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
