import re
valid_input = False
nicht_verstanden = "Das habe ich nicht verstanden"

vermögen = 0
inventar = []
global beute_wohnzimmer
global beute_badezimmer
global beute_kinderzimmer
global beute_schlafzimmer
beute_wohnzimmer = ["Silbernen Besteckset", "einen teuren Wein"]
beute_kinderzimmer = ["Ipad", "Sparschwein"]
beute_badezimmer = ["Parfüm"]
beute_schlafzimmer = ["Geld", "IWC Uhr", "Goldkette", "Goldarmband"]
beute_schlaflen = len(beute_schlafzimmer)
beute_kinderlen = len(beute_kinderzimmer)
beute_badelen = len(beute_badezimmer)
beute_wohnlen = len(beute_wohnzimmer)
def art():
    while not valid_input:
        art = input("Du kannst entweder die Tür oder das Fenster nutzen um einzubrechen? ")
        if re.match(r"(d|D)?i?e?\s*(h|H)?a?u?s?(t|T)ür", art):
            tur()
        elif re.match(r"(d|D)?a?s?\s*(F|f)enster", art):
            fenster()
        else:
            print(nicht_verstanden)
#Von wo er einbrechen will.
def tur():
    while not valid_input:
        werkzeug = input("Willst du ein Lockpick oder ein Brecheisen benutzen? ")
        if re.match(r"(l|L)ockpick", werkzeug):
            lockpick()
        elif re.match(r"(b|B)recheisen", werkzeug):
            input("Benutze lieber ein Lockpick")
            tur()
        else:
            print(nicht_verstanden)
def fenster():
    input("Du stehst vor dem Fenster")
    werkzeug = input("Du hast Lockpick und ein Brecheisen zur Verfügung.")
    if re.match(r"(b|B)recheisen", werkzeug):
        input("Du hast ausversehen das Fenster zerschmetert. Drücke auf eine beliebige Taste um zu fliehen")
        beenden()
    elif re.match(r"(L|l)ockpick", werkzeug):
        input("Ein Schattenläufer kennt seine Wekzeuge und er weiss wo man, was einsetzt.") 
        beenden()
    else:
        print(nicht_verstanden)

#Fragt welches Werkzeug er dafür brauchen will.
def lockpick():
    while not valid_input:
        antwort = int(input("Was ergibt 1 + 1? "))
        if antwort == 2:
            geknackt()
        else:
            beenden()
def geknackt():
    input("Du hast die Tür geknackt.")
    wohnzimmer_entscheidung()
# wenn mein vor einem Zimmer oder vor mehreren Zimmern eine Entscheidung treffen muss
def wohnzimmer_entscheidung():
    while not valid_input:
        was_tun = input("Du bist jetzt im Flur. Links von dir ist das Wohnzimmer mit der offenen Küche. Willst links laufen oder weiter nach vorne? ")
        if re.match(r"(l|L)inks", was_tun):
            wohnzimmer()
        elif re.match(r"(v|V)orne", was_tun):
            wohnzimmer_vorne()
        else:
            print(nicht_verstanden)

def wohnzimmer_vorne():
    input("Du läufst gerade aus.")
    input("Der Flur geht nach rechts weiter")
    kinderzimmer_entscheidung()

def kinderzimmer_entscheidung():
    was_tun = input("Links von dir ist das Kinderzimmer. Links oder nach vorne? ")
    if re.match(r"(l|L)inks", was_tun):
         kinderzimmer()
    elif re.match(r"(v|V)orne", was_tun):
        badezimmer_entscheidung()
    else:
        print(nicht_verstanden)

def badezimmer_entscheidung():
    while not valid_input:
        was_tun = input("Recht ist das Schlafzimmer und links von dir ist das Badezimmer. Links oder rechts? ")  
        if re.match(r"(l|L)inks", was_tun):
            badezimmer()
        elif re.match(r"(r|R)echts", was_tun):
            schlafzimmer()
        else:
            print(nicht_verstanden)
#Fragt was man in dem Zimmer tun will
def wohnzimmer():
    input("Du befindest dich im Wohnzimmer.")
    klauen_gehen = input("Willst du das Zimmer durchsuchen oder verlassen? ")
    if klauen_gehen == "klauen" or "Klauen":
        klauen_wohnzimmer()
    elif re.match(r"(v|V)erlassen", klauen_gehen):
        wohnzimmer_entscheidung()
    else:
        print(nicht_verstanden)

def kinderzimmer():
    input("Du bist im Kinderzimmer.")
    klauen_gehen = input("Willst du das Zimmer durchsuchen oder verlassen? ")
    if klauen_gehen == "klauen" or "Klauen":
        klauen_kinderzimmer()
    elif re.match(r"(v|V)erlassen", klauen_gehen):
        kinderzimmer_entscheidung()
    else:
        print(nicht_verstanden)

