hours=input("Enter hours:")
rate=input("Enter rate:")
try:
    fhours=float(hours)
    frate=float(rate)
except:
    print("Please use a numeric input")
    quit()
if fhours > 40:
    print("Overtime:")
    reg=fhours*frate
    othours=(fhours-40)*(frate*0.5)
    pay=reg+othours
    print("Pay:", pay)
else:
    print("Regular:")
    pay=(fhours)*(frate)
    print("Pay:", pay)
