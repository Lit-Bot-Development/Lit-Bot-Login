import sys
import sysconfig
import os
import json
import time

cls = lambda: os.system('cls')
cls()

H = 0
L = 0

with open(r"C:\Users\Gaming PC\Documents\GitHub\Application\Js.json") as f:
    data = json.load(f)

def logout():
    data['Cache']['Angemeldet'] = "False"
    with open("Js.json", "w+") as f:
        json.dump(data, f, indent=4)
    login()

def recapture():
    global L
    print("\nWillkommen bei Lit-Bot")
    print(f"Sie sind angemeldet als: {data['Cache']['Name']}")
    E  = input("<> ")
    if E == "/help":
        print("Um hier weiter zu kommen bitte gib '/recapture' ein")
        recapture()
    elif E == "/kill":
        sys.exit()
    elif E == "/logout":
        logout()
    elif E == "/recapture":
        pass
        #Hier die Verbindung zum Lit-Bot Programm
    else:
        if L >= 4:
            cls()
            print("Für Hilfe gib /help ein \n")
            recapture()
        else:
            print("Eingabe nicht vorhanden. Bitte erneut versuchen \n")
            L += 1
            recapture()

def signup():
    B = input("Bitte gib deinen Benutzernamen ein: ")
    data['Benutzer'].append(B)
    P = input(f"Bitte gib das Passwort für den Benutzer ein ({B}): ")
    data['Passwort'].append(P)
    with open(r"C:\Users\Gaming PC\Documents\GitHub\Application\Js.json", "w+") as f:
        json.dump(data, f, indent=4)
    print(f"Login-Daten: \n\n Benutzername: {B} \n Passwort: {P}")
    login()

def login():
    global H
    if data['Cache']['Angemeldet'] == "True":
        recapture()
    elif data['Cache']['Angemeldet'] == "False":
        V = input("\nBitte Benutzer auswählen: ")
        if V in data['Benutzer']:
            index = data['Benutzer'].index(V)
            User = data['Benutzer'][index]
            Passwort = data['Passwort'][index]
            if V == User:
                if Passwort == "-":
                    data['Cache']['Angemeldet'] = "True"
                    data['Cache']['Name'] = f"{V}"
                    with open(r"C:\Users\Gaming PC\Documents\GitHub\Application\Js.json", "w+") as f:
                        json.dump(data, f, indent=4)
                    recapture()
                else:
                    P = input(f"\nBitte das Passwort für den Benuzter ({User}) eingeben: ")
                    if P == Passwort:
                        data['Cache']['Angemeldet'] = "True"
                        data['Cache']['Name'] = f"{V}"
                        with open(r"C:\Users\Gaming PC\Documents\GitHub\Application\Js.json", "w+") as f:
                            json.dump(data, f, indent=4)
                        recapture()
                    else:
                        cls()
                        print("Falsches Passwort. Bitte erneut versuchen")
                        time.sleep(2)
                        cls()
                        login()
            elif V == "/help":
                print("Falls du keinen Account hast gib '/new' oder 'local' als Benutzernamen ein\n")
                login()
            elif V == "/new":
                try:
                    signup()
                except:
                    print("International Error", end="\n")
                    login()
        elif V == "/help":
                print("Falls du keinen Account hast gib '/new' oder 'local' als Benutzernamen ein\n")
                login()
        elif V == "/new":
            try:
                signup()
            except:
                print("International Error", end="\n")
                login()
            else:
                if H >= 4:
                    cls()
                    print("Für Hilfe gib /help ein \n")
                    login()
                else:
                    print(f"Nicht regestrierter Benutzer: <{V}> \n")
                    H += 1
                    login()
        else:
            if H >= 4:
                cls()
                print("Für Hilfe gib /help ein \n")
                login()
            else:
                print(f"Nicht regestrierter Benutzer: <{V}> \n")
                H += 1
                login()
    else:
        print("International Error. Bitte versuche es erneut")
        login()

login()