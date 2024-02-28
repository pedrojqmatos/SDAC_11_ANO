hours = input("Enter Hours:")   #pergunta qual a quantidade horas
rates = input("Enter Rate:")    #pergunta qual a quantidade de dinheiro por hora

try:
    hour = float(hours)
except:
    print("Error, please enter numeric input.")
    exit()
#Apenas aceita valores float se o valor não for float, da uma mensagem de erro e sai

try:
    rate = float(rates)
except:
    print("Error, please enter numeric input.")
    exit()
#Apenas aceita valores float se o valor não for float, da uma mensagem de erro e sai

if hour > 40:
    mon = hour * rate 
    difhour = hour - 40
    pay = (rate*1.5) * difhour
    total = pay + mon
    print("Vais receber:", total)
#se "hour" for maior que 40 faz a mutiplicação normal e pega nas horas extras e mutiplicas po 1.5

else:
    mon = hour * rate
    print("Vais receber:", mon)
    #se for menor que 40 faz a conta normal