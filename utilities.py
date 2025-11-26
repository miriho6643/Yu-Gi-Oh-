import time, random, os, pyttsx3
from characters import *

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('volume', 1.0)
engine.setProperty('rate', 190)
engine.setProperty('voice', voices[1].id)

class helpers:
    def read_aloud(txt: str):
        engine.say(txt)
        engine.runAndWait()

    def slow_print(txt: str, delay: float):
        for x in txt:
            print(x, end="", flush=True)
            time.sleep(delay)

    def get_yugioh_card(name, level, typ, attribute, attack, defense, effect, icon):
        end = "╔" + "═"*38 + "╗\n"
        end += f"║ {name.center(36)} ║\n"
        end += f"║ Level: {'*'*level:<29} ║\n"
        end += f"║ Type: {typ.ljust(30)} ║\n"
        end += "║" + "─"*38 + "║\n"
        end += "║" + " "*38 + "║\n"
        counter = 0
        for l in icon:
            counter += 1
            end += f"║{l.center(38)}║\n"
        end += "║" + f"[{attribute.upper()}]".center(38) + "║\n"
        for i in range(4-counter):
            end += "║" + " "*38 + "║\n"
        end += "║" + "─"*38 + "║\n"
        words = effect.split()
        line = ""
        count = 0
        for word in words:
            if len(line + word) <= 36:
                line += word + " "
            else:
                count += 1
                end += f"║ {line.ljust(36)} ║\n"
                line = word + " "
        if line:
            end += f"║ {line.ljust(36)} ║\n"
        for i in range(3-count):
            end += "║" + " "*38 + "║\n"
        end += "║" + "─"*38 + "║\n"
        end += f"║ ATK/{attack}  DEF/{defense}".ljust(39) + "║\n"
        end += "╚" + "═"*38 + "╝\n"
        return end

def read_cards(cards: list, printspeed: float = 100):
    all_decks = {**maindeck, **secdeck}
    helpers.slow_print(list_cards(cards), printspeed/10000000)
    for card in cards:
        helpers.read_aloud(all_decks[card]["name"])
        helpers.read_aloud(all_decks[card]["effect"])

def list_cards(cards: list):
    all_decks = {**maindeck, **secdeck}
    asciicards = [helpers.get_yugioh_card(**all_decks[x]) for x in cards]
    card_lines = [card.split("\n") for card in asciicards]
    max_lines = max(len(lines) for lines in card_lines)
    widths = [max(len(line) for line in lines) for lines in card_lines]
    for idx, lines in enumerate(card_lines):
        while len(lines) < max_lines:
            lines.append(" "*widths[idx])
        for i in range(len(lines)):
            lines[i] = lines[i].ljust(widths[idx])
    merged = []
    for i in range(max_lines):
        merged.append("   ".join(lines[i] for lines in card_lines))
    return "\n".join(merged)

def create_deck(cardpool, deck_size=20, max_copies=3):
    deck = []
    counts = {key: 0 for key in cardpool}
    attempts = 0
    max_attempts = 5000
    while len(deck) < deck_size:
        attempts += 1
        if attempts >= max_attempts:
            break
        card = random.choice(list(cardpool.keys()))
        divine_count = sum(1 for c in deck if cardpool[c].get("typ")=="Divine-Beast")
        if cardpool[card].get("typ")=="Divine-Beast" and divine_count >= 1:
            continue
        if counts[card] >= max_copies:
            continue
        deck.append(card)
        counts[card] += 1
    return deck

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')
