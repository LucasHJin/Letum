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
    def __init__(self, name, rarity, character):
        super().__init__(name=name, rarity=rarity, damage=50) #CHANGE BACK LATER
        self.character=character
        self.abilityDict = {
            'Common': ['Slash', 'HP'],
            'Uncommon': ['Slash', 'HP'],
            'Rare': ['Slash', 'Wide Slash', 'HP'],
            'Epic': ['Slash', 'Wide Slash', 'Holy Blow', 'HP'],
            'Legendary': ['Slash', 'Wide Slash', 'Holy Blow', 'Holy Aura', 'HP']
        }

    def slash(self):
        dmg = self.damage_multiplier * (self.damage + self.character.attack_damage // 2) * random.uniform(1, 1.1)
        return dmg
    
    def wide_slash (self):
        dmg = self.damage_multiplier * (self.damage + self.character.attack_damage) * random.uniform(0.5, 0.6)
        return dmg
    
    def holy_blow(self):
        dmg = self.damage_multiplier * (self.damage + self.character.attack_damage) * random.uniform(2, 3.5)
        return dmg
    
    def holy_aura(self):
        if self.character.tabbar["Buffed"]:
            self.character.tabbar["Buffed"] += 2
        else:
            self.character.tabbar["Buffed"] = 2
        return 0
    



"""
class Dagger(Weapon):
    def __init__(self, name):
        super().__init__(name=name)

    def swipe(self, character):
        crit = random.randint(1, 3)
        return self.damage_multiplier * self.damage // 2 * crit + character.attack_damage // 2


class Staff(Weapon):
    def __init__(self, name):
        super().__init__(name=name)

    def fireball(self, character):
        possible = random.randint(self.damage-6, self.damage+6)
        return self.damage_multiplier * possible + character.attack_damage // 2

"""
