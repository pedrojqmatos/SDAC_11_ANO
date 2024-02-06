#definir contado e total
total_numbers =0
count =0.0

#verifica se a entrada e float ou done
while True:
    user_input = input("Enter a number: ")
    if user_input == "done":
        break
    try :
        float_value = float (user_input)
        
    except :
        print("Invalid input! Please enter a valid number or 'done' to finish the calculation")
        continue

#calcula a função 
count = count +1
total_numbers = total_numbers + float_value

print("finishd counting numbers", total_numbers,count,total_numbers / count)
