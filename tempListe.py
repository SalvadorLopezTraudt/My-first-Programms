anzahl = 6

i = 0

summe = 0

temperaturen = []

while i < anzahl:
    print("Geben sie die {0}. temperatur in °C ein:".format(i+1))
    eingabe = float(input())
    temperaturen.append(eingabe)
    summe = summe + temperaturen[i]
    i += 1
durchschnitt = summe / anzahl

print("Der Durchschnitt beträgt {0} °C".format(durchschnitt))
print("Hier ist die Liste der eingegebenen Werte {0}".format(temperaturen))