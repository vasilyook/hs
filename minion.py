from basic_classes import Card, Deck

class Minion(Card):
    def __init__(
            self,
            name: str,
            mana_cost: int,
            attack: int,
            health: int,
            battlecry: bool=False,
            charge: bool=False,
            deathrattle: bool=False,
            divine_shield: bool=False,
            lifesteal: bool=False,
            no_target: bool=False,
            rush: bool=False,
            taunt: bool=False
    )-> None:
        self.name = name
        self.__mana_cost = mana_cost
        self.__attack = attack
        self.__health = health
        self.battlecry = battlecry
        self.charge = charge
        self.deathrattle = deathrattle
        self.divine_shield = divine_shield
        self.lifesteal = lifesteal
        self.no_target = no_target
        self.rush = rush
        self.taunt = taunt

    def battle_cry(self, damage=0, discover=False, draw=False):
        if damage>0:
            print('Вам снесли ' + str(damage) + ' hp.')

        if discover:
            return Deck.discover_spell()

    def deathrattle(self):
        pass

    def end_turn(self):
        pass

    def get_attack(self):  # получение значения атрибута
        return self.__attack

    def get_health(self):  # получение значения атрибута
        return self.__health

    def set_new_attack(self, attack):
        self.__attack = attack

    def set_new_health(self, health):
        self.__health = health

    def play_card(self, damage=0, discover=False, draw=False):
        if self.battlecry:
            return self.battle_cry(damage, discover, draw)


    def take_damage(
            self,
            minion_attacking: dict
    )->None:

        if self.divine_shield:
            self.divine_shield = False
        else:
            self.__health = self.__health - minion_attacking['_Minion__attack']





