hours = input("Enter Hours:")   
rates = input("Enter Rate:")    

try:
    hour = float(hours)
except:
    print("Error, please enter numeric input.")
    exit()

try:
    rate = float(rates)
except:
    print("Error, please enter numeric input.")
    exit()

if hour > 40:
    mon = hour * rate 
    difhour = hour - 40
    pay = (rate*1.5) * difhour
    total = pay + mon
    print("Vais receber:", total)

else:
    mon = hour * rate
    print("Vais receber:", mon)