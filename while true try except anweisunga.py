while True:
    try:
        U =float(input("Spannung in Volt:"))
        if U==0:
            print("Darf nicht 0 sein")
            continue
        
        I =float(input("Stromstärke in Ampere:"))
        if I==0:
            print("Darf nicht 0 sein")
            continue
        
 
        R = U / I
        P = U * I

        print("Der elek. Widerstand ist:" ,R, "Ohm.") 
        print("Die elek. Wirkleistung ist: {0:.2f} Watt". format(P))
        break

    except ValueError:
        print("Zahl eingeben")
        

