"""
Final Project
ICS3U
Lucas Jin

History:

"""

import random

class Enemy:
    ENEMY_TPE_MULT = {
        'Common': 1.0,
        'Elite': 2.0,
        'Boss': 4.0,
    }
    
    def __init__(self, name, health, damage, tpe):
        self.name = name
        self.health = health
        self.damage = damage
        self.tpe = tpe
        self.multiplier = self.ENEMY_TPE_MULT[tpe]

class Rat(Enemy):
    def __init__(self, name, tpe, character):
        #super().__init__(name=name, tpe=tpe, multiplier=self.ENEMY_TPE_MULT[tpe], health=random.randint(50, 75)*multiplier, damage=5*multiplier)
        self.name = name
        self.tpe = tpe
        self.character=character
        self.multiplier = self.ENEMY_TPE_MULT[tpe]
        self.health = int(random.randint(50, 75) * self.multiplier)
        self.damage = random.randint(4, 5) * self.multiplier
        self.exp = random.randint(8, 12) * self.multiplier
        self.gold = random.randint(50, 100) * self.multiplier

    def choose_ability(self):
        if not self.check_dead():
            # https://pynative.com/python-weighted-random-choices-with-probability/ for weighted values
            chosenAbility = random.choices(['Bite', 'Scratch'], weights = [60, 40], k=1) 
            if chosenAbility[0] == 'Bite':
                return self.bite()
            else:
                return self.scratch()
        else:
            return "DEAD"

    def bite(self):
        # https://pynative.com/python-get-random-float-numbers/ for random float
        # https://note.nkmk.me/en/python-math-floor-ceil-int/#:~:text=While%20math.,()%20instead%20rounds%20toward%20zero. -> rounding damage to integers
        damage = int(self.multiplier * self.damage * random.uniform(0.8, 1.2) * (100/(100+self.character.armor_class)))
        print(self.name, "unhinges its mutated mandibles, snapping at your body. Its bite deals", damage, "damage.") #DONT FORGET TO ROUND LATERdamage = self.multiplier * self.damage * random.uniform(0.8, 1.2)
        return damage
    
    def scratch(self):
        damage = int(self.multiplier * self.damage * random.uniform(0.5, 1.5) * (100/(100+self.character.armor_class)))
        print("Pouncing on you,", self.name, "successfully scratches you with its sharp, jagged claws. You feel a sharp pain where you were scratched, receiving", damage, "damage.")
        return damage
    
    def check_dead(self):
        if self.health<=0:
            dead = True
        else:
            dead = False
        return dead


class Goblin(Enemy):
    def __init__(self, name, tpe, character):
        self.name = name
        self.tpe = tpe
        self.character=character
        self.multiplier = self.ENEMY_TPE_MULT[tpe]
        self.health = int(random.randint(75, 100) * self.multiplier)
        self.damage = random.randint(7, 8) * self.multiplier
        self.exp = random.randint(15, 20) * self.multiplier
        self.gold = random.randint(150, 200) * self.multiplier

    def choose_ability(self):
        if not self.check_dead():
            chosenAbility = random.choices(['Stab', 'Poison_dart'], weights = [70, 30], k=1) 
            if chosenAbility[0] == 'Stab':
                return self.stab()
            else:
                return self.poison_dart()
        else:
            return "DEAD"

    def stab(self):
        damage = int(self.multiplier * self.damage * random.uniform(1, 1.2) * (100/(100+self.character.armor_class)))
        print(self.name, "stabs forward, plunging his shoddy stone knife into your body. It deals", damage, "damage.")
        return damage
    
    def poison_dart(self):
        damage = int(self.multiplier * self.damage * random.uniform(0.3, 0.5) * (100/(100+self.character.armor_class)))
        if self.character.tabbar["Poison"]:
            self.character.tabbar["Poison"] += 1
        else:
            self.character.tabbar["Poison"] = 1
        print("A quick projectile shoots out of", self.name, "blowdart and glances off you dealing", damage, "damage. You observe yourself for a moment, thinking you were lucky until you start feeling dizzy...")
        print(" ~ You have been poisoned for 1 turn. ~ ")
        return damage
    
    def check_dead(self):
        if self.health<=0:
            dead = True
        else:
            dead = False
        return dead

