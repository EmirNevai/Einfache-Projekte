import random

vermogen = 0
lotto_ziehung = set()

def lottoschein():
    global vermogen
    lotto = set()
    while len(lotto) != 6:
        lotto.add(random.randint(1, 42))
    superzahl = random.randint(1,6)
    lotto.add(superzahl)
    print(f"Deine Lottozahl ist {lotto}")
    vermogen -= 17.5 
    return lotto

def gewinner():
    global lotto_ziehung
    lotto_ziehung.clear() 
    while len(lotto_ziehung) != 6:
        lotto_ziehung.add(random.randint(1, 42))
    superzahl = random.randint(1,6)
    lotto_ziehung.add(superzahl)
    print(f"Die Zahl ist {lotto_ziehung}")
    return lotto_ziehung

def kontrolle(lotto):
    global vermogen, lotto_ziehung 
    if lotto == lotto_ziehung:
        print("Sie haben 7 Millionen Franken gewonnen!\n")
        vermogen += 7000000
        lotto.clear()
        lotto_ziehung.clear()
        quit()
    else:
        print("Vielleicht beim nächsten Mal!\n")
        lotto.clear()
        lotto_ziehung.clear()

vermogen = float(input("Wie hoch ist dein Vermögen? "))

count = 1
while vermogen >= 17.5:
    print(f"Versuch Nr. {count}")
    lotto = lottoschein()
    lotto_ziehung = gewinner()
    kontrolle(lotto)
    count += 1

print("Dein endgültiges Vermögen ist", vermogen)
