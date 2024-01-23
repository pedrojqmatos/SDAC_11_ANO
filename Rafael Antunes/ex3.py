Ht = input("Nº de horas trabalhadas ")
Vph = input("Valor por Hora ")

pagamento = float(Ht)*float(Vph)

Vpham= float(Ht)-40
Vphe = float(Vpham)*1.5 + 40*float(Vph)

if float(Ht) > 40:
    print("Totala a ser pago", Vphe)

if float (Ht) <= 40:
    print("Total a ser pago", pagamento)