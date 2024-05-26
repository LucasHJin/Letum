"""
Final Project
ICS3U
Lucas Jin
This file declares the Parent and Child classes for equipment with all the necessary methods and attributes. The equipment will be used by the player in various manners.
History:
    April 13, 2024: Program Creation
    May 25, 2024: Adding Comments
"""

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
    multiplier: float
        Calculated multiplier based off of rarity and RARITY_MULT
    buy_value: int
        Cost to buy the equipment from the shop
    sell_value: int
        Amount received from selling the equipment
    added_stats: {str: int}
        Amount of stats the equipment will add
    added_extra: {str: int}
        Amount of extra benefits (health, armor class, damage) the equipment will add
    RARITY_MULT: {str: float}
        Provides conversion from rarity to how much an equipment's stats/gold value should be multiplied by
        
    Methods
    -------
    decide_stats(weight1, weight2):
        Creates the stats and extra bonuses for an equipment when called
    """
    RARITY_MULT = {
        'Common': 1.0,
        'Uncommon': 1.2,
        'Rare': 1.5,
        'Epic': 2.0,
        'Legendary': 3.0
    }
    
    def __init__(self, name, rarity, buy_value, sell_value):
        """
        A function that is called immediately when an instance of this class is created. It initalizes all the attributes of the class.

        Parameters
        ----------
        name: str
            Name of the item
        rarity: str
            Rarity of the item
        buy_value: int
            Amount the item would cost to buy
        sell_value: int
            How much the item would sell for
            
        Returns
        -------
        None
        """
        #initializing all the attributes for the Base class
        self.name = name
        self.rarity = rarity
        #determining multiplier based on rarity
        self.multiplier = self.RARITY_MULT[rarity]
        self.buy_value = buy_value
        self.sell_value = sell_value
        #all will start with 0 in stats and extra -> will be updated with function when created
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
        """
        A function to create/decide the stats of an instance of Base or its children once it is created (creating stats for equipment)

        Parameters
        ----------
        weight1: [int]
            Values for probability calculations for stats
        weight2: [int]
            Values for probability calculations for extra bonuses
        
        Returns
        -------
        None
        """
        #using random.choices to determine how many points to assign to each stat
        split_points = random.choices(['str', 'dex', 'con'], weights=weight1, k=int(4 * self.multiplier))
        #assigning stats
        self.added_stats['str']=split_points.count('str')
        self.added_stats['dex']=split_points.count('dex')
        self.added_stats['con']=split_points.count('con')

        #using random.choices to determine how many extra points to assign to each extra value
        split_points_extra = random.choices(['ac', 'hp', 'dmg'], weights=weight2, k=int(4 * self.multiplier)*8)
        #assigning points
        self.added_extra['ac']=split_points_extra.count('ac')//3
        self.added_extra['hp']=int(split_points_extra.count('hp')*1.5)
        self.added_extra['dmg']=split_points_extra.count('dmg')//2

class Helmet(Base):
    """
    A class to represent the helmet template (is a child class, inheriting from parent class: Base)
    """
    #explicitly listing seemingly redunant arguments in init -> provides clarity for documentation
    def __init__(self, name, rarity, buy_value, sell_value):
        """
        A function that is called immediately when an instance of this class is created. It initalizes all the attributes of the class.

        Parameters
        ----------
        name: str
            Name of the item
        rarity: str
            Rarity of the item
        buy_value: int
            Amount the item would cost to buy
        sell_value: int
            How much the item would sell for

        Returns
        -------
        None
        """
        #init -> initializes all attributes of helmet
        #super -> calls parent class's methods (init in this case)
        #don't need to call added_stats or added_extra in super().__init__ because they were not passed as arguments in the parent class's init
        super().__init__(name, rarity, buy_value, sell_value)

class Armor(Base):
    """
    A class to represent the armor template (is a child class, inheriting from parent class: Base)
    """
    def __init__(self, name, rarity, buy_value, sell_value):
        """
        A function that is called immediately when an instance of this class is created. It initalizes all the attributes of the class.

        Parameters
        ----------
        name: str
            Name of the item
        rarity: str
            Rarity of the item
        buy_value: int
            Amount the item would cost to buy
        sell_value: int
            How much the item would sell for
            
        Returns
        -------
        None
        """
        super().__init__(name, rarity, buy_value, sell_value)

class Ring(Base):
    """
    A class to represent the ring template (is a child class, inheriting from parent class: Base)
    """
    def __init__(self, name, rarity, buy_value, sell_value):
        """
        A function that is called immediately when an instance of this class is created. It initalizes all the attributes of the class.

        Parameters
        ----------
        name: str
            Name of the item
        rarity: str
            Rarity of the item
        buy_value: int
            Amount the item would cost to buy
        sell_value: int
            How much the item would sell for
        
        Returns
        -------
        None
        """
        super().__init__(name, rarity, buy_value, sell_value)
