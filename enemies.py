"""
Final Project
ICS3U
Lucas Jin
This file declares the Parent and Child classes for the various enemies of the game with all the necessary methods and attributes. Instances of them will be called in the Battle class in battles.py to represent the enemies within the game.
History:
    April 13, 2024: Program Creation
    May 25, 2024: Adding Comments
"""

import random

class Enemy:
    """
    A class to represent the base template for an enemy.
    ...

    Attributes
    ----------
    name: str
        The name of the enemy.
    health: int
        The health of the enemy.
    damage: int
        The base amount of damage dealt by the enemy.
    tpe: str
        The enemy's type (i.e. Rat, Goblin, Skeleton, Demon).
    multiplier: float
        The multiplier that affects the enemy's stats.
    ENEMY_TPE_MULT: {str: float}
        A dictionary to determine multiplier based on rarity.

    Methods
    -------
    check_dead()
        Checks if the instance of the enemy is dead.
    """
    ENEMY_TPE_MULT = {
        'Common': 1.0,
        'Elite': 2.0,
        'Boss': 4.0,
    }
    
    def __init__(self, name, tpe):
        """
        A function that is called immediately when an instance of this class is created. It initalizes all the attributes of the class.

        Parameters
        ----------
        name: str
            Name of the instance
        tpe: str
            The type of enemy (Rat, Goblin, Skeleton, Demon)
        
        Returns
        -------
        None
        """
        self.name = name
        self.tpe = tpe
        self.multiplier = self.ENEMY_TPE_MULT[tpe]
        
    def check_dead(self):
        """
        Function to check if the instance has died.
        
        Parameters
        ----------
        None

        Returns
        -------
        dead: boolean
            If the instance is dead, return True, else return False.
        """
        if self.health<=0:
            dead = True
        else:
            dead = False
        return dead

class Rat(Enemy):
    """
    A child class that inherits from the Enemy parent class.
    ...

    Added Attributes
    ----------------
    character: Character
        Instance of the Character class -> to be able to access its damage reduction
    multiplier: float
        Multiplier for all the rat's stats.
    health: int
        Amount of health the rat has.
    damage: int
        Amount of damage the rat has.
    exp: int
        Amount of exp the rat gives once dead.
    gold: int
        Amount of gold the rat gives once dead.

    Methods
    -------
    choose_ability()
        Chooses the ability that will be used with random.choices.
    bite()
        1st ability. Prints out a message for the ability and returns the amount of damage done.
    scratch()
        2nd ability. Prints out a message for the ability and returns the amount of damage done.
    """
    def __init__(self, name, tpe, character):
        """
        A function that is called immediately when an instance of this class is created. It initalizes all the attributes of the class.

        Parameters
        ----------
        name: str
            Name of the instance
        tpe: str
            The type of enemy (Rat, Goblin, Skeleton, Demon)
        character:
            The instance of the player's character
        
        Returns
        -------
        None
        """
        super().__init__(name, tpe)
        self.character=character
        self.multiplier = self.ENEMY_TPE_MULT[tpe]
        #Randomized health, damage, exp and gold -> not part of parameters because of needing to be multiplied by self.multiplier
        self.health = int(random.randint(50, 75) * self.multiplier)
        self.damage = int(random.randint(4, 5) * self.multiplier)
        self.exp = int(random.randint(8, 12) * self.multiplier)
        self.gold = int(random.randint(50, 100) * self.multiplier)

    def choose_ability(self):
        """
        Function to choose the ability used by the instance on a certain turn.
        
        Parameters
        ----------
        None

        Returns
        -------
        dmg: int
            Based on the called function. Returns the value that is produced by the chosen ability.
        OR
        "Dead": str
            If the instance is dead, this is returned.
        """
        #calling check_dead() here as well as safety/backup
        if not self.check_dead():
            # https://pynative.com/python-weighted-random-choices-with-probability/ for weighted values
            chosenAbility = random.choices(['Bite', 'Scratch'], weights = [60, 40], k=1) 
            #choosing ability randomly and returning damage
            if chosenAbility[0] == 'Bite':
                return self.bite()
            else:
                return self.scratch()
        else:
            return "DEAD"

    def bite(self):
        """
        Function to calculate the amount of damage dealt with the bite ability and print a damage message.
        
        Parameters
        ----------
        None

        Returns
        -------
        damage: int
            The amount of damage dealt by this ability
        """
        # https://pynative.com/python-get-random-float-numbers/ for random float
        # https://note.nkmk.me/en/python-math-floor-ceil-int/#:~:text=While%20math.,()%20instead%20rounds%20toward%20zero. -> rounding damage to integers
        #armor class applies damage reduction
        damage = int(self.multiplier * self.damage * random.uniform(0.8, 1.2) * (100/(100+self.character.armor_class)))
        print(self.name, "unhinges its mutated mandibles, snapping at your body. Its bite deals", damage, "damage.") 
        return damage
    
    def scratch(self):
        """
        Function to calculate the amount of damage dealt with the scratch ability and print a damage message.
        
        Parameters
        ----------
        None

        Returns
        -------
        damage: int
            The amount of damage dealt by this ability
        """
        damage = int(self.multiplier * self.damage * random.uniform(0.5, 1.5) * (100/(100+self.character.armor_class)))
        print("Pouncing on you,", self.name, "successfully scratches you with its sharp, jagged claws. You feel a sharp pain where you were scratched, receiving", damage, "damage.")
        return damage


