from basic_classes import Card, Deck

class Spell(Card):
    def __init__(
            self,
            name: str,
            count_draw: int = 0,
            count_damage: int = 0,
            buff: bool=False,
            damage: bool=False,
            draw: bool=False,
    )->None:
        self.name = name
        self.count_draw = count_draw
        self.count_damage = count_damage
        self.buff = buff
        self.damage = damage
        self.draw = draw

    def play_card(self):
        if self.buff:
            pass
        if self.damage:
            pass
        if self.draw:
            return Deck.draw_card_from_deck(self.count_draw)

