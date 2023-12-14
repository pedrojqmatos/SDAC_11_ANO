
hours = input("Enter Hours:")   #pergunta qual a quantidade horas
rates = input("Enter Rate:")    #pergunta qual a quantidade de dinheiro por hora
hour = float(hours)
rate = float(rates)

def computepay(hour, rate):

    if hour > 40:
        mon = hour * rate 
        difhour = hour - 40
        pay = (rate*1.5) * difhour
        total = pay + mon
        print("Vais receber:", total)

    else:
        mon = hour * rate
        print("Vais receber:", mon)

computepay(hour, rate)