# Yu-Gi-Oh! Terminal Game

I try to make a fully functional Yu-Gi-Oh! ard game in the terminal.
I use custom ascii Cards with attack level defense and much more.
This Project is free to use for everyone.


# Files

**main.py** is the file where you start the game of.
There you can type the Sequence of the Game.

In **__init__.py** is all the code for downloading required libaries.
It imports the libaries utilities, characters and pyttsx3.
Pyttsx3 is a Text to speech libary and for reading of the cards.
The other two libaries are to play the game.

**utilities.py** is the python Libary for the game itself. 
It defines ingame functions like reading text or listing cards.

**characters.py** is the libary for all the characters in the game.
You have a strict format to add new characters to the game.
The Format is like that:
*'name': {'name': "YOUR CARD NAME", 'level': "YOUR CARD LEVEL", 'typ': "YOUR CARD TYPE", 'attribute': "YOUR CARD ELEMENT", 'attack': YOUR ATTACK DAMAGE, 'defense': YOUR DEFENSE NUMBER, 'effect': "YOUR CARD EFFECT", 'icon': [YOUR ASCII ICON]}*
