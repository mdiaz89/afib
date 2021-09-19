import random  # Modul random wird importiert, um Zufallswerte zu generieren
import turtle # Modul turtlem wird importiert, um die Blöcke grafisch darzustellen

tower = 1  # 1 Block steht schon auf dem Boden
blocks = 7  # Anzahl Blöcke
time = 12 # Anzahl Zeiteinheiten bzw. Versuche

def firstBlock():  # Diese Funktion zeichnet den ersten Block für den Turm
    for steps in range(3):
        turtle.color('black')
        turtle.forward(25)
        turtle.right(90)
    turtle.forward(25)
    return

def posBlock():  # Diese Funktion zeichnet alle zusätzlichen Blöcke in den Turm
    for steps in range(4):
        turtle.color('black')
        turtle.forward(25)
        turtle.right(90)
    turtle.forward(25)
    return

def negBlock():  # Diese Funktion lässt einen oder mehrere Blöcke herunterfallen, indem sie 'löscht' bzw. mit einer anderen Farbe überschreibt
    for steps in range(2):
        turtle.color('white')
        turtle.right(90)
        turtle.forward(25)
    turtle.color('black')
    turtle.right(90)
    turtle.forward(25)
    turtle.color('white')
    turtle.right(90)
    for steps in range(2):
        turtle.forward(25)
        turtle.right(180)
    return


turtle.hideturtle()  # Die Methode hideturtle vom Modul turtle macht den Cursor unsichtbar
firstBlock()  # Erster Block wird auf dem Boden gestellt.

while time > 0 :  # While-Schleife prüft, ob noch Zeit vorhanden ist und substrahiert eine Zeiteinheit pro Versuch
    time -= 1
    if blocks != 0 :  # If-Statement prüft, ob wir noch Blöcke zum stapeln haben
        x = input('Drücke 1 und die Eingabetaste um einen Block zu stapeln.')
        if x == '1' :  # If-Statement prüft, ob die Eingabe richtig ist
            if tower <= 2 :  # If-Statement prüft, ob der Turm weniger als 2 Blöcke hat
                posBlock()
                tower += 1
                blocks -= 1
                print(f'+{x} Block. Der Turm hat jetzt: {tower} || {blocks} fehlen noch!')
            elif tower == 3 or tower == 4 :  # Elif prüft, ob der Turm zwischen 3 und 4 Blöcke hat
                y = random.randint(0,2)  # Y ist ein Zufallswert zwischen 0 und 2 und genau so viele Blöcke können herunterfallen
                if y == 0 :
                    posBlock()
                    tower += 1
                    blocks -= 1
                    print(f'+{x} Block. Der Turm hat jetzt: {tower} || {blocks} fehlen noch.')
                elif y == 1:
                    negBlock()
                    tower -= 1
                    blocks += 1
                    print(f'-{x} Block. Der Turm hat jetzt: {tower} || {blocks} fehlen noch.')
                else: 
                    for i in range(y):
                        negBlock()
                    tower -= y
                    blocks += y
                    print(f'-{y} Block/Blöcke. Der Turm hat jetzt: {tower} || {blocks} fehlen noch.')
            elif tower >= 5 :  # Elif prüft, ob der Turm zwischen 5 und 8 Blöcke hat
                y = random.randint(0,4)  # Y ist ein Zufallswert zwischen 0 und 4, so viele Blöcke können herunterfallen
                if y == 0 :
                    posBlock()
                    tower += 1
                    blocks -= 1
                    print(f'+{x} Block. Der Turm hat jetzt: {tower} || {blocks} fehlen noch.')
                elif y == 1 :
                    negBlock()
                    tower -= y
                    blocks += y
                    print(f'-{y} Block. Der Turm hat jetzt: {tower} || {blocks} fehlen noch.')
                else: 
                    for i in range(y):
                        negBlock()
                    tower -= y
                    blocks += y
                    print(f'-{y} Blöcke. Der Turm hat jetzt: {tower} || {blocks} fehlen noch.')
        else:  # Else prüft, ob die Eingabe falsch ist und informiert den Nutzer
            print('Ungültige Eingabe. Drücke "1" um einen Block zu stapeln.')
    else:  # Wenn keine Blöcke mehr vorhanden sind, wird die Zeitschleife unterbrochen
        print('Geschafft! Du hast den Turm fertig gebaut!')
        break
else:  # Wenn keine Zeit mehr vorhanden ist, wird der Nutzer informiert
    print('Die Zeit ist um!')
_=input('Drücke die Eingabetaste, um das Programm zu schließen.')