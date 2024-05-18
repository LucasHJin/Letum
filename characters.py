import random
import os
from weapons import Sword
from armor import Head
from armor import Body
from armor import Ring

class Character:
    def __init__(self, name, srn, dex, con, level, exp):
        self.name = name
        self.stats = {
            'str': srn,
            'dex': dex,
            'con': con,
        }
        self.level = level
        self.exp = exp
        self.health = 10
        self.armor_class = 0
        self.attack_damage = 0
        self.inventory = {
            'Gold': 100000000,
            'Health Potion': 0
        }
        self.current_health = self.health
        self.tabbar = {
            "Poison": 0,
            "Stunned": 0,
            "Weakened": 0,
            "Buffed": 0
        }
        self.equipment = {
            'Helmet': "None",
            'Armor': "None",
            'Ring': "None",
            'Weapon': "None"
        }
        self.needed_exp = 40
        self.stat_points = 0
        self.is_buffed = False
        self.added_ac = 0
        self.added_hp = 0
        self.added_dmg = 0

    def check_profile(self):
        os.system('cls')
        print("STATUS")
        print(self.name)
        print("Level:", self.level)
        print("Experience: "+str(self.exp)+"/"+str(self.needed_exp))
        print("{---------------------------------------------------------------}")
        print("  >>  Health:", self.health)
        print("  >>  Weapon:", self.equipment['Weapon'].name)
        print("{---------------------------------------------------------------}")
        print("  >>  Strength:", self.stats['str'])
        print("  >>  Dexterity:", self.stats['dex'])
        print("  >>  Constitution:", self.stats['con'])
        print("{---------------------------------------------------------------}")
        if self.equipment['Helmet'] == "None":
            print("  >>  Helmet: N/A")
        else:
            print("  >>  Helmet:", self.equipment['Helmet'].name)
        if self.equipment['Armor'] == "None":
            print("  >>  Armor: N/A")
        else:
            print("  >>  Armor:", self.equipment['Armor'].name)
        if self.equipment['Ring'] == "None":
            print("  >>  Ring: N/A")
        else:
            print("  >>  Ring:", self.equipment['Ring'].name)
        print("{---------------------------------------------------------------}")
        input("[Enter any button to return.]")
        
    def print_single_equipment(self, val, choice, letter):
        if val==0:
            POSSIBLEDICT = {
                'h': "Helmets",
                'a': "Body Armor",
                'r': "Rings"
            }
            os.system('cls')
            inst = self.items[POSSIBLEDICT[letter.lower()]][int(choice[1])-1]
            print(inst.name)
            print("{---------------------------------------------------------------}")
            print("  >>  Cost:", inst.buy_value)
            print("  >>  Rarity:", inst.rarity)
            if inst.added_stats['str']>0 or inst.added_stats['dex']>0 or inst.added_stats['con']>0:
                print("  >>  Added Stats:")
                if inst.added_stats['str']>0:
                    print("    >>  Strength: +"+str(inst.added_stats['str']))
                if inst.added_stats['dex']>0:
                    print("    >>  Dexterity: +"+str(inst.added_stats['dex']))
                if inst.added_stats['con']>0:
                    print("    >>  Constitution: +"+str(inst.added_stats['con']))
            print("  >>  Added Benefits:")
            print("    >>  Health: +"+str(inst.added_extra['hp']))
            print("    >>  Damage: +"+str(inst.added_extra['dmg']))
            print("    >>  Armor Class: +"+str(inst.added_extra['ac']))
            input("[Press any button to return.]")
        elif val==1:
            os.system('cls')
            inst = self.items["Weapons"][int(choice[1])-1]
            print(inst.name)
            print("{---------------------------------------------------------------}")
            print("  >>  Cost:", inst.buy_value)
            print("  >>  Rarity:", inst.rarity)
            if inst.added_stats['str']>0 or inst.added_stats['dex']>0 or inst.added_stats['con']>0:
                print("  >>  Added Stats:")
                if inst.added_stats['str']>0:
                    print("    >>  Strength: +"+str(inst.added_stats['str']))
                if inst.added_stats['dex']>0:
                    print("    >>  Dexterity: +"+str(inst.added_stats['dex']))
                if inst.added_stats['con']>0:
                    print("    >>  Constitution: +"+str(inst.added_stats['con']))
            input("[Press any button to return.]")
    
    
    def display_equipments(self):
        print("Current Equipment")
        print("{---------------------------------------------------------------}")
        if self.equipment['Weapon'] == "None":
            print("  >>  Weapon: N/A")
        else:
            print("  >>  Weapon:", self.equipment['Weapon'].name)
        if self.equipment['Helmet'] == "None":
            print("  >>  Helmet: N/A")
        else:
            print("  >>  Helmet:", self.equipment['Helmet'].name)
        if self.equipment['Armor'] == "None":
            print("  >>  Armor: N/A")
        else:
            print("  >>  Armor:", self.equipment['Armor'].name)
        if self.equipment['Ring'] == "None":
            print("  >>  Ring: N/A")
        else:
            print("  >>  Ring:", self.equipment['Ring'].name)
        print("{---------------------------------------------------------------}\n")

    def equip_equipment(self):
        #display message
        self.display_equipments()
        #input and finding want to equip equipment
        POSSIBLE = ['h', 'a', 'r', 'w', 'l']
        POSSIBLEDICT = {
            'h': "Helmet",
            'a': "Armor",
            'r': "Ring",
            'w': "Weapon"
        }
        POSSIBLEDICT2 = {
            'h': Head,
            'a': Body,
            'r': Ring,
            'w': Sword
        }
        
        print("What would you like to equip right now? [Enter the first letter of the equipment category or [L] to leave.]")
        choice = input("  >>  ")
        
        while choice.lower() not in POSSIBLE:
                print("Sorry, that was not an option. What would you like to equip right now? [Enter the FIRST LETTER of the equipment category or [L] to leave.]")
                choice = input("  >>  ")
        
        choice2 = ""
        
        while choice.lower() != "l" and choice2.lower() != "l":
            print("And what equipment would you like to equip? Please make sure that you are equipping a new piece of equipment. [Enter the name of the equipment (exactly as written) or enter [I] to check your inventory.]")
            choice2 = ""
            choice2 = input("  >>  ")
            check = False
            if choice2.lower() == 'i':
                self.check_inventory()
            elif choice2.lower() != 'l':
                for item in self.inventory:
                    if isinstance(item, POSSIBLEDICT2[choice]):
                        if choice2 == item.name:
                            check = True
                            chosenItem = item
                            break
            if (choice != "l" and choice2 != "l" and check):
                #finding currently equipped equipment and the stats they would add
                if POSSIBLEDICT[choice.lower()] == "Weapon":
                    remove_stats = {
                        'str': 0,
                        'dex': 0,
                        'con': 0
                    }
                    remove_extra = {
                        'ac': 0,
                        'hp': 0,
                        'dmg': 0
                    }
                    if self.equipment[POSSIBLEDICT[choice.lower()]] != "None":
                        for item in self.inventory:
                            if isinstance(item, Sword):
                                if self.equipment[POSSIBLEDICT[choice.lower()]].name == item.name:
                                    remove_stats['str'] = item.added_stats['str']
                                    remove_stats['dex'] = item.added_stats['dex']
                                    remove_stats['con'] = item.added_stats['con']

                else:
                    remove_stats = {
                        'str': 0,
                        'dex': 0,
                        'con': 0
                    }
                    remove_extra = {
                        'ac': 0,
                        'hp': 0,
                        'dmg': 0
                    }
                    if self.equipment[POSSIBLEDICT[choice.lower()]] != "None":
                        for item in self.inventory:
                            if isinstance(item, (Ring, Head, Body)):
                                if self.equipment[POSSIBLEDICT[choice.lower()]].name == item.name:
                                    remove_stats['str'] = item.added_stats['str']
                                    remove_stats['dex'] = item.added_stats['dex']
                                    remove_stats['con'] = item.added_stats['con']
                                    remove_extra['ac'] = item.added_extra['ac']
                                    remove_extra['hp'] = item.added_extra['hp']
                                    remove_extra['dmg'] = item.added_extra['dmg']
                

                #changing stats to remove old and add new equipment
                printstr = chosenItem.added_stats['str'] - remove_stats['str']
                printdex = chosenItem.added_stats['dex'] - remove_stats['dex']
                printcon = chosenItem.added_stats['con'] - remove_stats['con']
                self.stats['str'] = self.stats['str'] - remove_stats['str'] + chosenItem.added_stats['str']
                self.stats['dex'] = self.stats['dex'] - remove_stats['dex'] + chosenItem.added_stats['dex']
                self.stats['con'] = self.stats['con'] - remove_stats['con'] + chosenItem.added_stats['con']
                #Refresh all the values on status
                self.refresh_stats()
                #Need to add on calced values again
                printac = 0
                printhp = 0
                printdmg = 0
                
                if POSSIBLEDICT[choice.lower()] != "Weapon":
                    self.added_ac = self.added_ac - remove_extra['ac'] + chosenItem.added_extra['ac']
                    self.added_hp = self.added_hp - remove_extra['hp'] + chosenItem.added_extra['hp']
                    self.added_dmg = self.added_dmg - remove_extra['dmg'] + chosenItem.added_extra['dmg']
                    self.armor_class = self.armor_class + self.added_ac
                    self.health = self.health + self.added_hp
                    self.attack_damage = self.attack_damage + self.added_dmg
                    
                    printac = self.added_ac
                    printhp = self.added_hp
                    printdmg = self.added_dmg

                self.equipment[POSSIBLEDICT[choice.lower()]] = item

                os.system('cls')
                print("You have equipped " + chosenItem.name + ".")
                PRINTDICT = {
                    'str': printstr,
                    'dex': printdex,
                    'con': printcon,
                    'ac': printac,
                    'hp': printhp,
                    'dmg': printdmg
                }
                
                for i in PRINTDICT:
                    if PRINTDICT[i]>=0:
                        print("  >>  "+i+": +"+str(PRINTDICT[i]))
                    else:
                        print("  >>  "+i+": "+str(PRINTDICT[i]))
            else:
                print("That was not a valid input. We shall restart.")
            print("")
            self.display_equipments()
            
            print("What would you like to equip right now? [Enter the first letter of the equipment category or [L] to leave.]")
            choice = input("  >>  ")
            while choice.lower() not in POSSIBLE:
                print("Sorry, that was not an option. What would you like to equip right now? [Enter the FIRST LETTER of the equipment category or [L] to leave.]")
                choice = input("  >>  ")
        input("Thank you for your business. I hope to see you soon. [Press enter to continue.]")
        
        
    def check_inventory(self):
        os.system('cls')
        print("INVENTORY")
        print("{---------------------------------------------------------------}")
        for i in self.inventory.keys():
            if not isinstance(i, Sword) and not isinstance(i, Head) and not isinstance(i, Body) and not isinstance(i, Ring):
                print(i+":", self.inventory[i])
            else:
                print(i.name+":", self.inventory[i])
        print("{---------------------------------------------------------------}")
        input("[Enter any button to return.]")
        

    def refresh_current_health(self): #for after level up or clear room 
        self.current_health = self.health

    def check_status_bar(self): 
        if self.tabbar["Poison"]>0: #works now
            pDamage = int(self.health*0.05)
            print(" ~ You have been poisoned for", pDamage, "damage. ~ ")
            self.current_health -= pDamage
            self.tabbar["Poison"]-=1 #WORKS
        if self.tabbar["Weakened"]>0:
            self.tabbar["Weakened"]-=1 
        if self.tabbar["Buffed"]==0 and self.is_buffed:
            for st in self.stats:
                self.stats[st]-=5
            self.is_buffed = False
            health_diff = self.health - self.current_health
            self.refresh_stats()
            self.current_health -= health_diff
        if self.tabbar["Buffed"]>0 and not self.is_buffed:
            for st in self.stats:
                self.stats[st]+=5
            self.is_buffed = True
            self.tabbar["Buffed"]-=1
            health_diff = self.health - self.current_health
            self.refresh_stats()
            self.current_health -= health_diff


    def use_health_potion(self):
        self.inventory['Health Potion'] -= 1
        add_health = random.randint(25, 50)
        self.current_health += add_health
        if self.current_health > self.health:
            self.current_health = self.health
        print("Quickly uncorking your health potion, you guzzle it down and feel your body rejuvenate. [+"+str(add_health)+"HP]")
        print("  >>  Health:", self.current_health)

            
    def check_dead(self):
        if self.current_health<=0:
            dead = True
        else:
            dead = False
        return dead

    def calc_health(self):
        self.health = 100 + self.stats['con'] * 2

    def calc_ac(self):
        self.armor_class = 20 + self.stats['dex'] * 2

    def calc_damage(self):
        self.attack_damage = 15 + self.stats['str'] * 3

    def calc_needed_exp(self):
        self.needed_exp = 40*self.level

    def refresh_stats(self):
        self.calc_health()
        self.calc_damage()
        self.calc_ac()

        #Need to add on armor bonuses again
        self.armor_class = self.armor_class + self.added_ac
        self.health = self.health + self.added_hp
        self.attack_damage = self.attack_damage + self.added_dmg

        self.calc_needed_exp()
        self.refresh_current_health()

    def calc_exp(self):
        counter=0
        while self.exp>=self.needed_exp:
            self.exp-=self.needed_exp
            counter += 1
            self.level += 1
            self.calc_needed_exp()
        return counter

    def assign_stat_points(self, repeated_num):
        print("Current Stats:")
        print("{---------------------------------------------------------------}")
        print("  >>  Strength:", self.stats['str'])
        print("  >>  Dexterity:", self.stats['dex'])
        print("  >>  Constitution:", self.stats['con'])
        print("{---------------------------------------------------------------}")
        print("  >>  Available Stat Points:", self.stat_points)
        print("{---------------------------------------------------------------}")
        for _ in range(repeated_num):
            print(" ~ Which stat would you like to increase? (str/dex/con) ~ ")
            stat_choice = input("  >>  ")
            good = False
            if stat_choice.lower() in self.stats:
                self.stats[stat_choice] += 1
            else:
                while not good:
                    print(" ~ Invalid choice. Please choose from 'str', 'dex', or 'con'. ~ ")
                    stat_choice = input("  >>  ")
                    if stat_choice.lower() in self.stats:
                        self.stats[stat_choice] += 1
                        good = True
                        print("{---------------------------------------------------------------}")
                        if self.stats.choice.lower() == 'str':
                            print("  >>  Strength:", self.stats['str'], "↑")
                        elif self.stats.choice.lower() == 'dex':
                            print("  >>  Dexterity:", self.stats['dex'], "↑")
                        else:
                            print("  >>  Constitution:", self.stats['con'], "↑")
                        print("{---------------------------------------------------------------}")
        print(" ~ Level up complete! Your stats are now: ~ ")
        print("{---------------------------------------------------------------}")
        print("  >>  Strength:", self.stats['str'])
        print("  >>  Dexterity:", self.stats['dex'])
        print("  >>  Constitution:", self.stats['con'])
        print("{---------------------------------------------------------------}")
        input("[Enter any button to continue.]")


    def all_level_up(self):
        os.system('cls')
        times = self.calc_exp()
        for _ in range(times):
            self.stat_points += 2
        self.assign_stat_points(self.stat_points)
        self.refresh_stats()

    def add_inventory(self, items):
        for i in items.keys():
            if i in self.inventory:
                self.inventory[i]+=items[i]
            else:
                self.inventory[i]=items[i]


