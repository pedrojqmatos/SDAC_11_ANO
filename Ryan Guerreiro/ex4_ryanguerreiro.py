#salario bruto

#recebe o valor de input dado pelo ultilizador em int
inhours=input("Enter hours: ")
inrate=input("Enter Rate: ")

#neste bloco, caso o utilizador tente colocar um número que não seja float, como letras, o programa irá imprimir um erro
try:
    fhours = float(inhours)
    frate = float(inrate)
except:
    print("Error! You provided an invalid value, please input a valid numeric input")
    exit()

#calcula o valor do pagamento caso o funcionário trabalhou mais de 40 horas e multiplica o rate para maior pagamento.
if fhours > 40:
    hxr = fhours * frate
    pag = (fhours - 40) * (frate * 1.5)
    total = hxr + pag
    print("You have worked overtime:", inhours , "Your pay is:", total)

#caso o funcionário não trabalhe mais de 40 horas, irá calcular a taxa de horas multiplicado pela taxa de avaliação
else:
    hxr = fhours * frate
    print("You have worked regular hours:", inhours , "Your pay is:", hxr)