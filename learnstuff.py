Brut =float(input("Bruttolohn in Euro?:"))
Ste = 30
Soli = 5
KV = 62
RV = 86
AV = 26

Net1 = (Brut) * (Ste + Soli + KV + RV + AV )
Net2 = (Brut) - (Net1)

print("Der Nettolohn beträgt bei" ,Brut, " Euro Bruttolohn" ,Net2, "Euro")

MB = float(input("Wie viel MB?:"))
Kbs = float(input("Wie viel Kb/s?:"))

Speed = MB * 1000 / Kbs
print("Es dauert" ,Speed, "sek zum übertragen")
Speedh =  MB * 1000 / Kbs / 60
print("Es dauert" ,Speedh, "std zum übertragen")


anzahl = 6
i = 0
summe = 0
while i < anzahl :
    print("geben sie die {0}. temperatur in °C ein:".format(i+1))
    temperatur = float(input())
    summe = summe + temperatur
    i += 1
durchschnitt = summe / anzahl
print("Die durchschnittstemperatur beträgt {0:.2f} °C".format(durchschnitt))


farbe = input("Farbe eingeben:")
print(farbe)

farbe =(input("Farbe eingeben:"))
print(farbe)