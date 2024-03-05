nhours = input("number of hours:")
nrate = input("rate amount:")
try:
    fhours = float(nhours)
    frate = float(nrate)
except:
    print("Error, please enter numeric input")
    exit()
if fhours > 40:
    reg = fhours * frate
    otp = (fhours - 40) * (frate * 1.5)
    ntotal = reg + otp
    print("You have worked overtime:", nhours , "Your pay is:", ntotal)
else:
    reg = fhours * frate
    print("You have worked regular hours:", nhours , "Your pay is:", reg)