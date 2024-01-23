data = "X-DSPAM-Confidence: 0.8475 "

#encontra o :
atpos = data.find(":")
print("Posição dos 2 pontos é:", atpos)

#a data que metemos, a partir do @ adicionamos (+1) porque nao queremos o @ e até ao primeiro " " que ouver
data_final = data[atpos +1 : ].strip()
print("Valor depois dos dois pontos é:", data_final)

#converter em float

fvalue= float (data_final)
print("Valor em float é:", fvalue)

#tries float value with operations
sun = fvalue * 3

