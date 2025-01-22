import csv
 
# Erstellen und Schreiben in die CSV-Datei
dateiname = "beispiel.csv"
 
 
with open(dateiname, mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["name", "alter", "stadt"])
 
# Daten, die in die CSV-Datei geschrieben werden sollen
while True:
    name = input("Gib den Namen ein: ")
    alter = input("Gib das Alter ein: ")
    stadt = input("Gib die Stadt ein: ")

    with open(dateiname, mode="a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow([name, alter, stadt])
    weiter = input("Weiterer Datensatz ? ja/nein: ") .strip().lower()
    if weiter != "ja":
        break
 
 
print(f"Die Datei {dateiname} wurde erfolgreich erstellt und gespeichert.")
