#recebe o valor de input dado pelo ultilizador em int
inhours=input("Enter hours: ")
inrate=input("Enter Rate: ")

#neste bloco, caso o utilizador tente colocar um número que não seja float, como letras, o programa irá imprimir um erro
fhours = float(inhours)
frate = float(inrate)

def computepay(inhours, inrate):

#calcula o valor do pagamento caso o funcionário trabalhou mais de 40 horas e multiplica o rate para maior pagamento.
    if inhours > 40:
        hxr = inhours * inrate
        pag = (inhours - 40) * (inrate * 1.5)
        total = hxr + pag

    else:
        return total

xp = computepay(fhours, frate)
print("Pay:", xp)