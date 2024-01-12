data = "X-DSPAM-Confidence: 0.8475 "

find1 = data.find(":")

find_finaly = data[find1 + 1 : ].strip()
find = float(find_finaly)
print(find)