class Goblin(Enemy):
    """
    A child class that inherits from the Enemy parent class.
    ...

    Added Attributes
    ----------------
    character: Character
        Instance of the Character class -> to be able to access its damage reduction
    multiplier: float
        Multiplier for all the rat's stats.
    health: int
        Amount of health the rat has.
    damage: int
        Amount of damage the rat has.
    exp: int
        Amount of exp the rat gives once dead.
    gold: int
        Amount of gold the rat gives once dead.

    Methods
    -------
    choose_ability()
        Chooses the ability that will be used with random.choices.
    stab()
        1st ability. Prints out a message for the ability and returns the amount of damage done.
    poison_dart()
        2nd ability. Prints out a message for the ability, returns the amount of damage done and applies a debuff to the character instance's status.
    """
    def __init__(self, name, tpe, character):
        """
        A function that is called immediately when an instance of this class is created. It initalizes all the attributes of the class.

        Parameters
        ----------
        name: str
            Name of the instance
        tpe: str
            The type of enemy (Rat, Goblin, Skeleton, Demon)
        character:
            The instance of the player's character
        
        Returns
        -------
        None
        """
        super().__init__(name, tpe)
        self.character=character
        self.multiplier = self.ENEMY_TPE_MULT[tpe]
        self.health = int(random.randint(75, 100) * self.multiplier)
        self.damage = int(random.randint(7, 8) * self.multiplier)
        self.exp = int(random.randint(15, 20) * self.multiplier)
        self.gold = int(random.randint(150, 200) * self.multiplier)

    def choose_ability(self):
        """
        Function to choose the ability used by the instance on a certain turn.
        
        Parameters
        ----------
        None

        Returns
        -------
        dmg: int
            Based on the called function. Returns the value that is produced by the chosen ability.
        OR
        "Dead": str
            If the instance is dead, this is returned.
        """
        if not self.check_dead():
            chosenAbility = random.choices(['Stab', 'Poison_dart'], weights = [70, 30], k=1) 
            if chosenAbility[0] == 'Stab':
                return self.stab()
            else:
                return self.poison_dart()
        else:
            return "DEAD"

    def stab(self):
        """
        Function to calculate the amount of damage dealt with the stab ability and print a damage message.
        
        Parameters
        ----------
        None

        Returns
        -------
        damage: int
            The amount of damage dealt by this ability
        """
        damage = int(self.multiplier * self.damage * random.uniform(1, 1.2) * (100/(100+self.character.armor_class)))
        print(self.name, "stabs forward, plunging his shoddy stone knife into your body. It deals", damage, "damage.")
        return damage
    
    def poison_dart(self):
        """
        Function to calculate the amount of damage dealt with the poison dart ability, apply a poison debuff on the character and print a damage message.
        
        Parameters
        ----------
        None

        Returns
        -------
        damage: int
            The amount of damage dealt by this ability
        """
        damage = int(self.multiplier * self.damage * random.uniform(0.3, 0.5) * (100/(100+self.character.armor_class)))
        #adds a poison debuff to the character
        if self.character.tabbar["Poison"]:
            self.character.tabbar["Poison"] += 1
        else:
            self.character.tabbar["Poison"] = 1
        print("A quick projectile shoots out of", self.name, "blowdart and glances off you dealing", damage, "damage. You observe yourself for a moment, thinking you were lucky until you start feeling dizzy...")
        print(" ~ You have been poisoned for 1 turn. ~ ")
        return damage
    

