for g in range(1,76):
    if g % 5 ==0 and g % 7 ==0:
        print("Ping Pong") and print (g)
    elif g % 5 == 0:
        print("ping")
    elif g % 7 == 0:
        print("Pong")
    elif g % 5 !=0 and g % 7 !=0:
        print(g)