def badezimmer():
    input("Du befindest dich im Badezimmer.")
    while not valid_input:
        klauen_gehen = input("Willst du das Zimmer durchsuchen oder verlassen? ")
        if re.match(r"(d|D)urchsuchen", klauen_gehen):
            klauen_badezimmer()
        elif re.match(r"(v|V)erlassen", klauen_gehen):
            kinderzimmer_entscheidung()
        else:
            print(nicht_verstanden)

def schlafzimmer():  
    input("Du befindest dich im Schlafzimmer.")
    while not valid_input:
        klauen_gehen = input("Willst du das Zimmer durchsuchen oder verlassen? ")
        if re.match(r"(d|D)urchsuchen", klauen_gehen):
            klauen_schlafzimmer()
        elif re.match(r"(v|V)erlassen", klauen_gehen):
            kinderzimmer_entscheidung()
        else:
            print(nicht_verstanden)
#Wenn man klauen auswählt, kontrolliert es ob es noch eine Beute hat
def klauen_wohnzimmer():
    global inventar
    global beute_wohnzimmer
    if beute_wohnlen != 0:
        input("Du kontrollierst die Schubladen...")
        inventar += beute_wohnzimmer
        input("Du hast " + ", ".join(beute_wohnzimmer) + " gefunden.")
        beute_wohnzimmer = []
    else:
        input("Da gibt es nichts mehr zum Klauen")

def klauen_kinderzimmer():
    global inventar
    global beute_kinderzimmer
    if beute_kinderlen != 0:
        input("Du durchsuchst das Zimmer...")
        inventar += beute_kinderzimmer
        beute_kinderzimmer = []
        input("Du hast " + ",".join(beute_kinderzimmer) + " gefunden.")
        kinderzimmer_entscheidung()
    else:
        input("Da gibt es nichts mehr zum Klauen")
        kinderzimmer_entscheidung()

def klauen_badezimmer():
    global beute_badezimmer
    global inventar
    if beute_badelen !=0:
        input("Du durchsuchst das Zimmer...")
        inventar += beute_badezimmer
        input("Du hast ein " + ", ".join(beute_badezimmer) + " gefunden.")
        beute_badezimmer = []
        badezimmer_entscheidung()
    else:
        input("Da gibt es nichts mehr zu klauen")
        klauen_badezimmer()

def klauen_schlafzimmer():
    global beute_schlafzimmer
    global inventar
    if beute_schlaflen != 0:
        input("Du durchsuchst das Zimmer...")
        inventar += beute_schlafzimmer
        input("Du hast ein " + ", ".join(beute_schlafzimmer) + " gefunden.")
        beute_schlafzimmer = []
        input("Deine beute ist: " + ", ".join(beute_badezimmer + beute_kinderzimmer + beute_schlafzimmer + beute_wohnzimmer))
        input("Vor dem Haus hat ein Auto parkiert, nichts wie raus hier.")
        input("Beliebige Taste drücken um das Spiel zu beenden")
        beenden()
    else:
        input("Da gibt es nichts mehr zu klauen")

#Wenn das Spiel beendet wurde, zeigt es wie gut man war
def beenden():
    global inventar
    global vermögen
    for b in inventar:
        if b == "Silbernen Besteckset":
            vermögen += 1
            inventar.remove(b)
        elif b == "Teuren Wein":
            vermögen += 2
            inventar.remove(b)
        elif b == "Ipad":
            vermögen += 3
            inventar.remove(b)
        elif b == "Sparschwein":
            vermögen += 4
            inventar.remove(b)
        elif b == "Parfüm":
            input("Das ist auf dem Schwarzmarkt nichts wert.")
            input("Du hast es in die Mülltonne geschmiessen")
            inventar.remove(b)
        elif b == "Geld":
            vermögen += 6
            inventar.remove(b)
        elif b == "IWC Uhr":
            vermögen += 7
            inventar.remove(b)
        elif b == "Goldkette":
            vermögen += 8
            inventar.remove(b)
        elif b == "Goldarmband": 
            vermögen += 1
            inventar.remove(b)
    input(f"Nach deinem Einbruch hast du {vermögen}$")
    input("Beliebige Taste um das Spiel zu beenden")
    quit()
    
name = input("Wie heisst du? ")
input(f"Willkommen, {name}!")
input("Ihr seid auserwählt, um Teil einer erlesenen Gemeinschaft zu werden, die die Dunkelheit beherrscht. Ihr seid diejenigen, die im Schatten wandeln, unsichtbar für die Augen der Welt, und diejenigen, die den Mut besitzen, das Unmögliche zu tun.")
input("Ihr seid die Schattenläufer.")

input("Du bist vor einer Tür.")
art()