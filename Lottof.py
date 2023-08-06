import random

def lottoschein():
    lotto = set()
    while len(lotto) != 6:
        lotto.add(random.randint(1, 42))
    superzahl = random.randint(1,6)
    lotto.add(superzahl)
    print(f"Deine Lottozahl ist {lotto}")
    return lotto

def gewinner():
    lotto_ziehung = set()
    while len(lotto_ziehung) != 6:
        lotto_ziehung.add(random.randint(1, 42))
    superzahl = random.randint(1,6)
    lotto_ziehung.add(superzahl)
    print(f"Die Zahl ist {lotto_ziehung}")
    return lotto_ziehung

def kontrolle(lotto):
    nummer = range(int(vermogen / 17.5))
    for i in enumerate(nummer):
        if lotto in lotto_ziehung:
            print(f"{i + 1} Sie haben 7 Millionen Franken gewonnen!")
            vermögen += 7000000
            lotto.clear()
            lotto_ziehung.clear()
        else:
            print(f"{i + 1} Vielleicht beim nächsten Mal!")
            vermogen -= 17.5
            lotto.clear()
            lotto_ziehung.clear()
            


vermogen = float(input("Wie hoch ist dein Vermögen"))
while vermogen >= 17.5:
    lotto = lottoschein()
    lotto_ziehung = gewinner()
    kontrolle(vermogen)