class Skeleton(Enemy):
    """
    A child class that inherits from the Enemy parent class.
    ...

    Added Attributes
    ----------------
    character: Character
        Instance of the Character class -> to be able to access its damage reduction
    multiplier: float
        Multiplier for all the rat's stats.
    health: int
        Amount of health the rat has.
    damage: int
        Amount of damage the rat has.
    exp: int
        Amount of exp the rat gives once dead.
    gold: int
        Amount of gold the rat gives once dead.
    used: boolean
        Variable to check if the revival passive has been used.

    Methods
    -------
    choose_ability()
        Chooses the ability that will be used with random.choices.
    slash()
        1st ability. Prints out a message for the ability and returns the amount of damage done.
    stun()
        2nd ability. Prints out a message for the ability, returns 0 and applies a debuff to the character instance's status.
    escape_death()
        Sets the instance's health to 1 after printing a message.
    """
    def __init__(self, name, tpe, character):
        """
        A function that is called immediately when an instance of this class is created. It initalizes all the attributes of the class.

        Parameters
        ----------
        name: str
            Name of the instance
        tpe: str
            The type of enemy (Rat, Goblin, Skeleton, Demon)
        character:
            The instance of the player's character
        
        Returns
        -------
        None
        """
        super().__init__(name, tpe)
        self.character=character
        self.multiplier = self.ENEMY_TPE_MULT[tpe]
        self.health = int(random.randint(75, 85) * self.multiplier)
        self.damage = int(random.randint(6, 7) * self.multiplier)
        self.exp = int(random.randint(25, 30) * self.multiplier)
        self.gold = int(random.randint(75, 125) * self.multiplier)
        #boolean for if passive was used
        self.used = False

    def choose_ability(self):
        """
        Function to choose the ability used by the instance on a certain turn.
        
        Parameters
        ----------
        None

        Returns
        -------
        dmg: int
            Based on the called function. Returns the value that is produced by the chosen ability.
        OR
        "Dead": str
            If the instance is dead, this is returned.
        """
        if not self.check_dead():
            chosenAbility = random.choices(['Slash', 'Stun'], weights = [50, 50], k=1) 
            if chosenAbility[0] == 'Slash':
                return self.slash()
            else:
                return self.stun()
        else:
            return "DEAD"

    def slash(self):
        """
        Function to calculate the amount of damage dealt with the slash ability and print a damage message.
        
        Parameters
        ----------
        None

        Returns
        -------
        damage: int
            The amount of damage dealt by this ability
        """
        damage = int(self.multiplier * self.damage * random.uniform(0.5, 2.5) * (100/(100+self.character.armor_class)))
        print(self.name, "swipes at you; you aren't sure with what but it looks to be a sharpened bone, possibly from its own body... You take", damage, "damage.")
        return damage
    
    def stun(self):
        """
        Function to apply a stun debuff on the character and print a message.
        
        Parameters
        ----------
        None

        Returns
        -------
        0: int
            This ability does no damage.
        """
        print(self.name, "lunges at you, disassembling and assembling itself, attempting to trap you.")
        #adds a stun debuff
        if self.character.tabbar["Stunned"]:
            self.character.tabbar["Stunned"] += 1
        else:
            self.character.tabbar["Stunned"] = 1
        return 0
    
    def escape_death(self):
        """
        Function to let the instance of this class survive once (will be called after health reaches 0).
        
        Parameters
        ----------
        None

        Returns
        -------
        None
        """
        print(self.name, "realizes its innate trait, avoiding the death which it has taunted for so long.")
        #sets health to 1 -> not dead
        self.health = 1
        

