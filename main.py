from __init__ import *

for i in range(2):
    handcards = deck[:5]
    deck = deck[5:]
    read_cards(handcards)
    print("\n")