sum=0
count=0
for thing in [12, 31, 60, 14, 20, 51, 666, 14, 23, 144, 123]:
    sum= sum + thing
    count= count + 1
    print(sum, thing)
print("After", sum)
print("The loop ran", count, "times.", "All numbers added =", sum, "The average raising is", sum/count)
