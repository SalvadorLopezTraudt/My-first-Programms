farbe = "rot"

# Variante 1
if farbe == "gruen":
	print(f"Sie fahren ein {farbe}es Auto!")

# Variante 2
if farbe == "gruen":
	print(f"Sie fahren ein {farbe}es Auto!")	
else:
	print(f"Andere Farbe gewählt")
	
# Variante 3
farbe2 = "rot"

if farbe2 == "grün" or farbe2 == "Grün":
    print(f"Sie fahren ein {farbe2}es Auto") 
elif farbe2 == "rot" or farbe2 == "Rot":
    print(f"Sie fahren ein {farbe2}es Auto")
elif farbe2 == "-1":
    print("Sie bekommen ein unlackiertes Auto!")  
else:
    print("Ich fahre nur grüne Autos")