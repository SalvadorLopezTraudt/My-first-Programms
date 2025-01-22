class Kreis:
    def __init__(self,radius):
        self.radius = radius

    def umfang(self):
        return 3.14 * 2 * self.radius
    def fläche(self):
        return 3.14 * (self.radius ** 2)

try:

    radius = float(input("Gib den Radius des Kreises ein: "))
    Kreis1 = Kreis(radius)

    umfang = Kreis1.umfang()
    print(f"der umfang ist: {umfang:.2f}")

    fläche = Kreis1.fläche()
    print (f"Die fläche ist: {fläche:.2f}")

    print(Kreis1.radius)

except ValueError:
    print("Bitte gib eine gültige Zahl für den Radius ein!")

