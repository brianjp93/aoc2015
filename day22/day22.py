from __future__ import annotations

DAMAGE = 10
HP = 71
ABILITIES = [
    'magic_missle',
    'drain',
    'shield',
    'poison',
    'recharge',
]

class Player:
    def __init__(self, hp: int, armor: int, damage: int, mana: int):
        self.hp = hp
        self._armor = armor
        self.damage = damage
        self.mana = mana

        self.mana_spent = 0
        self.effects = {
            'shield': 0,
            'poison': 0,
            'recharge': 0,
        }

    @property
    def armor(self):
        if self.effects['shield']:
            return self._armor + 7
        return self._armor

    @armor.setter
    def armor(self, val):
        self._armor = val

    def is_lose(self):
        return self.hp <= 0 or self.mana <= 0

    def can_use(self, ability):
        return self.effects.get(ability, 0) == 0

    def __or__(self, other: Player):
        pass

    def apply_mana(self, other: Player, cost: int):
        self.mana -= cost
        self.mana_spent += cost

    def magic_missle(self, other: Player):
        self.apply_mana(other, 53)
        other.hp -= 4

    def drain(self, other: Player):
        self.apply_mana(other, 73)
        other.hp -= 2
        self.hp += 2

    def shield(self, other: Player):
        self.apply_mana(other, 113)
        self.effects['shield'] += 6

    def poison(self, other: Player):
        self.apply_mana(other, 173)
        self.effects['poison'] += 6

    def recharge(self, other: Player):
        self.apply_mana(other, 229)
        self.effects['recharge'] += 5

    def decrement_effects(self):
        for key in self.effects:
            self.effects[key] = max(self.effects[key] - 1, 0)

    def my_turn(self, other: Player, spell: str|None=None):
        if self.effects['poison']:
            other.hp -= 3
        if self.effects['recharge']:
            self.mana += 101

        self.decrement_effects()
        if spell:
            getattr(self, spell)()

    def other_turn(self, other: Player):
        damage = other.damage - self.armor
        damage = max(1, damage)
        self.decrement_effects()
        self.hp -= damage

    def find_least_mana(self, other: Player, abilities: list|None=None, ability_counter=0, my_turn=True):
        if abilities is None:
            abilities = []
        else:
            abilities = abilities[:]

        print()
        print(f'my hp: {self.hp}')
        print(f'other hp: {other.hp}')
        if my_turn:
            ability_counter += 1
            ability_counter = ability_counter % len(ABILITIES)
            ability = ABILITIES[ability_counter]
            while not self.can_use(ability):
                ability_counter = (1 + ability_counter) % len(ABILITIES)
                ability = ABILITIES[ability_counter]
            print('my turn')
            print(f'abilities: {abilities}')
        else:
            self.other_turn()
            print('other turn')

        return self.find_least_mana(other, abilities, ability_counter, not my_turn)




player = Player(50, 0, 0, 500)
boss = Player(HP, 0, DAMAGE, 0)

