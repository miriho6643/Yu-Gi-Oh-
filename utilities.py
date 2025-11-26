import time, random, os, pyttsx3
from characters import *

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('volume', 1.0)  # 0.0 bis 1.0
engine.setProperty('rate', 190)  # langsamer = verständlicher
engine.setProperty('voice', voices[1].id)

class helpers:
    def read_aloud(txt: str):
        engine.say(txt)
        engine.runAndWait()
    def slow_print(txt: str, delay: float):
        for x in txt:
            print(x, end="")
            time.sleep(delay)
    def get_yugioh_card(name, level, typ, attribute, attack, defense, effect, icon):
        end = ""
        # Top border
        end +=("╔" + "═" * 38 + "╗" + "\n")
    
        # Name
        end +=(f"║ {name.center(36)} ║" + "\n")
    
        # Level stars
        stars = "*" * level
        end +=(f"║ Level: {stars.ljust(29)} ║" + "\n")
    
        # Type
        end +=(f"║ Type: {typ.ljust(30)} ║" + "\n")
    
        # Separator
        end +=("║" + "─" * 38 + "║" + "\n")
    
        # Monster attribute placeholder (6 lines)
        end +=("║" + " " * 38 + "║" + "\n")
        counter = 0
        for l in icon:
            counter += 1
            end +=("║" + l.center(38) + "║" + "\n")
        
        end +=("║" + ("[" + attribute.upper() + "]").center(38) + "║" + "\n")

        for i in range(4-counter):
            end +=("║" + " " * 38 + "║" + "\n")
    
        # Separator
        end +=("║" + "─" * 38 + "║" + "\n")
    
        # Effect text (wrap at 36 chars)
        words = effect.split()
        line = ""
        count = 0
        for word in words:
            if len(line + word) <= 36:
                line += word + " "
            else:
                count += 1
                end +=(f"║ {line.ljust(36)} ║" + "\n")
                line = word + " "
        if line:
            end +=(f"║ {line.ljust(36)} ║" + "\n")
        for i in range(3-count):
            end +=("║" + " " * 38 + "║" + "\n")

    
        # Separator
        end +=("║" + "─" * 38 + "║" + "\n")
    
        # ATK/DEF
        end +=(f"║ ATK/{attack}  DEF/{defense}".ljust(39) + "║" + "\n")
    
        # Bottom border
        end +=("╚" + "═" * 38 + "╝" + "\n")
        
        return end

def read_cards(cards: list, deck: list = normaldeck):
    helpers.slow_print(list_cards(cards), 0.001)
    for card in cards:
        helpers.read_aloud(deck[card]["name"])
        helpers.read_aloud(deck[card]["effect"])

def list_cards(cards: list):
    # Kattributeen in ASCII-Strings umwandeln (falls noch nicht geschehen)
    asciicards = [helpers.get_yugioh_card(**normaldeck[x]) if isinstance(x, str) else x for x in cards]

    # Jede Kattributee in eine Liste aus Zeilen aufteilen
    card_lines = [card.split("\n") for card in asciicards]

    # Maximale Zeilenanzahl bestimmen
    max_lines = max(len(lines) for lines in card_lines)

    # Breite jeder Kattributee bestimmen
    widths = [max(len(line) for line in lines) for lines in card_lines]

    # Kattributeen auf gleiche Höhe und Breite bringen
    for idx, lines in enumerate(card_lines):
        card_width = widths[idx]
        # Zeilen auffüllen, falls Kattributee kürzer ist
        while len(lines) < max_lines:
            lines.append(" " * card_width)
        # Alle Zeilen auf gleiche Breite bringen
        for i in range(len(lines)):
            lines[i] = lines[i].ljust(card_width)

    # Zeilenweise nebeneinander kombinieren
    merged = []
    for i in range(max_lines):
        row = "   ".join(lines[i] for lines in card_lines)
        merged.append(row)

    # Gesamtausgabe als String
    return "\n".join(merged)

def create_deck(deck=normaldeck, deck_size=20, max_copies=3):
    deck = []
    counts = {key: 0 for key in deck}

    while len(deck) < deck_size:
        card = random.choice(list(deck.keys()))

        # Prüfen, wie viele Divine-Beast-Kattributeen bereits im deck sind
        divine_count = sum(1 for c in deck if deck[c]['typ'] == 'Divine-Beast')

        if deck[card]['typ'] == 'Divine-Beast':
            # Wenn schon eine Divine-Beast im deck ist, überspringen
            if divine_count >= 1:
                continue
        else:
            # Für normale Kattributeen: max_copies beachten
            if counts[card] >= max_copies:
                continue

        deck.append(card)
        counts[card] += 1

    return deck

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def compare(card1: str, card2: str, card1inattack: bool, card2inattack: bool):
    c1 = normaldeck[card1]
    c2 = normaldeck[card2]

    # Werte abhängig vom Modus auswählen
    v1 = c1['attack'] if card1inattack else c1['defense']
    v2 = c2['attack'] if card2inattack else c2['defense']

    # Differenz berechnen (immer positiv)
    return (card1 if v1 > v2 and card1inattack else card2 if v1 < v2 and card2inattack else None, abs(v1 - v2))

maindeck = create_deck(deck_size=40)
handcards = []