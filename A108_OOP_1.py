# 3. Konstruktor
# a. Alle Klassen verfügen über eine Funktion namens __init__(),
# die immer ausgeführt wird, wenn die Klasse initiiert wird.

# b. Die Funktion __init__() wird erstellt, um Objekteigenschaften
# Werte zuzuweisen oder andere Vorgänge auszuführen, die beim Erstellen
# des Objekts erforderlich sind:

# c. Die __init__()Funktion wird jedes Mal automatisch aufgerufen,
# wenn die Klasse zum Erstellen eines neuen Objekts verwendet wird.

# In Python ist self ein konventioneller Name für den ersten Parameter
# jeder Instanzmethode einer Klasse (einschließlich des Konstruktors __init__).
# Es repräsentiert die aktuelle Instanz des Objekts, das die Methode aufruft. Durch self kann eine Methode auf die Attribute und Methoden des jeweiligen Objekts zugreifen und diese verändern.

# Eine Klasse ist wie  oder eine „Blaupause“ zum Erstellen von Objekten:
class Person:
	def __init__(self, name, age):
		self.name = name
		self.age = age

# 2. Objekt erstellen
p1 = Person("Tom", 44) # Objekt erstellt

print(p1.name)
print(p1.age)

# d. Die Funktion __str__() steuert, was zurückgegeben werden soll, wenn
# das Klassenobjekt als String dargestellt wird
# Wenn die Funktion __str__() nicht gesetzt, wird die String-Darstellung des Objekts zurückgegeben

# ohne: - Wird der Speicherbereich auf das Objekt zurückgegeben
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1) #will ich die ausgabe als john 36 müsste ich print(p1.name,p1.age usw für jeden parameter schreiben)


class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __str__(self):
    return f"{self.name}({self.age})" #(wichtig bei vielen objekten mit vielen parametern, sonst bei print viel schreiben)

p1 = Person("John", 36)

print(p1)


# 4.(Objekt)methoden
# Objekte können auch Methoden enthalten. Methoden in Objekten sind
# Funktionen, die zum Objekt gehören
class Person:
	def __init__(self, name, age):
		self.name = name
		self.age = age

	def mynfunc(self):
		print("Huhu, mein Name ist: " + self.name)

p1 = Person("Gert", 44)
p1.mynfunc()

# 6. Objekteigenschaft ändern - z.B Alter auf 55 gesetzt

p1.age = 55
#print(p1.age)

# 7. Objekteigenschaft löschen
del p1.age
#print(p1.name)
#print(p1.age)


# 8. Ganze Objekt löschen
del p1
# p1.myfunc

# 9. Die pass-Anweisung (wenn nur Klassenkopf erstellen) programm läuft testweise mit der klasse ohne werte etc. 

class Person:
	pass
