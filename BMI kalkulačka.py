jmeno = 'Zdenek'
vaha = 90
vyska = 1.8

bmi = vaha / vyska ** 2

kategorie = ''
if bmi > 40:
    kategorie = 'těžká obezita'
elif bmi > 30:
    kategorie = 'obezita'
elif bmi > 25:
    kategorie = 'mírná nadváha'
elif bmi > 18.5:
    kategorie = 'zdravá váha'
else:
    kategorie = 'podvýživa'
print(jmeno, "tvé BMI je", str(bmi) + ", což spadá do kategorie", kategorie + ".")