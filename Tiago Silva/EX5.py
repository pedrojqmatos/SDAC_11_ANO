def computepay(hours, rate):
    print("Compute pay is:", hours,rate)
    if hours > 40:
        reg = rate * hours
        otp = (hours-40) * (rate *1.5)
        pay = reg + otp
    else:
        pay = hours * rate
    print("Returning:", pay)
    return pay

nhours = input("Number of hours")
nrate = input ("Rate amount")
frate= float
fhours = float
