import random

class Armor:
    RARITY_MULT = {
        'Common': 1.0,
        'Uncommon': 1.2,
        'Rare': 1.5,
        'Epic': 2.0,
        'Legendary': 3.0
    }
    
    def __init__(self, name, rarity):
        self.name = name
        self.rarity = rarity
        self.multiplier = self.RARITY_MULT[rarity]
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

class Head(Armor):
    def __init__(self, name, rarity, buy_value, sell_value, added_stats=None, added_extra=None):
        super().__init__(name, rarity)
        self.added_stats = added_stats if added_stats is not None else {'str': 0, 'dex': 0, 'con': 0}
        self.added_extra = added_extra if added_extra is not None else {'ac': 0, 'hp': 0, 'dmg': 0}
        self.points = int(4 * self.multiplier)
    
    def decide_stats(self):
        split_points = random.choices(['str', 'dex', 'con'], weights=[2, 3, 4], k=self.points)
        self.added_stats['str']=split_points.count('str')
        self.added_stats['dex']=split_points.count('dex')
        self.added_stats['con']=split_points.count('con')

        split_points_extra = random.choices(['ac', 'hp', 'dmg'], weights=[3, 3, 1], k=self.points*8)
        self.added_extra['ac']=split_points_extra.count('ac')//3
        self.added_extra['hp']=int(split_points_extra.count('hp')*1.5)
        self.added_extra['dmg']=split_points_extra.count('dmg')//2


class Body(Armor):
    def __init__(self, name, rarity, buy_value, sell_value, added_stats=None, added_extra=None):
        super().__init__(name, rarity)
        self.added_stats = added_stats if added_stats is not None else {'str': 0, 'dex': 0, 'con': 0}
        self.added_extra = added_extra if added_extra is not None else {'ac': 0, 'hp': 0, 'dmg': 0}
        self.points = int(5 * self.multiplier)
    
    def decide_stats(self):
        split_points = random.choices(['str', 'dex', 'con'], weights=[4, 2, 4], k=self.points)
        self.added_stats['str']=split_points.count('str')
        self.added_stats['dex']=split_points.count('dex')
        self.added_stats['con']=split_points.count('con')

        split_points_extra = random.choices(['ac', 'hp', 'dmg'], weights=[3, 3, 1], k=self.points*8)
        self.added_extra['ac']=split_points_extra.count('ac')//3
        self.added_extra['hp']=int(split_points_extra.count('hp')*1.5)
        self.added_extra['dmg']=split_points_extra.count('dmg')//2


class Ring(Armor):
    def __init__(self, name, rarity, buy_value, sell_value, added_stats=None, added_extra=None):
        super().__init__(name, rarity)
        self.added_stats = added_stats if added_stats is not None else {'str': 0, 'dex': 0, 'con': 0}
        self.added_extra = added_extra if added_extra is not None else {'ac': 0, 'hp': 0, 'dmg': 0}
        self.points = int(2 * self.multiplier)
    
    def decide_stats(self):
        split_points = random.choices(['str', 'dex', 'con'], weights=[3, 2, 1], k=self.points)
        self.added_stats['str']=split_points.count('str')
        self.added_stats['dex']=split_points.count('dex')
        self.added_stats['con']=split_points.count('con')

        split_points_extra = random.choices(['ac', 'hp', 'dmg'], weights=[2, 1, 4], k=self.points*8)
        self.added_extra['ac']=split_points_extra.count('ac')//3
        self.added_extra['hp']=int(split_points_extra.count('hp')*1.5)
        self.added_extra['dmg']=split_points_extra.count('dmg')//2