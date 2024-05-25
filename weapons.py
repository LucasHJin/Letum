"""
Final Project
ICS3U
Lucas Jin
This file declares the Sword class with all the necessary methods and attributes. It is used in the instance of Battle to decide the damage dealt by the player.
History:
    April 13, 2024: Program Creation
    May 25, 2024: Adding Comments
"""

import random

class Sword:
    RARITY_MULT = {
        'Common': 1.0,
        'Uncommon': 1.2,
        'Rare': 1.5,
        'Epic': 2.0,
        'Legendary': 3.0
    }
    
    def __init__(self, name, rarity, character, buy_value, sell_value, srn, dex, con):
        self.name = name
        self.rarity = rarity
        self.damage = random.randint(6, 10)
        self.character = character
        self.buy_value = buy_value
        self.sell_value = sell_value
        self.added_stats = {
            'str': srn,
            'dex': dex,
            'con': con
        }
        self.damage_multiplier = self.RARITY_MULT[rarity]
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
    

