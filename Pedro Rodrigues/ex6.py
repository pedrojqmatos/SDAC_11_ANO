#ex6

count = 0
total = 0.0

while True:
    user_input = input("Enter a number: ")

    if user_input == 'done':
        break
    
    try:
        fvalue = float(user_input)
    except ValueError:
        print("Incorrect data")

if count > 0:
    average = total / count
    print(total, count, average)
else:
    print("Invalid input !")