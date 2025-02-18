# Umrechnungswerte zur Basiseinheit (Meter)
conversion_factors = {
    "mm": 0.001,
    "cm": 0.01,
    "dm": 0.1,
    "m": 1,
    "km": 1000
}

# Eingabe der Einheiten
unit = input("What unit do you have (mm/cm/dm/m/km)?: ").lower()
unit2 = input("What unit do you want to convert to (mm/cm/dm/m/km)?: ").lower()

# Überprüfung, ob die Einheiten gültig sind
if unit not in conversion_factors or unit2 not in conversion_factors:
    print("Invalid unit. Please use mm, cm, dm, m, or km.")
    exit()

# Eingabe des Zahlenwerts mit Fehlerbehandlung
try:
    value = float(input(f"How many {unit}?: "))
except ValueError:
    print("Error: Please enter a valid number!")
    exit()

# Umrechnung zur Basiseinheit (Meter) und dann zur Ziel-Einheit
value_in_meters = value * conversion_factors[unit]  
converted_value = value_in_meters / conversion_factors[unit2]

# Ausgabe des Ergebnisses
print(f"{value} {unit} are {converted_value:.5f} {unit2}")
