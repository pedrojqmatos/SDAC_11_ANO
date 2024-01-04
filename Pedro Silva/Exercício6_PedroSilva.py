largest_so_far = -1
print("before:", largest_so_far)
for num in [3, 41, 12, 9, 74, 15]:
    if num > largest_so_far:
        largest_so_far = num
    print(largest_so_far, num)
print("after:", largest_so_far)
