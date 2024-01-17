#gross pay program
hours = input("Number of hours:")         # Pede ao utilizador para intruduzir o numero de horas
rate = input("Rate amount:")              # Pede ao utilizador para intruduzir o valor recebido por hora

try:
# Converter string para float
    fhours = float(hours)
    frate = float(rate)
except:
    print("Error! You provided an invalid value, please input a valid numeric input")  #Enviar alerta quando o utilizador nao insere numeros
    exit()

#se o numero de horas for maior que 40
if fhours > 40:
    reg = fhours * frate                             #Calcula o valor recebido das 40 horas regulares
    otp = (fhours - 40) * (frate * 1.5)              #Calcula o valor recebido numero de horas extras
    total = reg + otp                                #Calcula o valor total recebido 
    print("You have worked overtime:", hours , "Your pay is:", total)                  #Escreve "You have worked overtime:(hours) Your pay is:(total)"
#se o numero de horas nao for maior que 40
else:
    reg = fhours * frate                             #Calcula o valor recebido no total
    print("You have worked regular hours:", hours , "Your pay is:", reg)               #Escreve "You have worked regular hours:(hours) Your pay is:(reg)"