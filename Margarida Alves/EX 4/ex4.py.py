horas_trabalhadas = input("Number of hours:")
taxa_horaria = input("rate amount:")

try:
    hours = float(horas_trabalhadas)
    rate = float(taxa_horaria)
except ValueError:
    print("Error! You provided an invalid value, please input a valid numeric input")
    exit()

if hours > 40:
    reg = hours * rate
    pay = (hours - 40) * (rate * 1.5)  
    total = reg + pay
    print("You have worked overtime:", hours, "Your pay is:", total)
else:
    reg = hours * rate
    print("You have worked regular hours:", hours, "Your pay is:", reg)