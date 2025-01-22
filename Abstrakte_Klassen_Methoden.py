'''
Eine abstrakte Klasse ist eine Klasse, die nicht direkt instanziiert werden kann.
Sie dient als Vorlage für andere Klassen und kann sowohl abstrakte Methoden
(Methoden ohne Implementierung) als auch konkrete Methoden (Methoden mit Implementierung)
enthalten. Dies wird in Python über das Modul abc ermöglicht.

Abstrakte Klassen und Methoden:
    • Die abstrakte Klasse Fahrzeug dient als Vorlage für andere Klassen.
    • Die Methode antrieb() ist abstrakt und muss von den Unterklassen implementiert werden.
    • Die Methode beschreibung() ist konkret und kann optional überschrieben werden.
'''

from abc import ABC, abstractmethod

class Fahrzeug(ABC):
    # Abstrakte Methode
    @abstractmethod
    def antrieb(self):
        """
        Diese Methode muss von Unterklassen implementiert werden.
        """
        pass

    # Konkrete Methode
    def beschreibung(self):
        """
        Diese Methode ist in der Basisklasse implementiert und kann von Unterklassen verwendet oder überschrieben werden.
        """
        return "Ich bin ein Fahrzeug."

# Konkrete Unterklasse 1
class Auto(Fahrzeug):
    def antrieb(self):
        """
        Implementierung der abstrakten Methode.
        """
        return "Verbrennungsmotor"

    def beschreibung(self):
        """
        Überschreiben der konkreten Methode.
        """
        return "Ich bin ein Auto mit einem Verbrennungsmotor."

# Konkrete Unterklasse 2
class EAuto(Fahrzeug):
    def antrieb(self):
        """
        Implementierung der abstrakten Methode.
        """
        return "Elektromotor"

# Verwendung
auto = Auto()
e_auto = EAuto()

print(auto.beschreibung())  # Ausgabe: Ich bin ein Auto mit einem Verbrennungsmotor.
print(auto.antrieb())       # Ausgabe: Verbrennungsmotor

print(e_auto.beschreibung())  # Ausgabe: Ich bin ein Fahrzeug.
print(e_auto.antrieb())       # Ausgabe: Elektromotor