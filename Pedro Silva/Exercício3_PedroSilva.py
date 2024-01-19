hours = input("Enter Hours:")   #pergunta qual a quantidade horas
rates = input("Enter Rate:")    #pergunta qual a quantidade de dinheiro por hora
hour = float(hours) 
rate = float(rates)    

if hour > 40:
    mon = hour * rate 
    difhour = hour - 40
    pay = (rate*1.5) * difhour
    total = pay + mon
    print("O valor a ser pago é ", total, "€")
#se "hour" for maior que 40 faz a mutiplicação normal e pega nas horas extras e mutiplicas po 1.5

else:
    mon = hour * rate
    print("O valor a ser pago é ", mon, "€")
#se for menor que 40 faz a conta normal