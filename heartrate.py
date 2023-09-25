pulse=input("Enter your current heartrate in  a 15sec interval:")
activity=input("Have you done something exhausting yes/no?:")
heartrate=(pulse)*4
iheartrate=int(heartrate)
too_low=iheartrate < 60
too_high=iheartrate > 100
if iheartrate < 60:
    print("Your heartrate is too low, you should seek a doctor and do an EKG")
if iheartrate > 100 and activity=="yes":
    print("You should do a little pause, do not overdo it")
if iheartrate > 100 and activity=="no":
    print("Your heartrate is too high, you might have tachycardia, you should seek a doctor for an EKG")
