# Python-Vererbung

# a. Durch Vererbung können wir eine Klasse definieren, die alle Methoden und Eigenschaften einer
#    anderen Klasse erbt
# b. Die übergeordnete Klasse ist die Klasse, von der geerbt wird, auch
#    Basisklasse genannt.
# c. Eine untergeordnete Klasse ist die Klasse, die von einer anderen
#    Klasse erbt, auch abgeleitete Klasse genannt.
# 10.Erstellen einer übergeordneten Klasse (Jede Klasse kann übergeordnete Klasse sein)
class Person:
	def __init__(self, fname, lname):
		self.firstname = fname
		self.lastname = lname

	def printname(self):
		print(self.firstname, self.lastname)

#Objekt erstellen und Name ausgeben
x = Person("Dirk", "Bach")
x.printname()

# 11. Erstellen einer untergeordneten Klasse
# Um eine Klasse zu erstellen, die die Funktionalität einer anderen Klasse erbt, sendet
# man beim Erstellen der untergeordneten Klasse die übergeordnete Klasse als Parameter:
class Student(Person):
	pass

x = Student("Hansi", "Aretz") # Zweites Objekt in der Unterklasse Student erstellt
x.printname()

# 12.Funktion __init__() hinzufügen
# Bisher haben wir eine untergeordnete Klasse erstellt, die die Eigenschaften und
# Methoden ihrer übergeordneten Klasse erbt.
# Hinzufügen von __init__() bewirkt, dass untergeordnete Klasse nicht mehr die __init__()Funktion der übergeordneten erbt
# Die Funktion des untergeordneten Elements überschreibt die Vererbung der __init__()Funktion des übergeordneten Elements.
class Student(Person):
	def __init__(self, fname, lname): # --> __init__
		pass #properties hinzufügen

# 13. Funktion __init__() der übergeordneten hinzufügen
# Um Vererbung der übergeordneten __init__() Fkt beibehalten, den übergeordneten __init__()Fkt Aufruf hinzufügen
class Person:
	def __init__(self, fname, lname):
		self.firstname = fname
		self.lastname = lname

	def printname(self):
		print(self.firstname, self.lastname)

class Student(Person):
	def __init__(self, fname, lname):
		Person.__init__(self, fname, lname) # -->  Person.__init__(...

x = Student("Gunter", "Gabriel")
x.printname()

'''
Warum __init__ in der Subklasse hinzufügen?
Die __init__-Methode wird genutzt, um Objekte bei ihrer Erstellung zu initialisieren. Wenn du in der Subklasse eine eigene __init__-Methode definierst, überschreibst du die der Basisklasse. Das erlaubt dir, die Initialisierung an die spezifischen Bedürfnisse der Subklasse anzupassen.

Szenario 1: Zusätzliche Eigenschaften in der Subklasse
Beispiel: Wenn ein Student zusätzlich zu Vor- und Nachnamen auch eine Matrikelnummer (oder andere spezifische Eigenschaften) haben soll, benötigst du eine eigene __init__-Methode:


class Student(Person):
    def __init__(self, fname, lname, student_id):
        # Eigenschaften aus der Basisklasse initialisieren
        super().__init__(fname, lname)  # Ruft den Konstruktor der Basisklasse auf
        # Zusätzliche Eigenschaften der Subklasse
        self.student_id = student_id

    def print_student(self):
        print(f"{self.firstname} {self.lastname}, Matrikelnummer: {self.student_id}")

# Test
x = Student("Hansi", "Aretz", "123456")
x.printname()  # Geerbte Methode
x.print_student()  # Methode der Subklasse
Erklärung:
super().__init__(fname, lname) ruft die __init__-Methode der Basisklasse (Person) auf, sodass Vor- und Nachname initialisiert werden.
Die Subklasse ergänzt eine spezifische Eigenschaft (student_id) und eine neue Methode (print_student).
Szenario 2: Angepasster Initialisierungsprozess
Beispiel: Wenn die Subklasse eine spezielle Art der Initialisierung benötigt, kannst du die __init__-Methode vollständig neu definieren. Beispielsweise sollen Studierende direkt mit einem vollständigen Namen (statt Vor- und Nachnamen getrennt) initialisiert werden:


class Student(Person):
    def __init__(self, fullname, student_id):
        # Den vollständigen Namen aufteilen
        fname, lname = fullname.split(" ", 1)
        super().__init__(fname, lname)
        self.student_id = student_id

# Test
x = Student("Hansi Aretz", "123456")
x.printname()
Erklärung:
Die Subklasse erhält als Argument den vollständigen Namen und verarbeitet ihn entsprechend.
Die Basisklasse wird trotzdem genutzt, um Vor- und Nachnamen zu initialisieren.
Wann sollte man keine eigene __init__-Methode in der Subklasse nutzen?
Wenn die Subklasse keinerlei zusätzliche Eigenschaften oder einen speziellen Initialisierungsprozess benötigt, kannst du die __init__-Methode der Basisklasse unverändert erben. Das war der Fall in deinem ursprünglichen Beispiel mit:


class Student(Person):
    pass
Das spart Code und sorgt dafür, dass die Subklasse automatisch alle Eigenschaften und Methoden der Basisklasse übernimmt.

Fazit
Das Hinzufügen einer __init__-Methode in einer Subklasse macht Sinn:

1.
Wenn die Subklasse eigene Eigenschaften oder Methoden benötigt.

2.
Wenn der Initialisierungsprozess von dem der Basisklasse abweicht.
Falls die Subklasse die Basisklasse unverändert übernimmt, kannst du auf die eigene __init__-Methode verzichten.
'''


# 14. super()Funktion, die untergeordnete Klasse erbt alle Methoden und Eigenschaften von übergeordneten Klasse
class Person:
	def __init__(self, fname, lname):
		self.firstname = fname
		self.lastname = lname

	def printname(self):
		print(self.firstname, self.lastname)

class Student(Person):
	def __init__(self, fname, lname):
		super().__init__(fname, lname)

x = Student("Emil", "Nolde")
x.printname()

# 15. Eigenschaften zur Unterfunktion hinzufügen
#     year Parameter hinzufügen, beim erstellen des Objektes mit übergeben
class Person:
	def __init__(self, fname, lname):
		self.firstname = fname
		self.lastname = lname

	def printname(self):
		print(self.firstname, self.lastname)

class Student(Person):
	def __init__(self, fname, lname, year):
		super().__init__(fname, lname)
		self.graduationyear = year

x = Student("Hans", "Hirsch", 2019)
print(x.graduationyear) # Ausgabe des Jahres

# 16. Methoden hinzufügen - zur Kindklasse
class Person:
	def __init__(self, fname, lname):
		self.firstname = fname
		self.lastname = lname

	def printname(self):
		print(self.firstname, self.lastname)

class Student(Person):
	def __init__(self, fname, lname, year):
		super().__init__(fname, lname)
		self.graduationyear = year

	def welcome(self):
		print("Johde Dach", self.firstname, self.lastname, "in de Klassruum", self.graduationyear)

x = Student("Mikey", "Olsen", 2019)
x.welcome()
