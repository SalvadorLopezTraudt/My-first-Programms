''' ##############################################################################################
Wichtig:
1. Eine Aufgabe pro Funktion!
   z.B. Eingabe, Verarbeitung, Ausgabe jeweils in eine Funktion auslagern
   
2. Trennung von Funktionsdefinition und -aufruf: Der Name eines Arguments,
   das beim Funktionsaufruf übergeben wird, muss nicht mit dem Namen des
   Parameters im Funktionskopf übereinstimmen (Siehe Beispiel 2)
   Stichwort: Wiederverwendbarkeit, Namenskonflikte
'''

# Beispiel 1 - Funktionsaufruf ohne Parameter, ohne Rückgabewert #################################
print("Guten Morgen")

def begrueßung():
	print("Schlecht geschlafen")
	
# Funktion aufrufen
begrueßung()

input("\nEnter drücken\n") # Pause zwischen den Beispielen


# Beispiel 2 - Funktionsaufruf mit Parameter, ohne Rückgabewert ###################################

# Funktion mit unterschiedlichen Namen im Funktionskopf
# gegenüber den Argumenten im Funktionsauruf
def persoenliche_begruessung(nachname, vorname):
	print(f"Hallo {vorname} {nachname}, wie gehts? ")

# Funktion mit identischen Namen im Funktionsaufruf
# sowie im Funktionskopf
def persoenliche_begruessung_2(name, vorname):
	print(f"Hallo {vorname} {name}, immer noch alles klar? ")

# Hauptprogramm
name = input("Name eingeben: ")
vorname = input("Vorname eingeben: ")

# Funktionsauf beider Funktionen - mit Parametern
persoenliche_begruessung(name, vorname)
persoenliche_begruessung_2(name, vorname)

input("\nEnter drücken\n") # Pause zwischen den Beispielen


# Beispiel 3 - Funktionsaufruf ohne Parameter, mit Rückgabewert ###################################

print("Guten Morgen")

def bekomme_zahl():
	wert = input("Zahl eingeben: ")
	return wert

# Funktionsaufruf sowie Funktionsrückgabewert in Variable "zahl" speichern
zahl = bekomme_zahl()

print(f"Zahl lautet: {zahl}")

input("\nEnter drücken\n") # Pause zwischen den Beispielen


# Beispiel 4 - Funktionsaufruf mit Parameter, mit Rückgabewert #####################################

def addiere(a, b):
	# c = a + b ; return c
	return a + b

eine_zahl = int(input("Erste Zahl eingeben: "))
zweite_zahl = int(input("Noch ne Zahl eingeben: "))

ergebnis = addiere(eine_zahl, zweite_zahl)

print(ergebnis)

