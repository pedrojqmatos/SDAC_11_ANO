def calcular_salario(remuneracao_por_hora, horas_trabalhadas):
    horas_normais = min(horas_trabalhadas, 40)
    horas_extra = max(horas_trabalhadas - 40, 0)
    salario_normal = horas_normais * remuneracao_por_hora
    salario_extra = horas_extra *   1.5 * remuneracao_por_hora

    salario_total = float (salario_normal )* float( salario_extra)
    return salario_total

remuneracao_por_hora = float(input("Diga a remuneração por hora: "))
horas_trabalhadas = float(input("Diga o número de horas feitas: "))

salario = calcular_salario(remuneracao_por_hora, horas_trabalhadas)
print(f"O remuneração total é: {salario}")


