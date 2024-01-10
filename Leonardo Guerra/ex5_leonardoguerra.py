def computepay(hour, rate):

    if hour > 40:
        mon = hour * rate 
        difhour = hour - 40
        pay = (rate*1.5) * difhour
        total = pay + mon

    else:
        total = hour * rate
    return total

hours = input("Enter Hours:")
rates = input("Enter Rate:")    
fhour = float(hours)
frate = float(rates)
 
xp = computepay(fhour, frate)
print("Pay:", xp)