class Demon(Enemy):
    """
    A child class that inherits from the Enemy parent class.
    ...

    Added Attributes
    ----------------
    character: Character
        Instance of the Character class -> to be able to access its damage reduction
    multiplier: float
        Multiplier for all the rat's stats.
    health: int
        Amount of health the rat has.
    damage: int
        Amount of damage the rat has.
    exp: int
        Amount of exp the rat gives once dead.
    gold: int
        Amount of gold the rat gives once dead.

    Methods
    -------
    choose_ability()
        Chooses the ability that will be used with random.choices.
    weaken()
        1st ability. Prints out a message for the ability, returns the amount of damage done and puts a 'Weakened' debuff on the player's character. 
    poison_dart()
        2nd ability. Prints out a message for the ability and returns the amount of damage done. The damage done and message depends on if the character has been 'Weakened'.
    """
    def __init__(self, name, tpe, character):
        """
        A function that is called immediately when an instance of this class is created. It initalizes all the attributes of the class.

        Parameters
        ----------
        name: str
            Name of the instance
        tpe: str
            The type of enemy (Rat, Goblin, Skeleton, Demon)
        character:
            The instance of the player's character
        
        Returns
        -------
        None
        """
        super().__init__(name, tpe)
        self.character=character
        self.multiplier = self.ENEMY_TPE_MULT[tpe]
        self.health = int(random.randint(100, 175) * self.multiplier)
        self.damage = int(random.randint(10, 11) * self.multiplier)
        self.exp = int(random.randint(50, 100) * self.multiplier)
        self.gold = int(random.randint(500, 1000) * self.multiplier)


    def choose_ability(self):
        """
        Function to choose the ability used by the instance on a certain turn.
        
        Parameters
        ----------
        None

        Returns
        -------
        dmg: int
            Based on the called function. Returns the value that is produced by the chosen ability.
        OR
        "Dead": str
            If the instance is dead, this is returned.
        """
        if not self.check_dead():
            chosenAbility = random.choices(['Weaken', 'Hellfire'], weights = [25, 75], k=1) 
            if chosenAbility[0] == 'Weaken':
                return self.weaken()
            else:
                return self.hellfire()
        else:
            return "DEAD"

    def weaken(self):
        """
        Function to calculate the amount of damage dealt with the weaken ability, apply a weaken debuff on the character and print a damage message.
        
        Parameters
        ----------
        None

        Returns
        -------
        damage: int
            The amount of damage dealt by this ability
        """
        damage = int(self.multiplier * (self.damage + self.character.health*0.03) * random.uniform(0.5, 0.6) * (100/(100+self.character.armor_class)))
        #adds weaken debuff to character
        if self.character.tabbar["Weakened"]:
            self.character.tabbar["Weakened"] += 1
        else:
            self.character.tabbar["Weakened"] = 1
        print(self.name, "chants a spell and, before long, you hear a ringing sound which only continues to grow. It deals", damage, "damage.")
        print(" ~ You have been weakened for 1 turn. ~ ")
        return damage
    
    def hellfire(self):
        """
        Function to calculate the amount of damage dealt with the hellfire ability and print a damage message. The damage depends on if the character has been weakened (conditionals).
        
        Parameters
        ----------
        None

        Returns
        -------
        damage: int
            The amount of damage dealt by this ability
        """
        #if the character has been weakened -> more damage
        if self.character.tabbar["Weakened"]>0:
            damage = int(self.multiplier * random.uniform(1, 1.2) * 2.5 * (self.damage + self.character.health*0.05) * (100/(100+self.character.armor_class)))
            print(self.name, "burns you with hellfire which is strengthed by your weakness. The flames burn you for", damage, "damage.")
            self.character.tabbar["Weakened"]-=1
            return damage
        #if the character hasn't been weakened -> less damage
        else:
            damage = int(self.multiplier * random.uniform(1, 1.1) * (self.damage + self.character.health*0.025) * (100/(100+self.character.armor_class)))
            print(self.name, "curses, bemoaning the fact that you aren't weakened. His flames deal", damage, "damage.")
            return damage
