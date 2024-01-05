total = 0
count = 0

while True:
    try:
        user_input = input("Enter a number: ")
        if user_input.lower() == "done":
            break

        number = float(user_input)
        total += number
        count += 1
    except ValueError:
        print("Invalid input! Please enter a valid number.")

if count > 0:
    average = total / count
    print(f"Total: {total}, Count: {count}, Average: {average}")
else:
    print("No valid numbers entered.")
