largest_so_far=1
print("Before:", largest_so_far)
for number in [11, 16, 1, 83, 122, 0, 4, 123]:
    if number > largest_so_far:
        largest_so_far = number
    print(largest_so_far, number)
print("After:", largest_so_far)
