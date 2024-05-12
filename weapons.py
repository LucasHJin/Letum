import random

class Weapon:
    RARITY_MULT = {
        'Common': 1.0,
        'Uncommon': 1.2,
        'Rare': 1.5,
        'Epic': 2.0,
        'Legendary': 3.0
    }
    
    def __init__(self, name, damage, rarity):
        self.name = name
        self.damage = damage
        self.rarity = rarity
        self.damage_multiplier = self.RARITY_MULT[rarity]

class Sword(Weapon):
    def __init__(self, name, rarity, character, buy_value, sell_value, srn, dex, con):
        super().__init__(name=name, rarity=rarity, damage = random.randint(6, 9)) 
        self.character = character
        self.buy_value = buy_value
        self.sell_value = sell_value
        self.abilityDict = {
            'Common': ['Slash', 'HP'],
            'Uncommon': ['Slash', 'HP'],
            'Rare': ['Slash', 'Wide Slash', 'HP'],
            'Epic': ['Slash', 'Wide Slash', 'Holy Blow', 'HP'],
            'Legendary': ['Slash', 'Wide Slash', 'Holy Blow', 'Holy Aura', 'HP']
        }
        self.cooldownsDict = {
            'Slash': 0,
            'Wide Slash': 0,
            'Holy Blow': 0,
            'Holy Aura': 0
        }
        self.added_stats = {
            'str': srn,
            'dex': dex,
            'con': con
        }

    def slash(self):
        dmg = int(self.damage_multiplier * (self.damage + self.character.attack_damage // 2) * random.uniform(1, 1.1))
        return dmg
    
    def wide_slash (self):
        dmg = int(self.damage_multiplier * (self.damage + self.character.attack_damage // 1.5) * random.uniform(0.5, 0.6))
        return dmg
    
    def holy_blow(self):
        dmg = int(self.damage_multiplier * (self.damage + self.character.attack_damage) * random.uniform(2, 3.5))
        return dmg
    
    def holy_aura(self):
        if self.character.tabbar["Buffed"]:
            self.character.tabbar["Buffed"] += 1
        else:
            self.character.tabbar["Buffed"] = 1
        return 0
    

