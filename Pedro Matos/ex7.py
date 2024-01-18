str = "X-DSPAM-Confidence: 0.8475 "

#Finds colon position
cpos = str.find(":")
print("Colon position is:", cpos)

#adds 1 to the current colon position and strips spaces
npos = str[cpos + 1 :].strip()
print("Value after the colon is:", npos)

#converts the value position into float
fvalue = float(npos)
print("Floating value is:", fvalue)

#tries float value with operations
sum = fvalue * 12
print("The sum result is", sum, "The round value is", round(sum))
