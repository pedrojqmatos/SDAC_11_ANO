totnum = 0
num = 0

while True:
    enter = input("Enter a number or Done :  ")
    if enter.lower() == 'done':
        break
    try:
        numero = float(enter)
        totnum += numero
        num += 1
    except ValueError:
        print("Error : Incorrect data.")
if totnum > 0:
    med = totnum / num
    print("Total:", totnum)
    print("Count:", num)
    print("Media:", med)
else:
    print("Invalid input")