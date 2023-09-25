sunday=input("Did you work on sunday yes/no?:")
if sunday=="yes":
    sundayh=input("How many hours on sunday?:")
if sunday=="no":
    sundayh=0
hours=input("Enter your regular worked hours:")
rate=input("Enter your rate of pay:")
fhours=float(hours)
frate=float(rate)
fsundayh=float(sundayh)
spay=(fsundayh*frate)+(fsundayh)*(frate*0.5)
if fhours > 40 and sunday=="yes":
    print("Overtime and sunday bonus:")
    reg=fhours*frate
    othours=(fhours-40)*(frate*0.5)
    pay=reg+othours+spay
    print("Pay:", pay)
elif fhours < 40 and sunday=="yes":
    print("Regular workshift and sunday bonus:")
    reg=fhours*frate
    pay=reg+spay
    print("Pay:", pay)
elif fhours > 40 and sunday=="no":
    print("Overtime:")
    reg=fhour*frate
    othours=(fhours-40)*(frate*0.5)
    pay=reg+othours
    print("Pay:", pay)
else:
    print("Reduced workshift:")
    pay=fhours*frate
    print("Pay:", pay)
