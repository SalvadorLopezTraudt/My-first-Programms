from abc import ABC, abstractmethod

class Fahrzeug(ABC):
    @abstractmethod
    def antrieb(self):
        pass

    def beschreibung(self):
        return "Ich bin ein Fahrzeug."

class Auto(Fahrzeug):
    def antrieb(self):
        return "Verbrennungsmotor"

class EAuto(Fahrzeug):
    def antrieb(self):
        return "Elektromotor"

# Verwendung:
def drucke_antrieb(fahrzeug: Fahrzeug):
    print(f"Antrieb: {fahrzeug.antrieb()}")

auto = Auto()
e_auto = EAuto()

drucke_antrieb(auto)   # Ausgabe: Antrieb: Verbrennungsmotor
drucke_antrieb(e_auto) # Ausgabe: Antrieb: Elektromotor