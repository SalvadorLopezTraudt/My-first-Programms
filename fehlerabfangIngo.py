
#Mit Bedingungen abfangbare Fehler #############################################################################################

# Beispiel 1:
#Überprüfung der Existenz von Schlüsseln in einem Wörterbuch (Dictionary)
wörterbuch = {"a": 1, "b": 2}
schlüssel = "c"
if schlüssel in wörterbuch:
    print(wörterbuch[schlüssel])
else:
    print("Schlüssel ist nicht im Wörterbuch vorhanden.")
    
# Beispiel 2
# Verwendung einer While-Schleife für Eingabevalidierung: 
while True:
    eingabe = input("Geben Sie eine positive Zahl ein: ")
    if eingabe.isdigit() and int(eingabe) > 0:
        print("Gültige Eingabe:", eingabe)
        break
    else:
        print("Ungültige Eingabe. Bitte versuchen Sie es erneut.")

# Fehler, die Try-Except erfordern #################################################################################################

# Beispiel 3
#Dateizugriffsfehler
try:
    with open("nicht_existierende_datei.txt") as f:
        content = f.read()
except FileNotFoundError:
    print("Die Datei wurde nicht gefunden.")

# Beispiel 4
# ValueError (falscher Datentyp):
try:
    zahl = int("keineZahl")
except ValueError:
    print("Konvertierung fehlgeschlagen, da der String keine Zahl darstellt.")

# Beispiel 5
# Dateizugriffsfehler
try:
    with open("nicht_existierende_datei.txt") as f:
        content = f.read()
except FileNotFoundError:
    print("Die Datei wurde nicht gefunden.")

# Beispiel 6
# KeyError:
d = {"a": 1}
try:
    value = d["b"]
except KeyError:
    print("Schlüssel nicht gefunden.")
    
# Beispiel 7
# Syntax Error
code = "print('Hello World'"  # Fehlender schließender Klammer verursacht SyntaxError
try:
    exec(code)
except SyntaxError as e:
    print(f"SyntaxError abgefangen: {e}")
# Beispiel 8
# IOError
try:
    with open("nicht_existierende_datei.txt", "r") as file:
        data = file.read()
except IOError as e:
    print(f"IOError abgefangen: {e}")

# Beispiel 9
# Runtime Error
def fehlerhafte_funktion():
    raise RuntimeError("Ein Laufzeitfehler ist aufgetreten")

try:
    fehlerhafte_funktion()
except RuntimeError as e:
    print(f"RuntimeError abgefangen: {e}")


# Können unterschiedliche Fehler auftreten, ist es sinnvoll, sich die Fehlermeldung des Systems ausgeben zu lassen wie folgt: #####
# Mit diesem Ansatz fängst man alle Fehler ab und kann sie im Detail mit e untersuchen
# Wenn man mögliche Fehler weiß, aber besser Fehler mit spezifischer Methode abfangen

# Beispiel 10
print("Bitte geben Sie eine ganze Zahl ein")
z = input()
try:
    zahl = int(z)
    print(f"Sie haben die ganze Zahl {zahl} eingegeben")
except Exception as e:
    print(e)
    



# Try-Except für Schleife mit Eingabewiederholung verwenden ########################################################################

# Beispiel 11
# While-Schleife Verwendung für Eingabewiederholung: 
while True:
    print("Bitte geben Sie eine ganze Zahl ein")
    z = input()
    try:
        zahl = int(z)
        print(f"Sie haben die ganze Zahl {zahl} eingegeben")
        break
    except:
        print("Fehler bei Umwandlung der Eingabe")

# Beispiel 12
# Schleife mit 3 Versuchen: 
for versuch in range(1,4):
        # 10: Eingabe
        try:
            print("Bitte Lösungsvorschlag eingeben:")
            zahl = int(input())
        except:
            # Umwandlung war nicht erfolgreich
            print("Sie haben keine ganze Zahl eingegeben")
            # Schleife unmittelbar fortsetzen
            continue





