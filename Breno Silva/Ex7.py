word = "X-DSPAM-Confidence: 0.8475 "
pos = word.find(":")

pos_2 = word.find("5", pos)

r = word[pos + 2 : pos_2 + 1]

word_2 = float(r) * 2
final = round(word_2)
print("final result is: ", final)