"""
Final Project
ICS3U
Lucas Jin
This file declares the Battle class for battling with all the necessary methods and attributes. One instance of this class will be initialized in main to call all battles within the program.
History:
    April 13, 2024: Program Creation
    May 25, 2024: Adding Comments
"""

from enemies import Rat
from enemies import Goblin
from enemies import Skeleton
from enemies import Demon
import os
import math
import random


class Battle:
    """
    A Battle class that will simulate each of the battles in the game with its methods.
    ...

    Attributes
    ----------
    enemiesDict: {str: [int]}
        A dictionary with keys based on the enemies names and values corresponding to the amount of enemies of each rarity (the values are lists of length 3, divided into common, elite and boss numbers)
    character: Character
        The instance of Character used by the player. To access its attributes like current health.
    weapon: Sword
        The instance of Sword used by the player. To access its attributes and methods like its abilities.
    shop: Shop
        The instance of Shop that is initialized at the start of the program. To access its ability to create items.
    turn_count: int 
        Counting each turn within a single round.
    round_count: int
        Counting each round.
        
    Methods
    -------
    one_round()
        Function to simulate one entire round of battle. It ends when the player dies or kills all enemies, returning either "WON or "DEAD".
    turn(en_inst)
        Function to simulate one turn of a battle. It will be called repeatedly in one_round().
    create_enemy_instances()
        Creates all the enemy instances for the round. Is called once at the beginning of one_round().
    """
    
    def __init__(self, enemiesDict, character, weapon, shop):
        """
        A function that is called immediately when an instance of this class is created. It initalizes all the attributes of the class.

        Parameters
        ----------
        enemiesDict: {str: [int]}
            A dictionary that dictates how many of each type of enemy and rarity of enemy is created.
        character: Character   
            The instance of the character.
        weapon: Sword
            The instance of the weapon.
        shop: Shop
            The instnace of the shop.
        
        Returns
        -------
        None
        """
        self.enemiesDict = enemiesDict 
        self.character = character
        self.weapon = weapon
        self.shop = shop
        self.turn_count = 1
        self.round_count = 1
        

    def one_round(self):
        """
        A function that simulates an entire round until either the player dies or all the enemies have been killed.

        Parameters
        ----------
        None
        
        Returns
        -------
        "WON": str
            Returned if the round has ended (all enemies have died) while the character is still alive
        OR
        "DEAD": str
            Returned if the character has died.
        """
        os.system('cls')
        print("ROUND", self.round_count)
        print("{---------------------------------------------------------------}")
        if self.turn_count == 1:
            ene_inst = self.create_enemy_instances()
        print("Looking into the distance, you see:")
        for enemy_key in self.enemiesDict:
            counter = 0
            for amount_enemies in self.enemiesDict[enemy_key]:
                if counter==0:
                    if amount_enemies != 0:
                        print("  [X"+str(amount_enemies)+"]", "Common", enemy_key)
                elif counter==1:
                    if amount_enemies != 0:
                        print("  [X"+str(amount_enemies)+"]", "Elite", enemy_key)
                else:
                    if amount_enemies != 0:
                        print("  [X"+str(amount_enemies)+"]", "Boss", enemy_key)
                counter += 1
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
            #refresh cooldowns
            for ability_cooldown in self.weapon.cooldownsDict:
                self.weapon.cooldownsDict[ability_cooldown] = 0
            #increment round count by 1
            self.round_count += 1
            return "WON"

    def turn(self, en_inst): 
        """
        A function that simulates 1 turn within a round. It accounts for both the player's and the enemy's turns.

        Parameters
        ----------
        en_inst: {str: [Rat/Goblin/Skeleton/Demon]}
            A dictionary containing all the enemy types as keys with their values being lists filled with all the enemy instances of that type.
        
        Returns
        -------
        en_inst: {str: [Rat/Goblin/Skeleton/Demon]}
            A dictionary containing all the enemy types as keys with their values being lists filled with all the enemy instances of that type.
            (Returning so that if an enemy dies for example, it stays dead the next time turn is called)
        """
        CONVERSION_DICT = {
            'Rat': 'r',
            'Goblin': 'g',
            'Skeleton': 's',
            'Demon': 'd'
        }
        RCONVERSION_DICT = {
            'r': 'Rat',
            'g': 'Goblin',
            's': 'Skeleton',
            'd': 'Demon'
        }
        POSSIBLE_LETTER = ['r', 'g', 's', 'd']
        RARITY_DROP_CHANCE = {
            'Common': 1.0,
            'Elite': 2.0,
            'Boss': 3.0,
        }
        TYPE_DROP_CHANCE = {
            "Rat": 1.0,
            "Goblin": 1.5,
            "Skeleton": 2.0,
            "Demon": 2.5
        }
        #player turn
        print("\nYour Turn:")
        print("{---------------------------------------------------------------}")
        dodge_stun = 0
        self.character.apply_status()
        print("  >>  Health:", self.character.current_health)
        for ability_cooldown in self.weapon.cooldownsDict:
            if self.weapon.cooldownsDict[ability_cooldown]>0:
                self.weapon.cooldownsDict[ability_cooldown] -= 1

        """
        for ability_cooldown in self.weapon.cooldownsDict:
            print(ability_cooldown, self.weapon.cooldownsDict[ability_cooldown])
        """


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
            for i in range(len(self.weapon.ABILITY_DICT[self.weapon.rarity])-1):
                if self.weapon.cooldownsDict[self.weapon.ABILITY_DICT[self.weapon.rarity][i]]==0:
                    print("  ["+str(i+1)+"] "+self.weapon.ABILITY_DICT[self.weapon.rarity][i])
                else:
                    print("X ["+str(i+1)+"] "+self.weapon.ABILITY_DICT[self.weapon.rarity][i], "→", self.weapon.cooldownsDict[self.weapon.ABILITY_DICT[self.weapon.rarity][i]], "turn cooldown remaining")
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
                    input("[Press enter to continue.]")
                    print("{---------------------------------------------------------------}")
            check_answer = False
            for j in range(len(self.weapon.ABILITY_DICT[self.weapon.rarity])):
                if choice == str(j+1):
                    if choice != str(len(self.weapon.ABILITY_DICT[self.weapon.rarity])):
                        #reorganized into 2 if statements instead of and for legibility
                        if self.weapon.cooldownsDict[self.weapon.ABILITY_DICT[self.weapon.rarity][int(choice)-1]]==0:
                            check_answer = True
                    else:
                        if self.character.inventory["Health Potion"] > 0 and self.character.current_health != self.character.health:
                            check_answer = True
            while not check_answer:
                print("Enter a new choice. The options are:")
                for i in range(len(self.weapon.ABILITY_DICT[self.weapon.rarity])-1):
                    if self.weapon.cooldownsDict[self.weapon.ABILITY_DICT[self.weapon.rarity][i]]==0:
                        print("  ["+str(i+1)+"] "+self.weapon.ABILITY_DICT[self.weapon.rarity][i])
                    else:
                        print("X ["+str(i+1)+"] "+self.weapon.ABILITY_DICT[self.weapon.rarity][i], "→", self.weapon.cooldownsDict[self.weapon.ABILITY_DICT[self.weapon.rarity][i]], "turn cooldown remaining")
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
                        input("[Press enter to continue.]")
                        print("{---------------------------------------------------------------}")
                for j in range(len(self.weapon.ABILITY_DICT[self.weapon.rarity])):
                    if choice == str(j+1):
                        if choice != str(len(self.weapon.ABILITY_DICT[self.weapon.rarity])):
                            if self.weapon.cooldownsDict[self.weapon.ABILITY_DICT[self.weapon.rarity][int(choice)-1]]==0:
                                check_answer = True
                        else:
                            if self.character.inventory["Health Potion"] > 0 and self.character.current_health != self.character.health:
                                check_answer = True
            choice_action = self.weapon.ABILITY_DICT[self.weapon.rarity][int(choice)-1]
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
                print("Who do you wish to attack? (Make sure to type the displayed letter and number. I.e. [s1] to attack Skeleton #1)")
                for enemy_key in self.enemiesDict:
                    counter2 = 1
                    for inst in en_inst[enemy_key]:
                        print("  ["+CONVERSION_DICT[enemy_key]+str(counter2)+"] "+inst.name+" - Current Health:", inst.health)
                        counter2+=1
                who = input("  >>  ")
                chosen = False
                if who.strip() != "": #not empty
                        if who[0].isalpha():
                            if who[0].lower() in POSSIBLE_LETTER and who[1:].isdigit():
                                #amount of enemies in that type
                                #https://www.geeksforgeeks.org/sum-function-python/
                                sum_amount = sum(self.enemiesDict[RCONVERSION_DICT[who[0].lower()]])
                                if int(who[1:])>0 and int(who[1:])<=sum_amount:
                                    chosen = True
                while not chosen:
                    print("That was not the option. (Make sure to type the letter and number exactly as displayed.) The options are: ")
                    for enemy_key in self.enemiesDict:
                        counter2 = 1
                        for inst in en_inst[enemy_key]:
                            print("  ["+CONVERSION_DICT[enemy_key]+str(counter2)+"] "+inst.name+" - Current Health:", inst.health)
                            counter2+=1
                    who = input("  >>  ")
                    if who.strip() != "": #not empty
                        if who[0].isalpha():
                            if who[0].lower() in POSSIBLE_LETTER and who[1:].isdigit():
                                #amount of enemies in that type
                                sum_amount = sum(self.enemiesDict[RCONVERSION_DICT[who[0].lower()]])
                                if int(who[1:])>0 and int(who[1:])<=sum_amount:
                                    chosen = True
                                    
                #dmg to chosen enemy
                en_inst[RCONVERSION_DICT[who[0].lower()]][int(who[1:])-1].health -= dmg
                
                if choice_action == "Slash":
                    print("You slash your sword through "+en_inst[RCONVERSION_DICT[who[0].lower()]][int(who[1:])-1].name+"'s grotesque cadaver. You deal", dmg, "damage.")
                elif choice_action == "Holy Blow":
                    print("Smiting "+en_inst[RCONVERSION_DICT[who[0].lower()]][int(who[1:])-1].name+" down, you deal", dmg, "damage.")
            
        for enemy_key in self.enemiesDict: 
            #iterate over copy -> no uninteded problems if multiple enemies are killed at the same time
            for inst in list(en_inst[enemy_key]):
                if inst.check_dead():
                    #https://www.toppr.com/guides/python-guide/references/methods-and-functions/methods/built-in/isinstance/python-isinstance-2/#:~:text=The%20isinstance%20()%20function%20checks,parent%20class%20of%20an%20object.
                    if not isinstance(inst, Skeleton): 
                        #https://www.w3schools.com/python/python_lists_remove.asp
                        print(" ~ Congratulations, you have slain an enemy! ["+inst.name+"] ~ ")
                        print("  >>  +"+str(int(inst.exp))+" EXP")
                        print("  >>  +"+str(int(inst.gold))+" Gold")
                        self.character.inventory['Gold'] += int(inst.gold)
                        self.character.exp += int(inst.exp)
                        en_inst[enemy_key].remove(inst) 
                        temp_prob = random.random()
                        if temp_prob<0.3:
                            amount_HP = random.randint(1, 2)
                            self.character.inventory['Health Potion'] += amount_HP
                            print("  >>  +"+str(amount_HP)+" Health Potions")
                        if temp_prob<(0.05 * RARITY_DROP_CHANCE[inst.tpe] * TYPE_DROP_CHANCE[enemy_key]):
                            item_type = random.choices(["Weapons", "Helmets", "Armor", "Rings"], weights = [30, 30, 15, 25], k=1)
                            if item_type[0] == "Weapons":
                                item_am = [1, 0, 0, 0]
                            elif item_type[0] == "Helmets":
                                item_am = [0, 1, 0, 0]
                            elif item_type[0] == "Armor":
                                item_am = [0, 0, 1, 0]
                            else:
                                item_am = [0, 0, 0, 1]
                            item = self.shop.create_items(item_am)[item_type[0]][0]
                            if item in self.character.inventory:
                                self.character.inventory+=1
                            else:
                                self.character.inventory[item]=1
                            print("  >>  +1 "+item.name+" ~ ")
                    else:
                        if not inst.used:
                            inst.used = True
                            inst.escape_death()
                        else:
                            print(" ~ You have overcome a skeleton's innate trait and slain them. ["+inst.name+"] ~ ")
                            print("  >>  +"+str(int(inst.exp))+" EXP")
                            print("  >>  +"+str(int(inst.gold))+" Gold")
                            self.character.inventory['Gold'] += int(inst.gold)
                            self.character.exp += int(inst.exp)
                            en_inst[enemy_key].remove(inst)
                            temp_prob = random.random()
                            if temp_prob<0.3:
                                amount_HP = random.randint(1, 2)
                                self.character.inventory['Health Potion'] += amount_HP
                                print("  >>  +"+str(amount_HP)+" Health Potions")
                            if temp_prob<(0.05 * RARITY_DROP_CHANCE[inst.tpe] * TYPE_DROP_CHANCE[enemy_key]):
                                item = self.create_item()
                                if item in self.character.inventory:
                                    self.character.inventory+=1
                                else:
                                    self.character.inventory[item]=1
                                print("  >>  +1 "+item.name+" ~ ")

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
        
        self.turn_count +=1 


        return en_inst

            

    def create_enemy_instances(self):
        """
        A function that simulates creates all the enemy instances for a round.

        Parameters
        ----------
        None
        
        Returns
        -------
        enemy_instances: {str: [Rat/Goblin/Skeleton/Demon]}
            A dictionary containing all the enemy types as keys with their values being lists filled with all the enemy instances of that type.
        """
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

