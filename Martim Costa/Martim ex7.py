word = "X-DSPAM-Confidence: 0.8475 "
dots = word.find(":")
num = word[dots + 1 :].strip()
fnum = float(num)
print(fnum)
rfnum= round(fnum)
print(rfnum)