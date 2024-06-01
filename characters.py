"""
Final Project
ICS3U
Lucas Jin
This file declares the Character class for the player's character with all the necessary methods and attributes. For example, it possesses attributes such as health and inventory and methods such as adding to stats.
History:
    April 13, 2024: Program Creation
    May 25, 2024: Adding Comments
"""

import random
import os
from weapons import Sword
from armor import Helmet
from armor import Armor
from armor import Ring

class Character:
    """
    A Character class that will be instantiated to create the character the player uses.
    ...

    Attributes
    ----------
    name: str
        Name of the character.
    stats: {str: int}
        The stats of the character. It affects other attributes such as health.
    level: int
        The level of the character. Starts at 1.
    exp: int
        The amount of exp the character currently has.
    needed_exp: int
        The amount of exp the character needs to level up.
    health: int
        The total amount of health the character has.
    current_health: int
        The amount of health the character currently has in a battle.
    armor_class: int
        A stat that affects damage reduction in battles.
    attack_damage: int
        A stat that affects how much damage the character does in battles.
    inventory: {str/Sword/Helmet/Armor/Ring: int}
        The inventory to store all of the character's equipment, gold, etc.
    tabbar: {str: int}
        Dictionary to check for any status affects.
    equipment: {str: str/Sword/Helmet/Armor/Ring}
        The equipment that the character currently has equipped.
    stat_points: int
        The amount of stat points the character currently has to use.
    is_buffed: boolean  
        If the character is buffed.
    added_ac: int
        Amount of armor class added from equipped equipment.
    added_hp: int
        Amount of health added from equipped equipment.
    added_dmg: int
        Amount of damage added from equipped equipment.

    Methods
    -------
    check_profile()
        Shows the profile/status window of the character.
    display_equipments()
        Prints the currently equipped equipment.
    print_single_equipment(val, inst)
        Prints a description of an equipment from the inventory.
    equip_equipment()
        Function to equip equipment from the inventory.
    display_inventory()
        Prints all the items in the inventory.
    check_inventory()
        Function to let the user check any of their items in their inventory.
    add_inventory(items)
        Function to add items to the inventory.
    apply_status()
        Applies status effects to the tabbar.
    use_health_potion()
        Function to use a health potion -> increase health and remove 1 health potion from inventory.
    check_dead()
        Check if the character is dead.
    calc_health()
        Calcuate health based on stats.
    calc_ac()
        Calcuate armor class based on stats.
    calc_damage()
        Calcuate damage based on stats.
    calc_needed_exp()
        Calculate amount of exp needed to reach next level.
    refresh_current_health()
        Refreshes current health to max (after finishing a round).
    refresh_stats()
        Calculates/updates all the necessary values (i.e. health, damage, etc.) To be used after leveling up.
    calc_lvl_up()
        Calculates how many times the player has leveled up based on their current exp.
    assign_stat_points()
        Function to assign all stat points.
    all_level_up()
        Function that combines the previous two functions to let the player level up.
    """
    
    def __init__(self, name, srn, dex, con):
        """
        A function that is called immediately when an instance of this class is created. It initalizes all the attributes of the class.

        Parameters
        ----------
        name: str
            Name of the instance
        srn: int
            Amount of strength the character has based on user input.
        dex: int
            Amount of dexterity the character has based on user input.
        con: int
            Amount of constitution the character has based on user input.
        
        Returns
        -------
        None
        """
        self.name = name
        self.stats = {
            'str': srn,
            'dex': dex,
            'con': con,
        }
        self.level = 1
        self.exp = 0
        self.needed_exp = 40
        self.health = 1 #ensure that character isn't dead as soon as it is instantiated -> will be replaced with proper health later on
        self.current_health = self.health
        self.armor_class = 0
        self.attack_damage = 0
        self.inventory = {
            'Gold': 0,
            'Health Potion': 0
        }
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
        self.stat_points = 0
        self.is_buffed = False
        self.added_ac = 0
        self.added_hp = 0
        self.added_dmg = 0

    def check_profile(self):
        """
        A function that prints out the characters profile (i.e. name, level, experience, health, etc.)

        Parameters
        ----------
        None
        
        Returns
        -------
        None
        """
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
        #print can't call .name on a string -> need to check if it is a string or custom class
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
        input("[Press enter to continue.]")
    
    
    def display_equipments(self):
        """
        A function that prints out the character's currently equipped equipment.

        Parameters
        ----------
        None
        
        Returns
        -------
        None
        """
        print("Current Equipment")
        print("{---------------------------------------------------------------}")
        #print can't call .name on a string -> need to check if it is a string or custom class
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

    def print_single_equipment(self, val, inst):
        """
        A function that prints out the description for a single piece of equipment.
        
        Parameters
        ----------
        val: int
            Acts as a boolean, for if we want to print a piece of equipment or weapon (different aspects that need to be printed)
        inst: Helmet/Armor/Ring/Sword
            The instance of the item to be printed
        
        Returns
        -------
        None
        """
        if val==0:
            os.system('cls')
            print(inst.name)
            print("{---------------------------------------------------------------}")
            print("  >>  Cost:", inst.buy_value)
            print("  >>  Sell Value:", inst.sell_value)
            print("  >>  Rarity:", inst.rarity)
            if inst.added_stats['str']>0 or inst.added_stats['dex']>0 or inst.added_stats['con']>0:
                print("  >>  Added Stats:")
                if inst.added_stats['str']>0:
                    #if it adds to the stat, display it
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
            print(inst.name)
            print("{---------------------------------------------------------------}")
            print("  >>  Cost:", inst.buy_value)
            print("  >>  Sell Value:", inst.sell_value)
            print("  >>  Rarity:", inst.rarity)
            print("  >>  Damage:", int(inst.damage * inst.damage_multiplier))
            if inst.added_stats['str']>0 or inst.added_stats['dex']>0 or inst.added_stats['con']>0:
                print("  >>  Added Stats:")
                if inst.added_stats['str']>0:
                    print("    >>  Strength: +"+str(inst.added_stats['str']))
                if inst.added_stats['dex']>0:
                    print("    >>  Dexterity: +"+str(inst.added_stats['dex']))
                if inst.added_stats['con']>0:
                    print("    >>  Constitution: +"+str(inst.added_stats['con']))
            print("  >>  Available Abilities:")
            for ability in range(len(inst.ABILITY_DICT[inst.rarity])-1):
                print("    >>  "+inst.ABILITY_DICT[inst.rarity][ability])
                #print all the possible abilities based on the rarity
            input("[Press any button to return.]")    

    def equip_equipment(self):

        ###STILL NEED TO FIX -> PART WITH EQUIPPING
        """
        A function that to equip equipment from the inventory.

        Parameters
        ----------
        None
        
        Returns
        -------
        None
        """
        #display message
        self.display_inventory()
        self.display_equipments()
        #input and finding want to equip equipment
        POSSIBLEDICT = {
            Helmet: "Helmet",
            Armor: "Armor",
            Ring: "Ring",
            Sword: "Weapon"
        }

        #getting first input
        print("What would you like to equip right now? [Enter the 'e' and the number of the equipment (no spaces) or [L] to leave or the number of the equipment to check it out.]")
        choice = input("  >>  ")
        
        #input validation
        checking = True
        while checking:
            #if empty
            if not choice:
                print("Sorry, that was not an option. What would you like to equip right now? [Enter the 'e' and the number of the equipment (no spaces) or [L] to leave or the number of the equipment to check it out.]")
                choice = input("  >>  ")
            #if length 1 -> 2 options
            elif len(choice) == 1:
                #is a number within the size of the inventory
                if choice.isdigit():
                    if int(choice) > len(self.inventory) or int(choice) <=2:
                        print("Sorry, that was not an option. What would you like to equip right now? [Enter the 'e' and the number of the equipment (no spaces) or [L] to leave or the number of the equipment to check it out.]")
                        choice = input("  >>  ")
                    else:
                        checking = False
                #needs to be l to leave
                elif choice.lower() != "l":
                    print("Sorry, that was not an option. What would you like to equip right now? [Enter the 'e' and the number of the equipment (no spaces) or [L] to leave or the number of the equipment to check it out.]")
                    choice = input("  >>  ")
                else:
                    checking = False
            #equipping
            elif len(choice) == 2:
                #first letter needs to be e
                if choice[0].lower() != "e":
                    print("Sorry, that was not an option. What would you like to equip right now? [Enter the 'e' and the number of the equipment (no spaces) or [L] to leave or the number of the equipment to check it out.]")
                    choice = input("  >>  ")
                #second character needs to be a number in the range of the inventory
                elif not choice[1].isdigit():
                    print("Sorry, that was not an option. What would you like to equip right now? [Enter the 'e' and the number of the equipment (no spaces) or [L] to leave or the number of the equipment to check it out.]")
                    choice = input("  >>  ")
                elif int(choice[1]) > len(self.inventory) or int(choice[1]) <= 2:
                    print("Sorry, that was not an option. What would you like to equip right now? [Enter the 'e' and the number of the equipment (no spaces) or [L] to leave or the number of the equipment to check it out.]")
                    choice = input("  >>  ")
                else:
                    checking = False
            else:
                print("Sorry, that was not an option. What would you like to equip right now? [Enter the 'e' and the number of the equipment (no spaces) or [L] to leave or the number of the equipment to check it out.]")
                choice = input("  >>  ")    
        
        #while the user doesn't want to leave
        while (choice != "l"):
            #results from user choice
            #inspecting
            if len(choice) == 1 and choice.isdigit():
                count_keys = 1
                #can't access iterator of inventory.keys -> must manually count
                for item in (self.inventory.keys()):
                    if count_keys == int(choice):
                        check_item = item
                        break
                    count_keys+=1
                #printing item description
                if isinstance(check_item, Sword):
                    self.print_single_equipment(1, check_item)
                else:
                    self.print_single_equipment(0, check_item)
            #equipping
            elif len(choice)==2:
                temp_count = 0
                for item in self.inventory:
                    if int(choice[1]) == temp_count+1:
                        chosenItem = item
                        #if it is an item in inventory, then it is good
                        break
                    temp_count+=1
                #finding currently equipped equipment and the stats they would add
                if isinstance(chosenItem, Sword):
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
                    #getting type of class -> https://stackoverflow.com/questions/510972/getting-the-class-name-of-an-instance
                    if self.equipment["Weapon"] != "None":
                        for item in self.inventory:
                            if isinstance(item, Sword):
                                if self.equipment["Weapon"].name == item.name:
                                    remove_stats['str'] = item.added_stats['str']
                                    remove_stats['dex'] = item.added_stats['dex']
                                    remove_stats['con'] = item.added_stats['con']

                else:
                    #finding stats again -> this time more because piece of equipment, not weapon
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
                    #getting type of class -> https://stackoverflow.com/questions/510972/getting-the-class-name-of-an-instance
                    #If not empty -> additional stats to be checked
                    if self.equipment[POSSIBLEDICT[chosenItem.__class__]] != "None":
                        #getting stats to be removed from current equipment
                        for item in self.inventory:
                            if isinstance(item, (Ring, Helmet, Armor)):
                                if self.equipment[POSSIBLEDICT[chosenItem.__class__]].name == item.name:
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
                
                #nonweapons have a few more stats to add 
                if not isinstance(chosenItem, Sword):
                    self.added_ac = self.added_ac - remove_extra['ac'] + chosenItem.added_extra['ac']
                    self.added_hp = self.added_hp - remove_extra['hp'] + chosenItem.added_extra['hp']
                    self.added_dmg = self.added_dmg - remove_extra['dmg'] + chosenItem.added_extra['dmg']
                    self.armor_class = self.armor_class + self.added_ac
                    self.health = self.health + self.added_hp
                    self.attack_damage = self.attack_damage + self.added_dmg
                    
                    #only need difference of what was added and removed, not total
                    printac = chosenItem.added_extra['ac'] - remove_extra['ac']
                    printhp = chosenItem.added_extra['hp'] - remove_extra['hp']
                    printdmg = chosenItem.added_extra['dmg'] - remove_extra['dmg']

                #changing equipped item to chosen item
                self.equipment[POSSIBLEDICT[chosenItem.__class__]] = chosenItem

                os.system('cls')
                #final message stating item has been equipped
                print("You have equipped " + chosenItem.name + ".")
                PRINTDICT = {
                    'str': printstr,
                    'dex': printdex,
                    'con': printcon,
                    'ac': printac,
                    'hp': printhp,
                    'dmg': printdmg
                }
                
                #printing out all the stat values changed by the change in equipment
                for i in PRINTDICT:
                    if PRINTDICT[i]>=0:
                        print("  >>  "+i+": +"+str(PRINTDICT[i]))
                    else:
                        print("  >>  "+i+": "+str(PRINTDICT[i]))
                input("[Press enter to continue.]")
            os.system('cls')
            
            self.display_inventory()
            self.display_equipments()
            
            #getting new input
            print("What would you like to equip right now? [Enter the 'e' and the number of the equipment (no spaces) or [L] to leave or the number of the equipment to check it out.]")
            choice = input("  >>  ")
            
            #input validation
            checking = True

            while checking:
                if not choice:
                    print("Sorry, that was not an option. What would you like to equip right now? [Enter the 'e' and the number of the equipment (no spaces) or [L] to leave or the number of the equipment to check it out.]")
                    choice = input("  >>  ")
                elif len(choice) == 1:
                    if choice.isdigit():
                        if int(choice) > len(self.inventory) or int(choice) <=2:
                            print("Sorry, that was not an option. What would you like to equip right now? [Enter the 'e' and the number of the equipment (no spaces) or [L] to leave or the number of the equipment to check it out.]")
                            choice = input("  >>  ")
                        else:
                            checking = False
                    elif choice.lower() != "l":
                        print("Sorry, that was not an option. What would you like to equip right now? [Enter the 'e' and the number of the equipment (no spaces) or [L] to leave or the number of the equipment to check it out.]")
                        choice = input("  >>  ")
                    else:
                        checking = False
                elif len(choice) == 2:
                    if choice[0].lower() != "e":
                        print("Sorry, that was not an option. What would you like to equip right now? [Enter the 'e' and the number of the equipment (no spaces) or [L] to leave or the number of the equipment to check it out.]")
                        choice = input("  >>  ")
                    elif not choice[1].isdigit():
                        print("Sorry, that was not an option. What would you like to equip right now? [Enter the 'e' and the number of the equipment (no spaces) or [L] to leave or the number of the equipment to check it out.]")
                        choice = input("  >>  ")
                    elif int(choice[1]) > len(self.inventory) or int(choice[1]) <= 2:
                        print("Sorry, that was not an option. What would you like to equip right now? [Enter the 'e' and the number of the equipment (no spaces) or [L] to leave or the number of the equipment to check it out.]")
                        choice = input("  >>  ")
                    else:
                        checking = False
                else:
                    print("Sorry, that was not an option. What would you like to equip right now? [Enter the 'e' and the number of the equipment (no spaces) or [L] to leave or the number of the equipment to check it out.]")
                    choice = input("  >>  ")    

    
    def display_inventory(self):
        """
        A function that displays the inventory and then returns a list with the inventory and the number of items in the inventory.

        Parameters
        ----------
        None
        
        Returns
        -------
        inventoryList: [Sword/Helmet/Armor/Ring/str]
            All the items in the inventory.
        count: int
            Amount of items within the inventory.
        """
        os.system('cls')
        inventoryList = []
        #inventory list to know whats in inventory
        count = 0
        #count to put a number next to each item
        print("INVENTORY")
        print("{---------------------------------------------------------------}")
        for item_inv in self.inventory.keys():
            if not isinstance(item_inv, Sword) and not isinstance(item_inv, Helmet) and not isinstance(item_inv, Armor) and not isinstance(item_inv, Ring):
                print("["+str(count+1)+"] "+item_inv+":", self.inventory[item_inv])
            else:
                print("["+str(count+1)+"] "+item_inv.name+":", self.inventory[item_inv])
            inventoryList.append(item_inv)
            count+=1
        print("{---------------------------------------------------------------}")
        #could also just return inventoryList and use len
        return [inventoryList, count]
    
    def check_inventory(self):
        """
        A function that lets the user check through their inventory.

        Parameters
        ----------
        None
        
        Returns
        -------
        None
        """
        #check through each item in the inventory specifically
        temp = self.display_inventory()
        inventoryList = temp[0]
        count = temp[1]
        print("[Enter [L] to leave the inventory or enter the number of a specific item to learn more about it.]")
        choice = input("  >>  ")
        while choice != "l":
            if choice.isdigit():
                if choice == "1":
                    #manually written description
                    print("Gold is the currency of the realm you currently reside in. It drops from monsters and chests and can be used to purchase equipment and consumables.")
                    input("[Press any button to return.]")
                    print("What will you do now?")
                    print("[Enter [L] to leave the inventory or enter the number of a specific item to learn more about it.]")
                    choice = input("  >>  ")
                elif choice == "2":
                    #manually written description
                    print("Health potions are an essential part of your kit. They will help you stay alive during battles, healing a random amount every use.")
                    input("[Press any button to return.]")    
                    print("What will you do now?")
                    print("[Enter [L] to leave the inventory or enter the number of a specific item to learn more about it.]")
                    choice = input("  >>  ")
                elif int(choice)-1<len(inventoryList) and int(choice)-1>=0:
                    if isinstance(inventoryList[int(choice)-1], Sword):
                        #print the description of the chosen item
                        self.print_single_equipment(1, inventoryList[int(choice)-1])
                        print("What will you do now?")
                        print("[Enter [L] to leave the inventory or enter the number of a specific item to learn more about it.]")
                        choice = input("  >>  ")
                    elif isinstance(inventoryList[int(choice)-1], Helmet):
                        self.print_single_equipment(0, inventoryList[int(choice)]-1)
                        print("What will you do now?")
                        print("[Enter [L] to leave the inventory or enter the number of a specific item to learn more about it.]")
                        choice = input("  >>  ")
                    elif isinstance(inventoryList[int(choice)-1], Armor):
                        self.print_single_equipment(0, inventoryList[int(choice)-1])
                        print("What will you do now?")
                        print("[Enter [L] to leave the inventory or enter the number of a specific item to learn more about it.]")
                        choice = input("  >>  ")
                    elif isinstance(inventoryList[int(choice)-1], Ring):
                        self.print_single_equipment(0, inventoryList[int(choice)-1])
                        print("What will you do now?")
                        print("[Enter [L] to leave the inventory or enter the number of a specific item to learn more about it.]")
                        choice = input("  >>  ")
                    else:
                        #invalid inputs (i.e. put a number out of the range)
                        print("That was not an option.")
                        print("[Enter [L] to leave the inventory or enter the number of a specific item to learn more about it.]")
                        choice = input("  >>  ")
                else:
                    print("That was not an option.")
                    print("[Enter [L] to leave the inventory or enter the number of a specific item to learn more about it.]")
                    choice = input("  >>  ")
            else:
                print("That was not an option.")
                print("[Enter [L] to leave the inventory or enter the number of a specific item to learn more about it.]")
                choice = input("  >>  ")
            
    def add_inventory(self, items):
        """
        A function that adds items to the player's inventory.

        Parameters
        ----------
        items: {str: int}
            Dictionary of items and amount of each item to be added to inventory
        
        Returns
        -------
        None
        """
        for item in items.keys():
            if item in self.inventory:
                self.inventory[item]+=items[item]
            else:
                self.inventory[item]=items[item]

    def apply_status(self): 
        """
        A function that applys status effects to the character's instance.

        Parameters
        ----------
        None
        
        Returns
        -------
        None
        """
        if self.tabbar["Poison"]>0: #if poisoned
            pDamage = int(self.health*0.05)
            #lose some health + print message
            print(" ~ You have been poisoned for", pDamage, "damage. ~ ")
            self.current_health -= pDamage
            #reduce cooldown by one
            self.tabbar["Poison"]-=1 
        if self.tabbar["Weakened"]>0:
            #reduce cooldown -> effect is calculated during ability by enemy
            self.tabbar["Weakened"]-=1 
        if self.tabbar["Buffed"]==0 and self.is_buffed:
            #if was buffed and it just ran out -> need to remove buff
            for st in self.stats:
                self.stats[st]-=5
            #no longer buffed
            self.is_buffed = False
            health_diff = self.health - self.current_health
            self.refresh_stats()
            self.current_health -= health_diff
        if self.tabbar["Buffed"]>0 and not self.is_buffed:
            #if has buff effect but has not been buffed yet
            for st in self.stats:
                self.stats[st]+=5
            #is buffed
            self.is_buffed = True
            self.tabbar["Buffed"]-=1
            health_diff = self.health - self.current_health
            self.refresh_stats()
            self.current_health -= health_diff


    def use_health_potion(self):
        """
        A function that heals the user by 25 to 50 HP in battle.

        Parameters
        ----------
        None
        
        Returns
        -------
        None
        """
        self.inventory['Health Potion'] -= 1
        add_health = random.randint(25, 50)
        self.current_health += add_health
        #can't go past full health
        if self.current_health > self.health:
            self.current_health = self.health
        print("Quickly uncorking your health potion, you guzzle it down and feel your body rejuvenate. [+"+str(add_health)+"HP]")
        print("  >>  Health:", self.current_health)

            
    def check_dead(self):
        """
        A function that checks if the user is dead.

        Parameters
        ----------
        None
        
        Returns
        -------
        dead: boolean
            Returns if the user is dead or not (True/False)
        """
        if self.current_health<=0:
            dead = True
        else:
            dead = False
        return dead

    def calc_health(self):
        """
        A function that calculates the user's health based on constitution.

        Parameters
        ----------
        None
        
        Returns
        -------
        None
        """
        self.health = 100 + self.stats['con'] * 2

    def calc_ac(self):
        """
        A function that calculates the user's armor class based on dexterity.

        Parameters
        ----------
        None
        
        Returns
        -------
        None
        """
        self.armor_class = 20 + self.stats['dex'] * 2

    def calc_damage(self):
        """
        A function that calculates the user's damage based on strength.

        Parameters
        ----------
        None
        
        Returns
        -------
        None
        """
        self.attack_damage = 15 + self.stats['str'] * 3

    def calc_needed_exp(self):
        """
        A function that calculates the amount of exp needed by the user to level up based on their level.

        Parameters
        ----------
        None
        
        Returns
        -------
        None
        """
        self.needed_exp = 40*self.level
        
    def refresh_current_health(self): #for after level up or clear room 
        """
        A function that refreshes the users current health to their max health.

        Parameters
        ----------
        None
        
        Returns
        -------
        None
        """
        self.current_health = self.health

    def refresh_stats(self):
        """
        A function that calls all the previous calculating and refreshing functions all at once. This can be used after a round to have all of their stats refreshed.

        Parameters
        ----------
        None
        
        Returns
        -------
        None
        """
        self.calc_health()
        self.calc_damage()
        self.calc_ac()

        #Need to add on armor bonuses again
        self.armor_class = self.armor_class + self.added_ac
        self.health = self.health + self.added_hp
        self.attack_damage = self.attack_damage + self.added_dmg

        self.calc_needed_exp()
        self.refresh_current_health()

    def calc_lvl_up(self):
        """
        A function that calculates the amount of level ups gained by the user.

        Parameters
        ----------
        None
        
        Returns
        -------
        counter: int
            The amount of times the user has leveled up.
        """
        counter=0
        while self.exp>=self.needed_exp:
            #while have more exp than needed exp
            #subtract exp to get to next level
            self.exp-=self.needed_exp
            counter += 1
            #increase level
            self.level += 1
            #calculate new needed exp
            self.calc_needed_exp()
        return counter

    def assign_stat_points(self, repeated_num):
        """
        A function that allows the user to add stat points to their stats.

        Parameters
        ----------
        repeated_num: int
            The amount of times the user can add to their stat points.
        
        Returns
        -------
        None
        """
        #print stats and stat points
        print("Current Stats:")
        print("{---------------------------------------------------------------}")
        print("  >>  Strength:", self.stats['str'])
        print("  >>  Dexterity:", self.stats['dex'])
        print("  >>  Constitution:", self.stats['con'])
        print("{---------------------------------------------------------------}")
        print("  >>  Available Stat Points:", self.stat_points)
        print("{---------------------------------------------------------------}")
        for _ in range(repeated_num):
            #while still have stat points
            print(" ~ Which stat would you like to increase? (str/dex/con) ~ ")
            stat_choice = input("  >>  ")
            #input validation + getting input
            good = False
            if stat_choice.lower() in self.stats:
                self.stats[stat_choice] += 1
                good = True
                #adding stats to the chosen one
                print("{---------------------------------------------------------------}")
                if stat_choice.lower() == 'str':
                    print("  >>  Strength:", self.stats['str'], "↑")
                elif stat_choice.lower() == 'dex':
                    print("  >>  Dexterity:", self.stats['dex'], "↑")
                else:
                    print("  >>  Constitution:", self.stats['con'], "↑")
                print("{---------------------------------------------------------------}")
            while not good:
                print(" ~ Invalid choice. Please choose from 'str', 'dex', or 'con'. ~ ")
                stat_choice = input("  >>  ")
                if stat_choice.lower() in self.stats:
                    self.stats[stat_choice] += 1
                    good = True
                    print("{---------------------------------------------------------------}")
                    if stat_choice.lower() == 'str':
                        print("  >>  Strength:", self.stats['str'], "↑")
                    elif stat_choice.lower() == 'dex':
                        print("  >>  Dexterity:", self.stats['dex'], "↑")
                    else:
                        print("  >>  Constitution:", self.stats['con'], "↑")
                    print("{---------------------------------------------------------------}")
        #when finished
        print(" ~ Level up complete! Your stats are now: ~ ")
        print("{---------------------------------------------------------------}")
        print("  >>  Strength:", self.stats['str'])
        print("  >>  Dexterity:", self.stats['dex'])
        print("  >>  Constitution:", self.stats['con'])
        print("{---------------------------------------------------------------}")
        input("[Press enter to continue.]")


    def all_level_up(self):
        """
        A function that calls the previous two functions to allow the character to level up and add to their stats seamlessly.

        Parameters
        ----------
        None
        
        Returns
        -------
        None
        """
        os.system('cls')
        #calculates how many level ups and stat points
        times = self.calc_lvl_up()
        for _ in range(times):
            self.stat_points += 2
        #lets you assign all of them
        self.assign_stat_points(self.stat_points)
        #updates all stats
        self.refresh_stats()
