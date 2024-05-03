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
    def __init__(self, name, type):
        super().__init__(name=name, type=type)
        self.damage = 5*self.multiplier
        self.health = random.randint(50, 75)*self.multiplier

    def choose_ability(self):
        # https://pynative.com/python-weighted-random-choices-with-probability/ for weighted values
        chosenAbility = random.choices(['Bite', 'Scratch'], weights = [60, 40], k=1) 
        if chosenAbility == 'Bite':
            self.bite()
        else:
            self.scratch()

    def bite(self):
        # https://pynative.com/python-get-random-float-numbers/ for random float
        return self.multiplier * self.damage * random.uniform(0.8, 1.2)
    
    def scratch(self):
        return self.multiplier * self.damage * random.uniform(0.5, 1.5)


class Goblin(Enemy):
    #temp filler
    temp = 1

class Skeleton(Enemy):
    #temp filler
    temp = 1

class Demon(Enemy):
    #temp filler
    temp = 1
