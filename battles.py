from enemies import Rat
from enemies import Goblin
from enemies import Skeleton
from enemies import Demon
import os

class Battle:
    def __init__(self, enemiesDict, character, weapon):
        self.enemiesDict = enemiesDict #dict with list of common, elite, boss numbers for each enemy
        self.character = character
        self.weapon = weapon
        self.turn_count = 1

    def entire_game(self):
        if self.turn_count == 1:
            ene_inst = self.create_enemy_instances()
        status = self.turn(ene_inst)
        while status != "DEAD" and status != "WON":
            os.system('cls')
            status = self.turn(status)

    def turn(self, en_inst): #REMEMBER ADD COOLDOWNS
        #have each enemy and character go once in a turn (loop iterate) AND check for death and if so remove that character
        print("  >>  Health:", self.character.health)
        if self.character.check_dead():
            print("Having taken too many blows, you succumb to your wounds.")
            return "DEAD"
        else:
            #player turn
            print("What do you want to do?")
            for i in range(len(self.weapon.abilityDict[self.weapon.rarity])-1):
                print("  ["+str(i+1)+"] "+self.weapon.abilityDict[self.weapon.rarity[i]])
            if self.character.inventory["Health Potion"]>0:
                print("  ["+str(i+2)+"] Use a Health Potion ("+str(self.character.inventory["Health Potion"])+"X)")
            choice = input("  >>  ")
            check_answer = False
            for j in range(i):
                if choice == str(j):
                    check_answer = True
            while not check_answer:
                print("That was not one of the options. The options are:")
                for i in range(len(self.weapon.abilityDict[self.weapon.rarity])):
                    print("  ["+str(i+1)+"] "+self.weapon.abilityDict[self.weapon.rarity[i]])
                if self.character.inventory["Health Potion"]>0:
                    print("  ["+str(i+2)+"] Use a Health Potion ("+str(self.character.inventory["Health Potion"])+"X)")
                choice = input("  >>  ")
                for j in range(i):
                    if choice == str(j):
                        check_answer = True
            choice_action = self.weapon.abilityDict[self.weapon.rarity[int(choice)-1]]
            if choice_action == "Slash":
                dmg = self.weapon.slash()
            elif choice_action == "Wide Slash":
                dmg = self.weapon.wide_slash()
            elif choice_action == "Holy Blow":
                dmg = self.weapon.holy_blow()
            elif choice_action == "Holy Aura":
                dmg = self.weapon.holy_aura()
            else:
                dmg = 0
                self.character.use_health_potion()
            if choice_action == "Wide Slash":
                for enemy_key in self.enemiesDict:
                    for inst in en_inst[enemy_key]:
                        inst.health -= dmg
            elif choice_action != "HP":
                print("Who do you wish to attack?")
                for enemy_key in self.enemiesDict:
                    for inst in en_inst[enemy_key]:
                        print("  ["+inst.name+"] -> Current Health:", inst.health, "(Make sure to type the name exactly as displayed.)")
                who = input("  >>  ")
                chosen = False
                for enemy_key in self.enemiesDict:
                    for inst in en_inst[enemy_key]:
                        if inst.name == who:
                            chosen = True
                while not chosen:
                    print("That was not the option. The options are: ")
                    for enemy_key in self.enemiesDict:
                        for inst in en_inst[enemy_key]:
                            print("  ["+inst.name+"] -> Current Health:", inst.health, "(Make sure to type the name exactly as displayed.)")
                    who = input("  >>  ")
                    for enemy_key in self.enemiesDict:
                        for inst in en_inst[enemy_key]:
                            if inst.name == who:
                                chosen = True
                for enemy_key in self.enemiesDict:
                    for inst in en_inst[enemy_key]:
                        if inst.name == who:
                            inst.health -= dmg
        #enemy turn
        for enemy_key in self.enemiesDict:
            for inst in en_inst[enemy_key]:
                if inst.check_dead:
                    if not isinstance(Skeleton, inst): #https://www.toppr.com/guides/python-guide/references/methods-and-functions/methods/built-in/isinstance/python-isinstance-2/#:~:text=The%20isinstance%20()%20function%20checks,parent%20class%20of%20an%20object.
                        en_inst[enemy_key.remove(inst)] #https://www.w3schools.com/python/python_lists_remove.asp
                    else:
                        if not inst.used:
                            inst.used = True
                            inst.escape_death()
                        else:
                            en_inst[enemy_key.remove(inst)]
        
        total_left = 0
        for enemy_key in self.enemiesDict:
            total_left += len(self.enemiesDict[enemy_key])
        if total_left == 0:
            return "WON"

        for enemy_key in self.enemiesDict:
            for inst in en_inst[enemy_key]:
                if not inst.check_dead:
                    enemy_dmg = inst.choose_ability()
                    self.character.current_health -= enemy_dmg

        return en_inst

            

    def create_enemy_instances(self):
        enemy_instances = {
            'Rat': [],
            'Goblin': [],
            'Skeleton': [],
            'Demon': []
        }
        for enemy_key in self.enemiesDict:
            enemy_amount = 0
            for type_amount in self.enemiesDict[enemy_key]:
                counter = 1
                for count in range(type_amount):
                    #https://www.w3schools.com/python/ref_string_format.asp -> for naming instance
                    instance_name = "{}{}".format(enemy_key, count)
                    if enemy_key == "Rat":
                        if counter == 1:
                            instance = Rat(instance_name, "Common", self.character)
                        elif counter == 2:
                            instance = Rat(instance_name, "Elite", self.character)
                        else:
                            instance = Rat(instance_name, "Boss", self.character)
                        enemy_instances['Rat'].append(instance)
                    elif enemy_key == "Goblin":
                        if counter == 1:
                            instance = Goblin(instance_name, "Common", self.character)
                        elif counter == 2:
                            instance = Goblin(instance_name, "Elite", self.character)
                        else:
                            instance = Goblin(instance_name, "Boss", self.character)
                        enemy_instances['Goblin'].append(instance)
                    elif enemy_key == "Skeleton":
                        if counter == 1:
                            instance = Skeleton(instance_name, "Common", self.character)
                        elif counter == 2:
                            instance = Skeleton(instance_name, "Elite", self.character)
                        else:
                            instance = Skeleton(instance_name, "Boss", self.character)
                        enemy_instances['Skeleton'].append(instance)
                    else:
                        if counter == 1:
                            instance = Demon(instance_name, "Common", self.character)
                        elif counter == 2:
                            instance = Demon(instance_name, "Elite", self.character)
                        else:
                            instance = Demon(instance_name, "Boss", self.character)
                        enemy_instances['Demon'].append(instance)
                counter+=1
        return enemy_instances

