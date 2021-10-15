import random

moznosti = ['kamen', 'nuzky', 'papir']

hrac = input("Zvol svou volbu: ")

pocitac = random.choice(moznosti)

print("Hráč:", hrac)
print("Počítač:", pocitac)

if hrac == 'kamen' or hrac == 'nuzky' or hrac == 'papir':
    if hrac == 'kamen' and pocitac == 'nuzky':
        print("Vyhral jsi!")
    elif hrac == 'nuzky' and pocitac == 'papir':
        print("Vyhral jsi!")
    elif hrac == 'papir' and pocitac == 'kamen':
        print("Vyhral jsi!")
    elif hrac == pocitac:
        print("Nerozhodne")
    else:
        print("Prohral jsi :(")
else:
    print("Neplatna volba")