def pagamento(horas_normais, taxa_horaria):
   
    if horas_normais > 40:
        horas_extras = horas_normais - 40
        horas_normais = 40
    else:
        horas_extras = 0
    
    salario = horas_normais * renumeracao_horaria + 1.5 * horas_extras * renumeracao_horaria

    return salario

horas_normais_trabalhadas = float(input("Informe as horas normais trabalhadas: "))
renumeracao_horaria = float(input("Informe a taxa horária: "))

salario_total = pagamento(horas_normais_trabalhadas, renumeracao_horaria)

print(f"O salário total é: {salario_total}")
