from requests import get

def thumbnail_herunterladen(url, dateiname="thumbnail.png"):
    while True:
        if "youtu.be" in url:
            id = url.split("/")[3]
        elif "youtube.com" in url:
            id = url.split("=")[1][:11]
        else:
            print("URL ist ungültig")
            url = input("Gültige URL eingeben: ")
            continue
        
        quali = input("Welche Auflösung:\n 1-Standard Qualität\n 2-Höchste Auflösung")

        if quali == "1":
            name = "sddefault.jpg"
        elif quali == "2":
            name = "maxresdefault.jpg"
        else:
            print("Ungültige Eingabe")
            quali = input("1- Standard Qualität\n2-Höchste Auflösung")
            continue

        with open(dateiname, "wb") as datei:
            antwort = get(f"https://img.youtube.com/vi/{id}/{name}")
            datei.write(antwort.content)
            print("Download erfolgreich!")
            break
        