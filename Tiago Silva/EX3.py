nh=input("Número de Horas:")

rat=input("Taxa por Hora:")

fnh=float(nh)
frat=float(rat)

if fnh > 40:
  reg = fnh * frat
  otp= (fnh - 40 ) * (frat*1.5)
  ntotal= reg + otp
  print("Trabalhaste quantas horas a mais:", nh, "O teu pagamento é:", ntotal) 
else:
    reg = fnh * frat
    print("Trabalhaste o número normal de horas", nh, "O teu pagamento é:" ,reg)

