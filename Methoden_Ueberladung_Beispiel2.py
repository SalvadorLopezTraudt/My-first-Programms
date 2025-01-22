'''
    • Überschreiben erlaubt es, das Verhalten der Basisklasse individuell für jede Unterklasse anzupassen.
    • Polymorphismus: Der Code funktioniert unabhängig vom konkreten Tiertyp.
'''
class Tier:
    def laut_machen(self):
        return "Ein generisches Tiergeräusch."

class Hund(Tier):
    def laut_machen(self):
        return "Wuff!"

class Katze(Tier):
    def laut_machen(self):
        return "Miau!"

# Verwendung:
def tier_geraeusch(tier: Tier):
    print(tier.laut_machen())

hund = Hund()
katze = Katze()

tier_geraeusch(hund)  # Ausgabe: Wuff!
tier_geraeusch(katze) # Ausgabe: Miau!