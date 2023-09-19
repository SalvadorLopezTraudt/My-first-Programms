lang=input("Which language do you choose en/fr/ge/sp?:")
def greet (lang):
    if lang=="en":
        return "Hello"
    if lang=="fr":
        return "Bonjour"
    if lang=="ge":
        return "Hallo"
    if lang=="sp":
        return "Hola"
if lang=="en":
    print(greet ("en"), "Glenn")
if lang=="fr":
    print(greet ("fr"), "Jaque")
if lang=="ge":
    print(greet ("ge"), "Heinrich")
if lang=="sp":
    print(greet ("sp"), "Jose")
