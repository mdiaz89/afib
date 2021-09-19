import random  # Modul random wird importiert, um Zufallswerte zu generieren

tower = 1  # 1 Block steht schon auf dem Boden
blocks = 7  # Anzahl Blöcke
time = 12 # Anzahl Zeiteinheiten bzw. Versuche

while time > 0 :  # While-Schleife prüft, ob noch Zeit vorhanden ist
    time -= 1
    if blocks != 0 :  # If-Statement prüft, ob wir noch Blöcke zum stapeln haben
        x = input('Drücke 1 und die Eingabetaste um einen Block zu stapeln.')
        if x == '1' :  # If-Statement prüft, ob die Eingabe richtig ist
            if tower <= 2 :  # If-Statement prüft, ob der Turm weniger als 2 Blöcke hat
                tower += 1
                blocks -= 1
                print(f'+{x} Block. Der Turm hat jetzt: {tower} || {blocks} fehlen noch!')
            elif tower == 3 or tower == 4 :  # Elif prüft, ob der Turm zwischen 3 und 4 Blöcke hat
                y = random.randint(0,2)  # Y ist ein Zufallswert zwischen 0 und 2 und genau so viele Blöcke können herunterfallen
                if y == 0 :
                    tower += 1
                    blocks -= 1
                    print(f'+{x} Block. Der Turm hat jetzt: {tower} || {blocks} fehlen noch.')
                else: 
                    tower -= y
                    blocks += y
                    print(f'-{y} Block/Blöcke. Der Turm hat jetzt: {tower} || {blocks} fehlen noch.')
            elif tower >= 5 :  # Elif prüft, ob der Turm zwischen 5 und 8 Blöcke hat
                y = random.randint(0,4)  # Y ist ein Zufallswert zwischen 0 und 4, so viele Blöcke können herunterfallen
                if y == 0 :
                    tower += 1
                    blocks -= 1
                    print(f'+{x} Block. Der Turm hat jetzt: {tower} || {blocks} fehlen noch.')
                else:
                    tower -= y
                    blocks += y
                    print(f'-{y} Block/Blöcke. Der Turm hat jetzt: {tower} || {blocks} fehlen noch.')
        else:  # Else prüft, ob die Eingabe falsch ist und informiert den Nutzer
            print('Ungültige Eingabe. Drücke "1" um einen Block zu stapeln.')
    else:  # Wenn keine Blöcke mehr vorhanden sind, wird die Zeitschleife unterbrochen
        print('Geschafft! Du hast den Turm fertig gebaut!')
        break
else:  # Wenn keine Zeit mehr vorhanden ist, wird der Nutzer informiert
    print('Die Zeit ist um!')
_=input('Drücke die Eingabetaste, um das Programm zu schließen.')