friends = ['Amanda','Louis','Jhon','Peter','Megan','Francis','Kyle']
friends.sort()
print(friends, friends[0])

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

numbers = [1,2,4,6,3,5,8,7,9,10,13,11,12,14,51,64,3,5,]
numbers.sort()
print(len(numbers))
print(max(numbers))
print(min(numbers))
print(sum(numbers))
print(round (sum(numbers)), (numbers[0]))

#----------------------------------------------------------------------------
#inicia uma lista vazia
numlist = list()
while True :
    #preenche a lista co numeros imputados
    inp = input("enter a number")
    if inp == "done":
        break
    try :
        value = float(inp)
    except :
        print('Insert a valid number')
        continue
    numlist.append(value)
    avarage = sum(numlist) / len(numlist)
print('Yhe avarage of the list is', numlist, avarage,)




