unit=input("What unit do you have mm/cm/dm/m/km/?:")
unit2=input("What unit do you want to change to mm/cm/dm/m/km?:")
if unit2==unit:
    print("Please use two diffrent units")
    quit()
if unit=="mm":
    mm=input("How many mm?:")
if unit=="cm":
    cm==input("How many cm?:")
if unit=="dm":
    dm=input("How many dm?:")
if unit=="m":
    m=input("How many m:?")
if unit=="km":
    km=input("How many km?:")
if unit2=="cm" and unit=="mm":
    cunit=int(mm)/10
    print(mm , "millimeters are " , cunit,  "centimeters")
if unit2=="dm" and unit=="mm":
    cunit=int(mm)/100
    print(mm , "millimeters are " , cunit,  "decimeters")
if unit2=="m" and unit=="mm":
    cunit=int(mm)/1000
    print(mm , "millimeters are " , cunit,  "meters")
if unit2=="km" and unit=="mm":
    cunit=int(mm)/1000000
    print(mm , "millimeters are " , cunit,  "kilometers")
if unit=="cm" and unit2=="mm":
    cunit=int(mm)*10
    print(cm , "centimeters are " , cunit,  "millimeters")
if unit=="cm" and unit2=="dm":
    cunit=int(cm)/10
    print(cm , "centimeters are " , cunit,  "decimeters")
if unit=="cm" and unit2=="m":
    cunit=int(cm)/100
    print(cm , "centimeters are " , cunit,  "meters")
if unit=="cm" and unit2=="km":
    cunit=int(cm)/100000
    print(cm , "centimeters are " , cunit,  "kilometers")
if unit=="dm" and unit2=="mm":
    cunit=int(dm)*100
    print(dm , "decimeters are " , cunit,  "millimeters")
if unit=="dm" and unit2=="cm":
    cunit=int(dm)*10
    print(dm , "decimeters are " , cunit,  "centimeters")
if unit=="dm" and unit2=="m":
    cunit=int(dm)/10
    print(dm , "decimeters are " , cunit,  "meters")
if unit=="dm" and unit2=="km":
    cunit=int(dm)/10000
    print(dm , "decimeters are " , cunit,  "kilometers")
if unit=="m" and unit2=="mm":
    cunit=int(m)*1000
    print(m , "meters are " , cunit,  "millimeters")
if unit=="m" and unit2=="cm":
    cunit=int(m)*100
    print(m , "meters are " , cunit,  "centimeters")
if unit=="m" and unit2=="dm":
    cunit=int(m)*10
    print(m , "meters are " , cunit,  "decimeters")
if unit=="m" and unit2=="km":
    cunit=int(m)/1000
    print(m , "meters are " , cunit,  "kilometers")
if unit=="km" and unit2=="mm":
    cunit=int(km)*1000000
    print(km , "kilometers are " , cunit,  "millimeters")
if unit=="km" and unit2=="cm":
    cunit=int(km)*100000
    print(km , "kilometers are " , cunit,  "centimeters")
if unit=="km" and unit2=="dm":
    cunit=int(km)*10000
    print(km , "kilometers are " , cunit,  "decimeters")
if unit=="km" and unit2=="m":
    cunit=int(km)*1000
    print(km , "kilometers are " , cunit,  "meters")
