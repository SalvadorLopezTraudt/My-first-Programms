def vergleiche_temp(temp): #temp dient nur als platzhalter und wird später durch durchschnitt ersetzt
    langjahr_mittel = 18.23
    if temp >= langjahr_mittel:
        if temp > langjahr_mittel:
            return "Die Temp. liegt über dem langjährigen Mittel"
        else:
            return "Die Temp. entspricht dem langjährigen Mittel"
    else:
        return "Die Temp. liegt unter dem langjährigen Mittel"
    
def main():
    try:
        print("Programm zur Berechnung einer Durchschnittstemp. \n")
        print("Geben Sie bitte drei Temp.Werte in °C ein")
        temp1 = float(input("1. Wert:"))
        temp2 = float(input("2. Wert:"))
        temp3 = float(input("3. Wert:"))
        durchschnitt = (temp1 + temp2 + temp3) / 3
        print("Sie haben folgende Temp. eingegeben {0} °C, {1} °C, {2} °C".format(temp1, temp2, temp3))
        print("Die Durchschnitttemp. beträgt: {0:.2f} °C".format(durchschnitt))
        text = vergleiche_temp(durchschnitt)
        print(text)
    except Exception as e:
        print("Fehler: \n" + e.args[0])

main()