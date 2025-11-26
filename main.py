from __init__ import *

for i in range(1):
    print(maindeck)
    handcards = maindeck[:5]
    maindeck = maindeck[5:]
    read_cards(handcards)
    print("\n")
    print(maindeck)