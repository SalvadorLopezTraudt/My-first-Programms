pulse = int(input("Enter your current heartrate in a 15sec interval: "))  # Direkt in int umwandeln
activity = input("Have you done something exhausting? (yes/no): ").strip().lower()  # Eingabe standardisieren

heartrate = pulse * 4  # Korrekte Berechnung

if heartrate < 60:
    print("Your heartrate is too low, you should seek a doctor and do an EKG.")

elif heartrate > 100:
    if activity == "yes":
        print("You should do a little pause, do not overdo it.")
    elif activity == "no":
        print("Your heartrate is too high, you might have tachycardia. You should seek a doctor for an EKG.")
    else:
        print("Invalid input for activity. Please enter 'yes' or 'no'.")
