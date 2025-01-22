'''
Python hat keine direkten Interfaces wie andere Sprachen,
aber man kann sie durch abstrakte Klassen simulieren:

Ein Interface ist ein reines Vertragskonzept: Es legt fest,
welche Methoden eine Klasse implementieren muss, enthält
jedoch keine Implementierung. In Python simulieren wir
Interfaces mit abstrakten Klassen, die ausschließlich
abstrakte Methoden enthalten.
'''
from abc import ABC, abstractmethod

class Zeichnung(ABC):
    @abstractmethod
    def zeichnen(self):
        pass

class Kreis(Zeichnung):
    def zeichnen(self):
        return "Kreis zeichnen"

class Rechteck(Zeichnung):
    def zeichnen(self):
        return "Rechteck zeichnen"

# Beispiel:
kreis = Kreis()
rechteck = Rechteck()
print(kreis.zeichnen())       # Ausgabe: Kreis zeichnen
print(rechteck.zeichnen())    # Ausgabe: Rechteck zeichnen