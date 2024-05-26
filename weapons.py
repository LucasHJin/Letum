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
    """
    A class to represent the base template for armor.
    ...

    Attributes
    ----------
    name: str
        Name of the equipment
    rarity: str
        Rarity of the equipment
    character: Character
        Instance of the Character class -> to be used for values such as the character's damage value
    buy_value: int
        Cost to buy the equipment from the shop
    sell_value: int
        Amount received from selling the equipment
    damage_multiplier: int
        Calculated multiplier based off of rarity and RARITY_MULT
    added_stats: {str: int}
        Amount of stats the equipment will add
    damage: int
        Amount of base damage before damage multiplier
    cooldownsDict: {str: int}
        Decides cooldowns within battle for each of the abilities
    ABILITY_DICT
        Provides the possible abilities to use based on the rarity of the weapon
    RARITY_MULT: {str, int}
        Provides conversion from rarity to how much an equipment's stats/gold value should be multiplied by
        
    Methods
    -------
    slash():
        Returns a value for the damage of the slash ability.
    wide_slash():
        Returns a value for the damage of the wide slash ability.
    holy_blow():
        Returns a value for the damage of the holy blow ability.
    holy_aura():
        Returns 0 for the damage of the holy aura ability and increments the 'Buffed' status in the character's instance by 1
    """
    #Created class attribute outside of initialization for it to be global among all instances
    RARITY_MULT = {
        'Common': 1.0,
        'Uncommon': 1.2,
        'Rare': 1.5,
        'Epic': 2.0,
        'Legendary': 3.0
    }
    
    def __init__(self, name, rarity, character, buy_value, sell_value, srn, dex, con):
        """
        A function that is called immediately when an instance of this class is created. It initalizes all the attributes of the class.

        Parameters
        ----------
        name: str
            Name of the item
        rarity: str
            Rarity of the item
        character: Character
            Instance of the Character class created in main
        buy_value: int
            Amount the item would cost to buy
        sell_value: int
            How much the item would sell for
        srn: int
            Amount of points the weapon gives in srn
        dex: int
            Amount of points the weapon gives in dex
        con: int
            Amount of points the weapon gives in con
            
        Returns
        -------
        None
        """
        self.name = name
        self.rarity = rarity
        #random damage
        self.damage = random.randint(6, 10)
        self.character = character
        self.buy_value = buy_value
        self.sell_value = sell_value
        self.damage_multiplier = self.RARITY_MULT[rarity]
        self.added_stats = {
            'str': srn,
            'dex': dex,
            'con': con
        }
        self.cooldownsDict = {
            'Slash': 0,
            'Wide Slash': 0,
            'Holy Blow': 0,
            'Holy Aura': 0
        }
        #Created instance attribute for it to be individual for each instance -> to ensure avoiding any possible errors
        self.ABILITY_DICT = {
            'Common': ['Slash', 'HP'],
            'Uncommon': ['Slash', 'HP'],
            'Rare': ['Slash', 'Wide Slash', 'HP'],
            'Epic': ['Slash', 'Wide Slash', 'Holy Blow', 'HP'],
            'Legendary': ['Slash', 'Wide Slash', 'Holy Blow', 'Holy Aura', 'HP']
        }

    def slash(self):
        """
        Function to calculate the amount of damage dealt with slash.
        
        Parameters
        ----------
        None

        Returns
        -------
        dmg: int
            The amount of damage dealt by this ability
        """
        #damage calculation
        dmg = int(self.damage_multiplier * (self.damage + self.character.attack_damage // 2) * random.uniform(1, 1.1))
        return dmg
    
    def wide_slash (self):
        """
        Function to calculate the amount of damage dealt with wide slash.
        
        Parameters
        ----------
        None

        Returns
        -------
        dmg: int
            The amount of damage dealt by this ability
        """
        #damage calculation
        dmg = int(self.damage_multiplier * (self.damage + self.character.attack_damage // 1.5) * random.uniform(0.5, 0.6))
        return dmg
    
    def holy_blow(self):
        """
        Function to calculate the amount of damage dealt with holy blow.

        Parameters
        ----------
        None

        Returns
        -------
        dmg: int
            The amount of damage dealt by this ability
        """
        #damage calculation
        dmg = int(self.damage_multiplier * (self.damage + self.character.attack_damage) * random.uniform(2, 3.5))
        return dmg
    
    def holy_aura(self):
        """
        Function to apply a buff to the player's character.
        
        Parameters
        ----------
        None
            
        Returns
        -------
        0: int (constant)
            Return 0 damage dealt because the buff has already been increased
        """
        if self.character.tabbar["Buffed"]:
            self.character.tabbar["Buffed"] += 1
        else:
            self.character.tabbar["Buffed"] = 1
        return 0
    