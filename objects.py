from basic_classes import Card, Hero, Deck
from spell import Spell
from creating_minions import *

# realisation Arcane (play Arcane)
arcane = Spell('Arcane Intellect', count_draw = 2, draw=True)
x=arcane.play_card()
print(x)

# attack murloc on acalyte with draw
acolyte.take_damage(vars(murloc))
print(vars(acolyte))
deck = Deck.draw_card_from_deck(1)

# attack murloc on annoy with divine shield
mech.take_damage(vars(murloc))
print(vars(mech))

# play Flame Imp
imp.play_card(damage=2)

#babbling book play
print(book.play_card(discover=True))

