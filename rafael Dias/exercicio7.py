str = "X-DSPAM-Confidence: 0.8475 "
position = str.find(":")
print("colon positionis:", position)
extracted_str = str[position +1 :]
print("Value after the colon is:", extracted_str)
float_num = float(extracted_str)
print("Floating value is:", float_num)
sum = float_num * 12
print("The sum result is", sum, "The round value is", round(sum))