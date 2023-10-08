smallest=None
for value in [9, 22, 400, 1, 12, 0.5, 0.2]:
    if smallest==None:
        smallest=value
    elif value<smallest:
        smallest=value
    print(smallest, value)
print("after", smallest)
