data = "X-DSPAM-Confidence: 0.8475 "

find2pontos = data.find(":")         # Procura ":" em data

d2pontos = data[find2pontos + 1 : ]  # Guarda em string a partir dos ":" até ao fim da frase 

without_space = d2pontos.strip()     # Retira os espaços presentes em d2pontos

fnumb = float(without_space)         # converte a string em float

# Conta de dividir
conta = fnumb / 2                    # Realiza a conta
round_conta = round(conta, 2)        # Arredondao valor de conta a duas casas decimais
print(round_conta)                   # Escreve o resultado arredondado
