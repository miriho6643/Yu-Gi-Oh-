from __init__ import *

# --- Decks erstellen ---
normaldeck = gameplay.create_deck(maindeck, deck_size=40)
extradeck = gameplay.create_deck(secdeck, deck_size=15)

# --- Handkarten ziehen ---
handcards = normaldeck[:5]
normaldeck = normaldeck[5:]

# --- Handkarten anzeigen und vorlesen ---
gameplay.read_cards(handcards)
