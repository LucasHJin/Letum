from enemies import Rat
from enemies import Goblin
from enemies import Skeleton
from enemies import Demon
import os
import math
import random

#TO DO:
'''
ENEMIES DROP GOLD AND ARMOUR?!!!
'''

class Battle:
    def __init__(self, enemiesDict, character, weapon):
        self.enemiesDict = enemiesDict #dict with list of common, elite, boss numbers for each enemy
        self.character = character
        self.weapon = weapon
        self.turn_count = 1

    def entire_game(self):
        if self.turn_count == 1:
            ene_inst = self.create_enemy_instances()
        print("Looking into the distance, you see:")
        for enemy_key in self.enemiesDict:
            counter = 0
            for amount_enemies in self.enemiesDict[enemy_key]:
                if counter==0:
                    print("  [X"+str(amount_enemies)+"]", "Common", enemy_key)
                elif counter==1:
                    print("  [X"+str(amount_enemies)+"]", "Elite", enemy_key)
                else:
                    print("  [X"+str(amount_enemies)+"]", "Boss", enemy_key)
        status = self.turn(ene_inst)
        while status != "DEAD" and status != "WON":
            input("[Press any key to continue.]")
            os.system('cls')
            status = self.turn(status)
        if status == "DEAD":
            return "DEAD"
        else:
            #refresh hp
            self.character.refresh_current_health()
            #level up
            if self.character.exp>self.character.needed_exp:
                self.character.all_level_up()
            return "WON"

    def turn(self, en_inst): 
        #player turn
        print("\nYour Turn:")
        print("{---------------------------------------------------------------}")
        dodge_stun = 0
        self.character.check_status_bar()
        print("  >>  Health:", self.character.current_health)
        for ability_cooldown in self.weapon.cooldownsDict:
            if self.weapon.cooldownsDict[ability_cooldown]>0:
                self.weapon.cooldownsDict[ability_cooldown] -= 1


        for ability_cooldown in self.weapon.cooldownsDict:
            print(ability_cooldown, self.weapon.cooldownsDict[ability_cooldown])


        #case 1: dead
        if self.character.check_dead():
            print("Having taken too many blows, you succumb to your wounds.")
            return "DEAD"
        #case 2: check stunned
        elif self.character.tabbar["Stunned"]>0:
            PROBABILITY_FACTOR = 2/3
            #https://www.w3schools.com/python/ref_math_log.asp
            probability = PROBABILITY_FACTOR * math.log(self.character.tabbar["Stunned"]+1)
            #check if skip turn based off probability
            if random.random() <= probability:
                print("You were immobilized and lose 1 turn.")
                dodge_stun = 1
            else:
                print("You dodge the skeleton and avoid being caught between their ribgcages.")
            self.character.tabbar["Stunned"]=0
        #case 3: normal turn
        if (self.character.tabbar["Stunned"]==0 and dodge_stun==0):
            print("What do you want to do?")
            for i in range(len(self.weapon.abilityDict[self.weapon.rarity])-1):
                if self.weapon.cooldownsDict[self.weapon.abilityDict[self.weapon.rarity][i]]==0:
                    print("  ["+str(i+1)+"] "+self.weapon.abilityDict[self.weapon.rarity][i])
                else:
                    print("X ["+str(i+1)+"] "+self.weapon.abilityDict[self.weapon.rarity][i], "→", self.weapon.cooldownsDict[self.weapon.abilityDict[self.weapon.rarity][i]], "turn cooldown remaining")
            if self.character.inventory["Health Potion"]>0 and self.character.current_health != self.character.health:
                print("  ["+str(i+2)+"] Use a Health Potion ("+str(self.character.inventory["Health Potion"])+"X)")
            print("  [V] View the enemy")
            choice = input("  >>  ")
            if not choice.isdigit():
                if choice.lower() == "v":
                    print("{---------------------------------------------------------------}")
                    print("Enemy:")
                    for enemy_key in self.enemiesDict:
                        for inst in en_inst[enemy_key]:
                            print("  ["+inst.name+"] - Current Health:", inst.health)
                    input("[Enter any key to continue.]")
                    print("{---------------------------------------------------------------}")
            check_answer = False
            for j in range(len(self.weapon.abilityDict[self.weapon.rarity])):
                if choice == str(j+1):
                    if choice != str(len(self.weapon.abilityDict[self.weapon.rarity])):
                        #reorganized into 2 if statements instead of and for legibility
                        if self.weapon.cooldownsDict[self.weapon.abilityDict[self.weapon.rarity][int(choice)-1]]==0:
                            check_answer = True
                    else:
                        if self.character.inventory["Health Potion"] > 0 and self.character.current_health != self.character.health:
                            check_answer = True
            while not check_answer:
                print("Enter a new choice. The options are:")
                for i in range(len(self.weapon.abilityDict[self.weapon.rarity])-1):
                    if self.weapon.cooldownsDict[self.weapon.abilityDict[self.weapon.rarity][i]]==0:
                        print("  ["+str(i+1)+"] "+self.weapon.abilityDict[self.weapon.rarity][i])
                    else:
                        print("X ["+str(i+1)+"] "+self.weapon.abilityDict[self.weapon.rarity][i], "→", self.weapon.cooldownsDict[self.weapon.abilityDict[self.weapon.rarity][i]], "turn cooldown remaining")
                if self.character.inventory["Health Potion"]>0 and self.character.current_health != self.character.health:
                    print("  ["+str(i+2)+"] Use a Health Potion ("+str(self.character.inventory["Health Potion"])+"X)")
                print("  [V] View the enemy")
                choice = input("  >>  ")
                if not choice.isdigit():
                    if choice.lower() == "v":
                        print("{---------------------------------------------------------------}")
                        print("Enemy:")
                        for enemy_key in self.enemiesDict:
                            for inst in en_inst[enemy_key]:
                                print("  ["+inst.name+"] - Current Health:", inst.health)
                        input("[Enter any key to continue.]")
                        print("{---------------------------------------------------------------}")
                for j in range(len(self.weapon.abilityDict[self.weapon.rarity])):
                    if choice == str(j+1):
                        if choice != str(len(self.weapon.abilityDict[self.weapon.rarity])):
                            if self.weapon.cooldownsDict[self.weapon.abilityDict[self.weapon.rarity][int(choice)-1]]==0:
                                check_answer = True
                        else:
                            if self.character.inventory["Health Potion"] > 0 and self.character.current_health != self.character.health:
                                check_answer = True
            choice_action = self.weapon.abilityDict[self.weapon.rarity][int(choice)-1]
            if choice_action == "Slash":
                dmg = self.weapon.slash()
            elif choice_action == "Wide Slash":
                dmg = self.weapon.wide_slash()
                self.weapon.cooldownsDict[choice_action]=3
            elif choice_action == "Holy Blow":
                dmg = self.weapon.holy_blow()
                self.weapon.cooldownsDict[choice_action]=3
            elif choice_action == "Holy Aura":
                dmg = self.weapon.holy_aura()
                self.weapon.cooldownsDict[choice_action]=4
                print("You call upon the holy power of the Gods and buff yourself.")
                print(" ~ All your stats have been increased by 5 for 2 turns. ~ ")
                print("  >>  Strength:", self.character.stats['str'], "→", self.character.stats['str']+5)
                print("  >>  Dexterity:", self.character.stats['dex'], "→", self.character.stats['dex']+5)
                print("  >>  Constitution:", self.character.stats['con'], "→", self.character.stats['con']+5)
            elif choice_action == "HP" and self.character.inventory["Health Potion"]>0 and self.character.current_health!=self.character.health:
                dmg = 0
                self.character.use_health_potion()
            if choice_action == "Wide Slash":
                for enemy_key in self.enemiesDict:
                    for inst in en_inst[enemy_key]:
                        inst.health -= dmg
                print("Throwing a wide slash, you hit all the enemies, dealing", dmg, "damage to each one of them.")
            elif choice_action != "HP" and choice_action != "Holy Aura":
                print("Who do you wish to attack? (Make sure to type the name exactly as displayed.)")
                for enemy_key in self.enemiesDict:
                    for inst in en_inst[enemy_key]:
                        print("  ["+inst.name+"] - Current Health:", inst.health)
                who = input("  >>  ")
                chosen = False
                for enemy_key in self.enemiesDict:
                    for inst in en_inst[enemy_key]:
                        if inst.name == who:
                            chosen = True
                while not chosen:
                    print("That was not the option. (Make sure to type the name exactly as displayed.) The options are: ")
                    for enemy_key in self.enemiesDict:
                        for inst in en_inst[enemy_key]:
                            print("  ["+inst.name+"] -> Current Health:", inst.health)
                    who = input("  >>  ")
                    for enemy_key in self.enemiesDict:
                        for inst in en_inst[enemy_key]:
                            if inst.name == who:
                                chosen = True
                for enemy_key in self.enemiesDict:
                    for inst in en_inst[enemy_key]:
                        if inst.name == who:
                            inst.health -= dmg
                if choice_action == "Slash":
                    print("You slash your sword through the enemy's grotesque cadaver. You deal", dmg, "damage.")
                elif choice_action == "Holy Blow":
                    print("Smiting the enemy down, you deal", dmg, "damage.")
            
        for enemy_key in self.enemiesDict: 
            #iterate over copy -> no uninteded problems if multiple enemies are killed at the same time
            for inst in list(en_inst[enemy_key]):
                if inst.check_dead():
                    #https://www.toppr.com/guides/python-guide/references/methods-and-functions/methods/built-in/isinstance/python-isinstance-2/#:~:text=The%20isinstance%20()%20function%20checks,parent%20class%20of%20an%20object.
                    if not isinstance(inst, Skeleton): 
                        #https://www.w3schools.com/python/python_lists_remove.asp
                        print(" ~ Congratulations, you have slain an enemy! ["+inst.name+"] ~ ")
                        print(" ~ +"+str(int(inst.exp))+" experience ~ ")
                        self.character.exp = int(self.character.exp+inst.exp)
                        en_inst[enemy_key].remove(inst) 
                    else:
                        if not inst.used:
                            inst.used = True
                            inst.escape_death()
                        else:
                            print(" ~ You have overcome a skeleton's innate trait and slain them. ["+inst.name+"] ~ ")
                            print(" ~ +"+str(int(inst.exp))+" experience ~ ")
                            self.character.needed_exp += inst.exp
                            en_inst[enemy_key].remove(inst)

        print("{---------------------------------------------------------------}")
        input("[Press any key to continue.]\n")

        #check if won
        total_left = 0
        for enemy_key in self.enemiesDict:
            total_left += len(en_inst[enemy_key])
        if total_left == 0:
            return "WON"

        #enemy turn
        print("Enemy's turn")
        print("{---------------------------------------------------------------}")
        for enemy_key in self.enemiesDict:
            for inst in en_inst[enemy_key]:
                if not inst.check_dead():
                    enemy_dmg = inst.choose_ability()
                    self.character.current_health -= enemy_dmg
        print("{---------------------------------------------------------------}")


        return en_inst

            

    def create_enemy_instances(self):
        enemy_instances = {
            'Rat': [],
            'Goblin': [],
            'Skeleton': [],
            'Demon': []
        }
        ENEMY_LVL = ['Common', 'Elite', 'Boss']
        for enemy_key in self.enemiesDict:
            enemy_amount = 0
            counter = 0 #counter for each individual type
            for type_amount in self.enemiesDict[enemy_key]:
                for count in range(type_amount):
                    #https://www.w3schools.com/python/ref_string_format.asp -> for naming instance
                    instance_name = "{} {} #{}".format(ENEMY_LVL[counter], enemy_key, count+1)
                    if enemy_key == "Rat":
                        if counter == 0:
                            instance = Rat(instance_name, "Common", self.character)
                        elif counter == 1:
                            instance = Rat(instance_name, "Elite", self.character)
                        else:
                            instance = Rat(instance_name, "Boss", self.character)
                        enemy_instances['Rat'].append(instance)
                    elif enemy_key == "Goblin":
                        if counter == 0:
                            instance = Goblin(instance_name, "Common", self.character)
                        elif counter == 1:
                            instance = Goblin(instance_name, "Elite", self.character)
                        else:
                            instance = Goblin(instance_name, "Boss", self.character)
                        enemy_instances['Goblin'].append(instance)
                    elif enemy_key == "Skeleton":
                        if counter == 0:
                            instance = Skeleton(instance_name, "Common", self.character)
                        elif counter == 1:
                            instance = Skeleton(instance_name, "Elite", self.character)
                        else:
                            instance = Skeleton(instance_name, "Boss", self.character)
                        enemy_instances['Skeleton'].append(instance)
                    else:
                        if counter == 0:
                            instance = Demon(instance_name, "Common", self.character)
                        elif counter == 1:
                            instance = Demon(instance_name, "Elite", self.character)
                        else:
                            instance = Demon(instance_name, "Boss", self.character)
                        enemy_instances['Demon'].append(instance)
                counter+=1
        return enemy_instances

