
hours = input("Enter Hours:")   #pergunta qual a quantidade horas
rate = input("Enter Rate:")    #pergunta qual a quantidade de dinheiro por hora
float(hours) 
float(rate)    

if hours > 40: 
    difhours = hours - 40 
    mon = hours * rate
    pay = (rate*1.5)*difhours + mon
    print("O valor a ser pago é ", pay, "€")
else:
    mon = hours * rate
    print("O valor a ser pago é ", mon, "€")