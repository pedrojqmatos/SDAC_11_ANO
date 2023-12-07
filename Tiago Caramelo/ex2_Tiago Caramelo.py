#imput onde iremos escolher o número de horas, de seguida o "inp" e o "TC" são as 2 variáveis
nhours = input("Enter Hours:")
nrate = input("Enter Rate:")
#a variável "AB" vai converter o "inp" em int; #a variável "CB" vai converter o "TC" em float
ntotal = int(nhours) * float(nrate)
#valor total que iremos receber
print("Pay:", ntotal)



