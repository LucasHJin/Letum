from enemies import Rat
from enemies import Goblin
from enemies import Skeleton
from enemies import Demon
import os

#TO DO:
'''
ADD REFRESH HP AND LEVEL UP
- CHANGE LEVEL UP TO CONTINUOSULY BE CALLED AND JUST KEEP TRACK OF AVAILABLE STATUS POINTS
- END OF EVERY BATTLE, OFFER TO ALLOCATE STAT POINTS
ADD ALL THE NECESSARY STATUS EFFECTS
CHANGE THE INIT FOR ALL OTHER CLASSES -> DONE TO BE CHECKED
MAKE GAME FINISHED WORK!!! (I.e. WHEN ENEMY IS KILLED)
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
        status = self.turn(ene_inst)
        while status != "DEAD" and status != "WON":
            #os.system('cls')
            status = self.turn(status)
        if status == "DEAD":
            return "DEAD"
        else:
            #REFRESH HP AND LEVEL UP?
            temp = 1
            return "WON"

    def turn(self, en_inst): #REMEMBER ADD COOLDOWNS
        #have each enemy and character go once in a turn (loop iterate) AND check for death and if so remove that character
        if self.character.check_dead():
            print("Having taken too many blows, you succumb to your wounds.")
            return "DEAD"
        else:
            #player turn
            print("\nYour Turn:")
            print("{---------------------------------------------------------------}")
            print("  >>  Health:", self.character.current_health)
            
            print("What do you want to do?")
            for i in range(len(self.weapon.abilityDict[self.weapon.rarity])-1):
                print("  ["+str(i+1)+"] "+self.weapon.abilityDict[self.weapon.rarity][i])
            if self.character.inventory["Health Potion"]>0 and self.character.current_health != self.character.health:
                print("  ["+str(i+2)+"] Use a Health Potion ("+str(self.character.inventory["Health Potion"])+"X)")
            choice = input("  >>  ")
            check_answer = False
            for j in range(len(self.weapon.abilityDict[self.weapon.rarity])):
                if choice == str(j+1):
                    if choice != str(len(self.weapon.abilityDict[self.weapon.rarity])):
                        check_answer = True
                    else:
                        if self.character.inventory["Health Potion"] > 0 and self.character.current_health != self.character.health:
                            check_answer = True
            while not check_answer:
                print("Sorry, you can't do that. The options are:")
                for i in range(len(self.weapon.abilityDict[self.weapon.rarity])-1):
                    print("  ["+str(i+1)+"] "+self.weapon.abilityDict[self.weapon.rarity][i])
                if self.character.inventory["Health Potion"]>0 and self.character.current_health != self.character.health:
                    print("  ["+str(i+2)+"] Use a Health Potion ("+str(self.character.inventory["Health Potion"])+"X)")
                choice = input("  >>  ")
                for j in range(len(self.weapon.abilityDict[self.weapon.rarity])):
                    if choice == str(j+1):
                        if choice != str(len(self.weapon.abilityDict[self.weapon.rarity])):
                            check_answer = True
                        else:
                            if self.character.inventory["Health Potion"] > 0 and self.character.current_health != self.character.health:
                                check_answer = True
            choice_action = self.weapon.abilityDict[self.weapon.rarity][int(choice)-1]
            if choice_action == "Slash":
                dmg = self.weapon.slash()
            elif choice_action == "Wide Slash":
                dmg = self.weapon.wide_slash()
            elif choice_action == "Holy Blow":
                dmg = self.weapon.holy_blow()
            elif choice_action == "Holy Aura":
                dmg = self.weapon.holy_aura()
            elif choice_action == "HP" and self.character.inventory["Health Potion"]>0 and self.character.current_health!=self.character.health:
                dmg = 0
                self.character.use_health_potion()
            if choice_action == "Wide Slash":
                for enemy_key in self.enemiesDict:
                    for inst in en_inst[enemy_key]:
                        inst.health -= dmg
            elif choice_action != "HP":
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
                elif choice_action == "Wide Slash":
                    print("Throwing a wide slash, you hit all the enemies, dealing", dmg, "damage to each one of them.")
                elif choice_action == "Holy Blow":
                    print("Smiting the enemy down, you deal", dmg, "damage.")
                elif choice_action == "Holy Aura":
                    print("You call upon the holy power of the Gods and buff yourself.")
                    print(" ~ All your stats have been increased by 5 for 2 turns. ~ ")
                
        #enemy turn
        for enemy_key in self.enemiesDict: 
            for inst in en_inst[enemy_key]:
                if inst.check_dead():
                    #https://www.toppr.com/guides/python-guide/references/methods-and-functions/methods/built-in/isinstance/python-isinstance-2/#:~:text=The%20isinstance%20()%20function%20checks,parent%20class%20of%20an%20object.
                    if not isinstance(inst, Skeleton): 
                        #https://www.w3schools.com/python/python_lists_remove.asp
                        en_inst[enemy_key].remove(inst) 
                        print(" ~ Congratulations, you have slain an enemy! ["+inst.name+"] ~ ")
                    else:
                        if not inst.used:
                            inst.used = True
                            inst.escape_death()
                        else:
                            en_inst[enemy_key].remove(inst)
                            print(" ~ You have overcome a skeleton's innate trait and slain them. ["+inst.name+"] ~ ")
        print("{---------------------------------------------------------------}\n")

        print("Enemy's turn")
        print("{---------------------------------------------------------------}")
        for enemy_key in self.enemiesDict:
            for inst in en_inst[enemy_key]:
                if not inst.check_dead():
                    enemy_dmg = inst.choose_ability()
                    self.character.current_health -= enemy_dmg
        print("{---------------------------------------------------------------}")

        #check won DOESN"T WORK YET -> FIX
        total_left = 0
        for enemy_key in self.enemiesDict:
            total_left += len(self.enemiesDict[enemy_key])
        if total_left == 0:
            return "WON"

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

