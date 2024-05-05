import random

class Enemy:
    ENEMY_TYPE_MULT = {
        'Common': 1.0,
        'Elite': 2.0,
        'Boss': 4.0,
        'Final Boss': 8.0
    }
    
    def __init__(self, name, health, damage, type):
        self.name = name
        self.health = health
        self.damage = damage
        self.type = type
        self.multiplier = self.RARITY_MULT[type]

class Rats(Enemy):
    def __init__(self, name, type, character):
        super().__init__(name=name, type=type)
        self.damage = 5*self.multiplier
        self.health = random.randint(50, 75)*self.multiplier
        self.character=character

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
        return self.multiplier * self.damage * random.uniform(0.8, 1.2)
    
    def scratch(self):
        return self.multiplier * self.damage * random.uniform(0.5, 1.5)
    
    def check_dead(self):
        if self.health<=0:
            dead = True
        else:
            dead = False
        return dead


class Goblin(Enemy):
    def __init__(self, name, type, character):
        super().__init__(name=name, type=type)
        self.damage = 8*self.multiplier
        self.health = random.randint(75, 100)*self.multiplier
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
        return self.multiplier * self.damage * random.uniform(1, 1.2)
    
    def poison_dart(self):
        if self.character.tabbar["Poison"]:
            self.character.tabbar["Poison"] += 1
        else:
            self.character.tabbar["Poison"] = 1
        return self.multiplier * self.damage * random.uniform(0.3, 0.5)
    
    def check_dead(self):
        if self.health<=0:
            dead = True
        else:
            dead = False
        return dead

class Skeleton(Enemy):
    def __init__(self, name, type, character):
        super().__init__(name=name, type=type)
        self.damage = 8*self.multiplier
        self.health = random.randint(75, 100)*self.multiplier
        self.character=character

    def choose_ability(self):
        if self.health<=0:
            self.escape_death()
        if not self.check_dead():
            chosenAbility = random.choices(['Slash', 'Block'], weights = [50, 50], k=1) 
            if chosenAbility == 'Slash':
                return self.slash()
            else:
                return self.block()
        else:
            return "DEAD"

    def slash(self):
        return self.multiplier * self.damage * random.uniform(0.5, 2.5)
    
    def block(self):
        if self.character.tabbar["Blocked"]:
            self.character.tabbar["Blocked"] += 1
        else:
            self.character.tabbar["Blocked"] = 1
    
    def escape_death(self):
        self.health = 1
        
    def check_dead(self):
        if self.health<=0:
            dead = True
        else:
            dead = False
        return dead

class Demon(Enemy):
    def __init__(self, name, type, character):
        super().__init__(name=name, type=type)
        self.damage = 8*self.multiplier
        self.health = random.randint(75, 100)*self.multiplier
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
        if self.character.tabbar["Weakened"]:
            self.character.tabbar["Weakened"] += 1
        else:
            self.character.tabbar["Weakened"] = 1
        return self.multiplier * (self.damage + self.character.health*0.03) * random.uniform(0.5, 0.6)  
    
    def hellfire(self):
        if self.character.tabbar["Weakened"]>0:
            return self.multiplier * random.uniform(1, 1.2) * 2.5 * (self.damage + self.character.health*0.05)
        else:
            return self.multiplier * random.uniform(1, 1.1) * (self.damage + self.character.health*0.025)

    def check_dead(self):
        if self.health<=0:
            dead = True
        else:
            dead = False
        return dead