class Skeleton(Enemy):
    def __init__(self, name, tpe, character):
        self.name = name
        self.tpe = tpe
        self.character=character
        self.multiplier = self.ENEMY_TPE_MULT[tpe]
        self.health = int(random.randint(75, 85) * self.multiplier)
        self.damage = random.randint(6, 7) * self.multiplier
        self.exp = random.randint(25, 30) * self.multiplier
        self.used = False
        self.gold = random.randint(75, 125) * self.multiplier

    def choose_ability(self):
        """
        if self.check_dead() and not self.used:
            self.used = True
            self.escape_death()
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
        damage = int(self.multiplier * self.damage * random.uniform(0.5, 2.5) * (100/(100+self.character.armor_class)))
        print(self.name, "swipes at you; you aren't sure with what but it looks to be a sharpened bone, possibly from its own body... You take", damage, "damage.")
        return damage
    
    def stun(self):
        print(self.name, "lunges at you, disassembling and assembling itself, attempting to trap you.")
        if self.character.tabbar["Stunned"]:
            self.character.tabbar["Stunned"] += 1
        else:
            self.character.tabbar["Stunned"] = 1
        return 0
    
    def escape_death(self):
        print(self.name, "realizes its innate trait, avoiding the death which it has taunted for so long.")
        self.health = 1
        
    def check_dead(self):
        if self.health<=0:
            dead = True
        else:
            dead = False
        return dead

class Demon(Enemy):
    def __init__(self, name, tpe, character):
        self.name = name
        self.tpe = tpe
        self.character=character
        self.multiplier = self.ENEMY_TPE_MULT[tpe]
        self.health = int(random.randint(100, 175) * self.multiplier)
        self.damage = random.randint(10, 11) * self.multiplier
        self.exp = random.randint(50, 100) * self.multiplier
        self.gold = random.randint(500, 1000) * self.multiplier


    def choose_ability(self):
        if not self.check_dead():
            chosenAbility = random.choices(['Weaken', 'Hellfire'], weights = [25, 75], k=1) 
            if chosenAbility[0] == 'Weaken':
                return self.weaken()
            else:
                return self.hellfire()
        else:
            return "DEAD"

    def weaken(self):
        damage = int(self.multiplier * (self.damage + self.character.health*0.03) * random.uniform(0.5, 0.6) * (100/(100+self.character.armor_class)))
        if self.character.tabbar["Weakened"]:
            self.character.tabbar["Weakened"] += 1
        else:
            self.character.tabbar["Weakened"] = 1
        print(self.name, "chants a spell and, before long, you hear a ringing sound which only continues to grow. It deals", damage, "damage.")
        print(" ~ You have been weakened for 1 turn. ~ ")
        return damage
    
    def hellfire(self):
        if self.character.tabbar["Weakened"]>0:
            damage = int(self.multiplier * random.uniform(1, 1.2) * 2.5 * (self.damage + self.character.health*0.05) * (100/(100+self.character.armor_class)))
            print(self.name, "burns you with hellfire which is strengthed by your weakness. The flames burn you for", damage, "damage.")
            self.character.tabbar["Weakened"]-=1
            return damage
        else:
            damage = int(self.multiplier * random.uniform(1, 1.1) * (self.damage + self.character.health*0.025) * (100/(100+self.character.armor_class)))
            print(self.name, "curses, bemoaning the fact that you aren't weakened. His flames deal", damage, "damage.")
            return damage

    def check_dead(self):
        if self.health<=0:
            dead = True
        else:
            dead = False
        return dead
