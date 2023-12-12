
nhours = input("horas?")
nrate = input("preço por hora?")

fhours = float(nhours)
frate = float(nrate)

if fhours > 40:
    reg = fhours * frate
    otp = (fhours-40) * (frate*1.5)
    ntotal = reg + otp 
    print("Trabalhas-te:", nhours , "Pago-te:", ntotal)

else:
    reg = fhours * frate
    print("Trabalhas-te:", nhours , "Pago-te:", reg)
