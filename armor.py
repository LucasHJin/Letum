#to use to generate items
import random

class Base:
    """
    A class to represent the base template for armor.
    ...

    Attributes
    ----------
    name: str
        Name of the equipment
    rarity: str
        Rarity of the equipment
    multiplier: str
        Calculated multiplier based off of rarity and RARITY_MULT
    buy_value: int
        Cost to buy the equipment from the shop
    sell_value: int
        Amount received from selling the equipment
    added_stats: {str, int}
        Amount of stats the equipment will add
    added_extra: {str, int}
        Amount of extra benefits (health, armor class, damage) the equipment will add

    Constants
    ---------
    RARITY_MULT: {str, int}
        Provides conversion from rarity to how much an equipment's stats/gold value should be multiplied by
    """
    RARITY_MULT = {
        'Common': 1.0,
        'Uncommon': 1.2,
        'Rare': 1.5,
        'Epic': 2.0,
        'Legendary': 3.0
    }
    
    def __init__(self, name, rarity, buy_value, sell_value):
        self.name = name
        self.rarity = rarity
        self.multiplier = self.RARITY_MULT[rarity]
        self.buy_value = buy_value
        self.sell_value = sell_value
        self.added_stats = {
            'str': 0,
            'dex': 0,
            'con': 0
        }
        self.added_extra = {
            'ac': 0,
            'hp': 0,
            'dmg': 0
        }

    def decide_stats(self, weight1, weight2):
        split_points = random.choices(['str', 'dex', 'con'], weights=weight1, k=self.points)
        self.added_stats['str']=split_points.count('str')
        self.added_stats['dex']=split_points.count('dex')
        self.added_stats['con']=split_points.count('con')

        split_points_extra = random.choices(['ac', 'hp', 'dmg'], weights=weight2, k=self.points*8)
        self.added_extra['ac']=split_points_extra.count('ac')//3
        self.added_extra['hp']=int(split_points_extra.count('hp')*1.5)
        self.added_extra['dmg']=split_points_extra.count('dmg')//2

class Helmet(Base):
    """
    A class to represent the helmet template (is a child class, inheriting from parent class: Base)
    ...
    """
    def __init__(self, name, rarity, buy_value, sell_value, added_stats=None, added_extra=None):
        super().__init__(name, rarity, buy_value, sell_value)
        self.added_stats = added_stats if added_stats is not None else {'str': 0, 'dex': 0, 'con': 0}
        self.added_extra = added_extra if added_extra is not None else {'ac': 0, 'hp': 0, 'dmg': 0}
        self.points = int(4 * self.multiplier)

class Armor(Base):
    """
    A class to represent the armor template (is a child class, inheriting from parent class: Base)
    ...
    """
    def __init__(self, name, rarity, buy_value, sell_value, added_stats=None, added_extra=None):
        super().__init__(name, rarity, buy_value, sell_value)
        self.added_stats = added_stats if added_stats is not None else {'str': 0, 'dex': 0, 'con': 0}
        self.added_extra = added_extra if added_extra is not None else {'ac': 0, 'hp': 0, 'dmg': 0}
        self.points = int(5 * self.multiplier)

class Ring(Base):
    """
    A class to represent the ring template (is a child class, inheriting from parent class: Base)
    ...
    """
    def __init__(self, name, rarity, buy_value, sell_value, added_stats=None, added_extra=None):
        super().__init__(name, rarity, buy_value, sell_value)
        self.added_stats = added_stats if added_stats is not None else {'str': 0, 'dex': 0, 'con': 0}
        self.added_extra = added_extra if added_extra is not None else {'ac': 0, 'hp': 0, 'dmg': 0}
        self.points = int(2 * self.multiplier)
