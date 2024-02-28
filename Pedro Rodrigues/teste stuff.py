stuff = {'peter': 11, 'mary': 43, 'jane': 22}
print(list(stuff))
print(list(stuff.keys()))
print(list(stuff.values()))
print(list(stuff.items()))

for name, age in stuff.items() :
    print(name, age)