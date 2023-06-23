import random


class Card():

    def __init__(self, name: str, mana_cost: int)-> None:
        self.name = name
        self.mana_cost = mana_cost

    def spending_mana(self):
        pass




class Hero():
    health_points = 30
    __card_counts = 3

    def __init__(self,name: str)-> None:
        self.name = name

    # не знаю от чего он зависит, чтобы написать
    def hero_power(self):
        pass

    def draw_card(self, count: int):
        self.__card_counts += count


class Table():
    pass

class Deck():
    deck = [
        "Minion('Murloc Tinyfin', 0, 1, 1)",
        "Minion('Deathwing',10, 12, 12)",
        "Minion('Emerald Drake', 4, 7, 6)"
    ]
    spells = ["Spell('Arcane Intellect', count = 2, draw=True)", "Spell('Fireball', count_damage=6, damage=True)"]

    @classmethod
    def draw_card_from_deck(cls, count: int)-> list:
        cards = []
        for i in range(count):
            x = cls.deck.pop()
            cards.append(x)
        return cards

    @classmethod
    def discover_spell(cls):
        return random.choice(cls.spells)

