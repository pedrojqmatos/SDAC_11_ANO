data = "X-DSPAM-Confidence: 0.8475"
atpos = data.find(":")

host = data[atpos + 1 :].lstrip()

out = float(host)
sum = out * 12
print(out)

print("The sum result is", sum, "The round value is", round(sum))