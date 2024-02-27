count = 0
total = 0


while True:
        numb = input ('Enter a number: ')
        if numb == 'done':
            
            break
try:
    fnumb = float(numb)
    total += fnumb
    count += 1

except ValueError: 
    print ('invalid input !!!')

