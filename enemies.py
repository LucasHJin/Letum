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
        self.health = random.randint(50, 75) * self.multiplier
        self.damage = 5 * self.multiplier

    def choose_ability(self):
        if not self.check_dead():
            # https://pynative.com/python-weighted-random-choices-with-probability/ for weighted values
            chosenAbility = random.choices(['Bite', 'Scratch'], weights = [60, 40], k=1) 
            if chosenAbility == 'Bite':
                return self.bite()
            else:
                return self.scratch()
        else:
            return "DEAD"

    def bite(self):
        # https://pynative.com/python-get-random-float-numbers/ for random float
        damage = self.multiplier * self.damage * random.uniform(0.8, 1.2)
        print("The mutated rat unhinges his mandibles, snapping at your body. Its bite deals", damage, "damage.") #DONT FORGET TO ROUND LATERdamage = self.multiplier * self.damage * random.uniform(0.8, 1.2)
        return damage
    
    def scratch(self):
        damage = self.multiplier * self.damage * random.uniform(0.5, 1.5)
        print("Pouncing on you the rat successfully scratches you with its sharp, jagged claws. You feel a sharp pain where you were scratched, receiving", damage, "damage.")
        return damage
    
    def check_dead(self):
        if self.health<=0:
            dead = True
        else:
            dead = False
        return dead


class Goblin(Enemy):
    def __init__(self, name, tpe, character):
        super().__init__(name=name, tpe=tpe, health=random.randint(75, 100), damage=9)
        self.damage *= self.multiplier
        self.health *= self.multiplier
        self.character=character

    def choose_ability(self):
        if not self.check_dead():
            chosenAbility = random.choices(['Stab', 'Poison_dart'], weights = [70, 30], k=1) 
            if chosenAbility == 'Stab':
                return self.stab()
            else:
                return self.poison_dart()
        else:
            return "DEAD"

    def stab(self):
        damage = self.multiplier * self.damage * random.uniform(1, 1.2)
        print("The goblin stabs forward, plunging his shoddy stone knife into your body. It deals", damage, "damage.")
        return damage
    
    def poison_dart(self):
        damage = self.multiplier * self.damage * random.uniform(0.3, 0.5)
        if self.character.tabbar["Poison"]:
            self.character.tabbar["Poison"] += 1
        else:
            self.character.tabbar["Poison"] = 1
        print("A quick projectile shoots out of the goblin's blowdart and glances off you dealing", damage, "damage. You observe yourself for a moment, thinking you were lucky until you start feeling dizzy...")
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
        super().__init__(name=name, tpe=tpe, health=random.randint(75, 100), damage=7)
        self.damage *= self.multiplier
        self.health *= self.multiplier
        self.character=character
        self.used = False

    def choose_ability(self):
        if self.check_dead() and not self.used:
            self.used = True
            self.escape_death()
        if not self.check_dead():
            chosenAbility = random.choices(['Slash', 'Stun'], weights = [50, 50], k=1) 
            if chosenAbility == 'Slash':
                return self.slash()
            else:
                return self.block()
        else:
            return "DEAD"

    def slash(self):
        damage = self.multiplier * self.damage * random.uniform(0.5, 2.5)
        print("The skeleton swipes at you; you aren't sure with what but it looks to be a sharpened bone, possibly from its own body... You take", damage, "damage.")
        return damage
    
    def stun(self):
        print("The skeleton lunges at you, disassembling and assembling itself, trapping you for one turn.")
        if self.character.tabbar["Stunned"]:
            self.character.tabbar["Stunned"] += 1
        else:
            self.character.tabbar["Stunned"] = 1
        return 0
    
    def escape_death(self):
        print("The skeleton realizes its innate trait, avoiding the death with which it has taunted for so long.")
        self.health = 1
        
    def check_dead(self):
        if self.health<=0:
            dead = True
        else:
            dead = False
        return dead

class Demon(Enemy):
    def __init__(self, name, tpe, character):
        super().__init__(name=name, tpe=tpe, health=random.randint(100, 200), damage=10)
        self.damage *= self.multiplier
        self.health *= self.multiplier
        self.character=character


    def choose_ability(self):
        if not self.check_dead():
            chosenAbility = random.choices(['Weaken', 'Hellfire'], weights = [25, 75], k=1) 
            if chosenAbility == 'Weaken':
                return self.weaken()
            else:
                return self.hellfire()
        else:
            return "DEAD"

    def weaken(self):
        damage = self.multiplier * (self.damage + self.character.health*0.03) * random.uniform(0.5, 0.6)  
        if self.character.tabbar["Weakened"]:
            self.character.tabbar["Weakened"] += 1
        else:
            self.character.tabbar["Weakened"] = 1
        print("The demon chants a spell and, before long, you hear a ringing sound which only continues to grow. It deals", damage, "damage.")
        print(" ~ You have been weakened for 1 turn. ~ ")
        return damage
    
    def hellfire(self):
        if self.character.tabbar["Weakened"]>0:
            damage = self.multiplier * random.uniform(1, 1.2) * 2.5 * (self.damage + self.character.health*0.05)
            print("The demon burns you with hellfire which is strengthed by your weakness. The flames burn you for", damage, "damage.")
            return damage
        else:
            print("The demon curses, bemoaning the fact that you aren't weakened. His flames deal", damage, "damage.")
            damage = self.multiplier * random.uniform(1, 1.1) * (self.damage + self.character.health*0.025)
            print("")
            return damage

    def check_dead(self):
        if self.health<=0:
            dead = True
        else:
            dead = False
        return dead
