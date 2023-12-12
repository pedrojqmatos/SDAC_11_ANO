astr = "hello, jhon"
try:
    istr = int(astr)

except:
    istr = -1

print("first", istr)

astr = "123"
try:
    istr = int(astr)

except:
    istr = -1

print("second", istr)