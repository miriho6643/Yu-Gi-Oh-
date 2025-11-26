from __init__ import *

read_cards(create_deck(deck_size=5))

for i in range(5):
    cards = deck[i]
print(cards)
read_cards(cards)