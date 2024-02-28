nhours = input("Number of hours:")
nrate = input("Rate amount:")

try:
    fhours = float(nhours)
    frate = float(nrate)
except:
    print("Error! You provided an invalid value, please input a valid numeric input")
    exit()

if fhours > 40:
    reg = fhours * frate
    otp = (fhours - 40) * (frate * 1.5)
    ntotal = reg + otp
    print("You have worked overtime:", nhours , "Your pay is:", ntotal)
else:
    reg = fhours * frate
    print("You have worked regular hours:", nhours , "Your pay is:", reg)