horas_trabalhadas = (input("enter Hours"))
taxa_horaria = (input("enter rate"))

ht= float(horas_trabalhadas)
th = float( taxa_horaria)

if ht > 40:
    reg = ht * th
    pay = (40 - ht ) + (th * 1.5)
    ntotal = reg + pay
    print ("You over hours are:", horas_trabalhadas, "Your payment is:", ntotal)
else:
    pay = ht * th

print("You have worked the normal amount of hours:", horas_trabalhadas, "Your payment is:", reg)