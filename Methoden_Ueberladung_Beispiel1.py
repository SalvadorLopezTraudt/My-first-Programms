'''
Methodenüberladung (in Python mit optionalen Parametern simuliert) ist nützlich,
wenn eine Methode in verschiedenen Kontexten unterschiedlich funktionieren soll,
abhängig von der Anzahl oder Art der übergebenen Argumente.

Methodenüberschreibung ist nützlich, wenn eine Methode der Basisklasse in einer
abgeleiteten Klasse spezifisches Verhalten erhalten soll. Sie wird häufig im
Zusammenhang mit Polymorphismus verwendet.
'''
class Rechner:
    def addiere(self, a, b=0, c=0):
        return a + b + c

# Verwendung:
rechner = Rechner()
print(rechner.addiere(2, 3))       # Ausgabe: 5
print(rechner.addiere(2, 3, 4))    # Ausgabe: 9