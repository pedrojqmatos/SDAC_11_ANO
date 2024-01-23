data = "X-DSPAM-Confidence: 0.8475"
atpos = data.find(":")

host = data[atpos + 1 :].lstrip()

out = float(host)
print(out)

arredondado= round(float (out), 2)
print (arredondado)
