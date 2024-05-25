"""
Final Project
ICS3U
Lucas Jin
This file declares the Shop class with all the necessary methods and attributes. It has one instance of itself created at the beginning of the program in main and both buys and sells various items (instances of the equipment).
History:
    April 13, 2024: Program Creation
    May 25, 2024: Adding Comments
"""

from weapons import Sword
from armor import Helmet
from armor import Armor
from armor import Ring
import random
import os


class Shop:
    def __init__(self, character):
        self.character = character
        self.items = {
            'Utility': ["Health Potion"],
            'Weapons': [],
            'Helmets': [],
            'Armor': [],
            'Rings': []
        }
        
    def create_items(self, items_amount):
        #items -> amount [weapon, helmet, armor, ring]
        RARITY_MULT = {
            'Common': 1.0,
            'Uncommon': 1.2,
            'Rare': 1.5,
            'Epic': 2.0,
            'Legendary': 3.0
        }
            
        #Generated these lists with AI
        WORSE_ADJECTIVES = [
            "Rusty", "Old", "Worn", "Tarnished", "Dull", "Faded", "Cracked", 
            "Chipped", "Broken", "Weathered", "Battered", "Fractured", "Rugged", 
            "Scratched", "Bent", "Corroded", "Decayed", "Moldy", "Musty", "Tattered"
        ]
        ADJECTIVES = [
            "Mighty", "Eternal", "Ancient", "Legendary", "Unyielding", "Glorious", 
            "Venerable", "Resplendent", "Mysterious", "Mythical", "Swift", "Stalwart", 
            "Valiant", "Enchanted", "Radiant", "Arcane", "Ethereal", "Spectral", 
            "Blazing", "Gleaming"
        ]
        PREFIXES = [
            "Shadow", "Blood", "Dawn", "Death", "Fire", "Ice", "Storm", "Soul", 
            "Void", "Frost", "Sun", "Moon", "Thunder", "Dragon", "Celestial", 
            "Inferno", "Oath", "Demon", "Fey", "Rune"
        ]
        SUFFIXES = [
            "blade", "edge", "fang", "brand", "caller", "reaver", "thirster", 
            "keeper", "slayer", "whisper", "bane", "strike", "clap", "shadow", 
            "thunder", "claw", "hammer", "crown", "crescent", "harbinger", "hunter"
        ]
        NOUNS = [
            "Sword", "Blade", "Saber", "Scimitar", "Rapier", "Cutlass", "Katana", 
            "Longsword", "Bastard Sword", "Greatsword", "Claymore", "Dagger", 
            "Broadsword", "Warblade", "Falchion", "Gladius", "Dirk", "Kris", 
            "Katana", "Tanto"
        ]
        HELMET_NOUNS = [
            "Helm", "Visage", "Headgear", "Cap", "Crown", "Mask", "Veil", "Crest", 
            "Hood", "Visor", "Coif", "Circlet", "Tiara", "Casque", "Cowl"
        ]
        ARMOR_NOUNS = [
            "Armor", "Cuirass", "Plate", "Harness", "Mail", "Hauberk", "Vest", "Jacket", 
            "Robe", "Garb", "Tabard", "Tunic", "Brigandine", "Vestments", "Surcoat"
        ]
        RING_NOUNS = [
            "Ring", "Band", "Circle", "Loop", "Hoop", "Bandlet", "Bangle", "Orb", 
            "Sphere", "Jewel", "Gem", "Stone", "Amulet", "Charm", "Token"
        ]
        for amount in range(len(items_amount)):
            for _ in range(items_amount[amount]):
                item_a = random.choice(ADJECTIVES)
                item_a2 = random.choice(WORSE_ADJECTIVES)
                item_p = random.choice(PREFIXES)
                item_s = random.choice(SUFFIXES)
                item_n = random.choice(NOUNS)
                item_hn = random.choice(HELMET_NOUNS)
                item_bn = random.choice(ARMOR_NOUNS)
                item_rn = random.choice(RING_NOUNS)
                
                RARITY_LIST = ["Common", "Uncommon", "Rare", "Epic", "Legendary"]
                item_rarity = random.choices(RARITY_LIST, weights = [50, 25, 15, 7.5, 2.5], k=1)
                
                if amount == 0:
                    if item_rarity[0]=="Common" or item_rarity[0]=="Uncommon":
                        item_name = item_a2 + " " + item_p + item_s + "'s " + item_n
                        inst = Sword(item_name, item_rarity[0], self.character, 0, 0, 0, 0, 0)
                        item_cost = inst.damage*225 + int(inst.damage*inst.damage_multiplier*10)
                        item_sell = int(item_cost * 0.7)
                        inst.buy_value = item_cost
                        inst.sell_value = item_sell
                    else:
                        item_name = item_a + " " + item_p + item_s + "'s " + item_n
                        points = int(random.randint(1, 2) * RARITY_MULT[item_rarity[0]])
                        #print("POINTS", points)
                        split_points = random.choices(['str', 'dex', 'con'], weights=[2, 1, 1], k=points)
                        #print("SPLIT POINTS", split_points)
                        added_stats = {
                            'str': 0,
                            'dex': 0,
                            'con': 0
                        }
                        added_stats['str']=split_points.count('str')
                        added_stats['dex']=split_points.count('dex')
                        added_stats['con']=split_points.count('con')
                        #print("ADDED", added_stats)
                        inst = Sword(item_name, item_rarity[0], self.character, 0, 0, int(added_stats["str"]), int(added_stats["dex"]), int(added_stats["con"]))
                        #print("AFTER", inst.added_stats)
                        item_cost = points*300 + inst.damage*250 + int(inst.damage*inst.damage_multiplier*10)
                        item_sell = int(item_cost * 0.7)
                        inst.buy_value = item_cost
                        inst.sell_value = item_sell
                    self.items['Weapons'].append(inst)
                elif amount == 1:
                    item_name = item_a2 + " " + item_p + item_s + "'s " + item_hn
                    inst = Helmet(name=item_name, rarity=item_rarity[0], buy_value=0, sell_value=0)
                    inst.decide_stats([2, 3, 4], [3, 3, 1])
                    item_cost = 0
                    for extra in inst.added_extra:
                        item_cost += inst.added_extra[extra]*50
                    for stat in inst.added_stats:
                        item_cost += inst.added_stats[stat]*100
                    inst.buy_value = item_cost
                    inst.sell_value = int(item_cost * 0.7)
                    self.items['Helmets'].append(inst)
                elif amount == 2:
                    item_name = item_a2 + " " + item_p + item_s + "'s " + item_bn
                    inst = Armor(name=item_name, rarity=item_rarity[0], buy_value=0, sell_value=0)
                    inst.decide_stats([4, 2, 4], [3, 3, 1])
                    item_cost = 0
                    for extra in inst.added_extra:
                        item_cost += inst.added_extra[extra]*50
                    for stat in inst.added_stats:
                        item_cost += inst.added_stats[stat]*100
                    inst.buy_value = item_cost
                    inst.sell_value = int(item_cost * 0.7)
                    self.items['Armor'].append(inst)
                else:
                    item_name = item_a2 + " " + item_p + item_s + "'s " + item_rn
                    inst = Ring(name=item_name, rarity=item_rarity[0], buy_value=0, sell_value=0)
                    inst.decide_stats([3, 2, 1], [2, 1, 4])
                    item_cost = 0
                    for extra in inst.added_extra:
                        item_cost += inst.added_extra[extra]*50
                    for stat in inst.added_stats:
                        item_cost += inst.added_stats[stat]*100
                    inst.buy_value = item_cost
                    inst.sell_value = int(item_cost * 0.7)
                    self.items['Rings'].append(inst)
          
    def sort_items(self):
        #https://stackoverflow.com/questions/403421/how-do-i-sort-a-list-of-objects-based-on-an-attribute-of-the-objects
        for items_type in self.items:
            if items_type != "Utility":
                self.items[items_type].sort(key=lambda x: x.buy_value, reverse=False)   
      
    def display_shop(self):
        os.system('cls')
        print("SHOP")
        print("Utility")
        print("{---------------------------------------------------------------}")
        print("  >>  Health Potion [1]")
        print("{---------------------------------------------------------------}\n")
        print("Weapons")
        print("{---------------------------------------------------------------}")
        counter = 1
        for item in self.items['Weapons']:
            print("  ["+str(counter)+"]  "+item.name, "-", str(item.buy_value)+"G - "+item.rarity)
            counter+=1
        print("{---------------------------------------------------------------}\n")
        print("Helmets")
        print("{---------------------------------------------------------------}")
        counter = 1
        for item in self.items['Helmets']:
            print("  ["+str(counter)+"]  "+item.name, "-", str(item.buy_value)+"G - "+item.rarity)
            counter+=1
        print("{---------------------------------------------------------------}\n")
        print("Armor")
        print("{---------------------------------------------------------------}")
        counter = 1
        for item in self.items['Armor']:
            print("  ["+str(counter)+"]  "+item.name, "-", str(item.buy_value)+"G - "+item.rarity)
            counter+=1
        print("{---------------------------------------------------------------}\n")
        print("Rings")
        print("{---------------------------------------------------------------}")
        counter = 1
        for item in self.items['Rings']:
            print("  ["+str(counter)+"]  "+item.name, "-", str(item.buy_value)+"G - "+item.rarity)
            counter+=1
        print("{---------------------------------------------------------------}\n")

    def open_shop(self):
        GOOD_INPUT = ['l', 'u', 'w', 'h', 'a', 'r']

        self.display_shop()
        self.print_instructions()
        choice = input("  >>  ")
        choice = self.not_option(choice)

        print("ASDL CJAFWFQ")
        print(choice)
            
        while choice[0].lower() != "l":
            if choice[0].lower() == "u":
                if len(choice) == 2:
                    if choice[1].isdigit():
                        if int(choice[1])==1:
                            os.system('cls')
                            print("Health Potion")
                            print("{---------------------------------------------------------------}")
                            print("Heals 40HP. Takes up 1 turn.")
                            input("[Press any button to return.]")
                            self.display_shop()
                            self.print_instructions()
                            choice = input("  >>  ")
                            if choice[0] not in GOOD_INPUT:
                                choice = self.not_option(choice)
                        else:
                            choice = self.not_option(choice)
                    else:
                        choice = self.not_option(choice)
                else:
                    choice = self.not_option(choice)
            elif choice[0].lower() == "w":
                if len(choice) == 2:
                    if choice[1].isdigit():
                        if int(choice[1])>=1 and int(choice[1])<=20:
                            self.print_item(1, choice, choice[0].lower())
                            self.display_shop()
                            self.print_instructions()
                            choice = input("  >>  ")
                            if choice[0] not in GOOD_INPUT:
                                choice = self.not_option(choice)
                        else:
                            choice = self.not_option(choice)
                    else:
                        choice = self.not_option(choice)
                else:
                    choice = self.not_option(choice)
            elif choice[0].lower() == "h":
                if len(choice) == 2:
                    if choice[1].isdigit():
                        if int(choice[1])>=1 and int(choice[1])<=10:
                            self.print_item(0, choice, choice[0].lower())
                            self.display_shop()
                            self.print_instructions()
                            choice = input("  >>  ")
                            if choice[0] not in GOOD_INPUT:
                                choice = self.not_option(choice)
                        else:
                            choice = self.not_option(choice)
                    else:
                        choice = self.not_option(choice)
                else:
                    choice = self.not_option(choice)
            elif choice[0].lower() == "a":
                if len(choice) == 2:
                    if choice[1].isdigit():
                        if int(choice[1])>=1 and int(choice[1])<=10:
                            self.print_item(0, choice, choice[0].lower())
                            self.display_shop()
                            self.print_instructions()
                            choice = input("  >>  ")
                            if choice[0] not in GOOD_INPUT:
                                choice = self.not_option(choice)
                        else:
                            choice = self.not_option(choice)
                    else:
                        choice = self.not_option(choice)
                else:
                    choice = self.not_option(choice)
            elif choice[0].lower() == "r":
                if len(choice) == 2:
                    if choice[1].isdigit():
                        if int(choice[1])>=1 and int(choice[1])<=10:
                            self.print_item(0, choice, choice[0].lower())
                            self.display_shop()
                            self.print_instructions()
                            choice = input("  >>  ")
                            if choice[0] not in GOOD_INPUT:
                                choice = self.not_option(choice)
                        else:
                            choice = self.not_option(choice)
                    else:
                        choice = self.not_option(choice)
                else:
                    choice = self.not_option(choice)
            elif choice[0].lower() == "b":
                if len(choice) == 3:
                    POSSIBLE = ['u', 'w', 'h', 'a', 'r']
                    CATEGORY_CONVERSION = {
                        'u': "Utility",
                        'w': "Weapons", 
                        'h': "Helmets",
                        'a': "Armor",
                        'r': "Rings"
                    }
                    found = False
                    category = "a"
                    for i in POSSIBLE:
                        if choice[1].lower() == i:
                            found = True
                            category = i
                    if not found:
                        choice = self.not_option(choice)
                    else:
                        if choice[2].isdigit():
                            if int(choice[2])>=1 and int(choice[2])<=10:
                                inst = self.items[CATEGORY_CONVERSION[category]][int(choice[2])-1]
                                if inst=="Health Potion":
                                    name = inst
                                    price = 50
                                else:
                                    name = inst.name
                                    price = inst.buy_value
                                if price<=self.character.inventory['Gold']:
                                    print("You have bought ["+name+"].")
                                    self.character.inventory['Gold']-=price
                                    print("You have", self.character.inventory['Gold'], "Gold remaining.")
                                    if inst in self.character.inventory:
                                        self.character.inventory[inst]+=1
                                    else:
                                        self.character.inventory[inst]=1
                                    os.system('cls')
                                    self.display_shop()
                                    print("Thanks for buying an item. Would you like to buy anything else?")
                                    self.print_instructions()
                                    choice = input("  >>  ")
                                    if choice[0] not in GOOD_INPUT:
                                        choice = self.not_option(choice)
                                else:
                                    print("Sorry, you do not have enough Gold. Would you like to buy anything else?")
                                    self.print_instructions()
                                    choice = input("  >>  ")
                                    if choice[0] not in GOOD_INPUT:
                                        choice = self.not_option(choice)
                            else:
                                choice = self.not_option(choice)
                        else:
                            choice = self.not_option(choice)
                        
                else:
                    choice = self.not_option(choice)
            elif choice[0].lower() == 's' and len(choice) == 1:
                self.sell_item()
                os.system('cls')
                self.display_shop()
                print("Thank you for selling an item. What would you like to do now?")
                self.print_instructions()
                choice = input("  >>  ")
                if choice[0] not in GOOD_INPUT:
                    choice = self.not_option(choice)
            else:
                choice = self.not_option(choice)
                
                
    def print_item(self, val, choice, letter):
        if val==0:
            POSSIBLEDICT = {
                'h': "Helmets",
                'a': "Armor",
                'r': "Rings"
            }
            os.system('cls')
            inst = self.items[POSSIBLEDICT[letter.lower()]][int(choice[1])-1]
            print(inst.name)
            print("{---------------------------------------------------------------}")
            print("  >>  Cost:", inst.buy_value)
            print("  >>  Sell Value:", inst.sell_value)
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
            input("[Press any button to return.]")

    def print_instructions(self):
        print("  >>  [Enter the FIRST LETTER of the CATEGORY and NUMBER of the item, WITH SPACES, to see more about it.]")
        print("  >>  [Enter [B], followed by the FIRST LETTER of the CATEGORY and NUMBER of the item, WITH SPACES, to buy an item.]")
        print("  >>  [Enter [S] to initiate the selling process.]")
        print("  >>  [Press [L] to return.]")

    def not_option(self, choice):
        #DO IT BASED ON LEN 0, LEN1, LEN 2, LEN 3
        GOOD_CHECK = ['u', 'w', 'h', 'a', 'r']
        passed = False

        while not passed:
            if choice:
                #https://stackoverflow.com/questions/2184955/test-if-a-variable-is-a-list-or-tuple
                if type(choice) is not list:
                    choice = choice.split()
                if len(choice) == 1:
                    if choice[0].lower() == "s" or choice[0].lower() == "l":
                            passed = True
                elif len(choice) == 2:
                    if choice[0].lower() in GOOD_CHECK:
                        if choice[0].lower() == "u":
                            if choice[1].isdigit():
                                if int(choice[1]) == 1:
                                    passed = True
                        else:
                            if choice[1].isdigit():
                                if int(choice[1]) >= 1 and int(choice[1]) <=10:
                                    passed = True
                elif len(choice) == 3:
                    if choice[0].lower() == "b":
                        if choice[1].lower() in GOOD_CHECK:
                            if choice[1].lower() == "u":
                                if choice[2].isdigit():
                                    if int(choice[2]) == 1:
                                        passed = True
                            else:
                                if choice[2].isdigit():
                                    if int(choice[2]) >= 1 and int(choice[2]) <=10:
                                        passed = True
            if not passed:
                print("That was not an option.")
                self.print_instructions()
                choice = input("  >>  ")
        #double check (make sure split)
        if type(choice) is not list:
            choice = choice.split()
        return choice
    
    
    def sell_item(self):
        self.display_inventory_sell_price()
        print("What item do you want to sell? (Enter the number of the item or press [L] to leave.)")
        choice_item = input("  >>  ").strip()
        sell_price = 0
        check = False
        check_equipped = False
        inv_list = list(self.character.inventory.keys())
        
        if choice_item.isdigit():
            if int(choice_item) > 2 and int(choice_item) <= len(inv_list):
                item_sell = inv_list[int(choice_item)-1]
                for item_type in self.character.equipment:
                    if self.character.equipment[item_type] == item_sell:
                        check_equipped = True
                        break
                if not check_equipped:
                    check = True
                    sell_price = item_sell.sell_value
        elif choice_item.lower() == 'l':
            check = True
                
        while not check:
            check_equipped = False
            print("That was not a valid choice. (Please note that you are unable to sell gold or potions. Additionally, you are unable to sell any equipment that you currently have equipped. You may also press [L] to leave.)")
            choice_item = input("  >>  ").strip()
            if choice_item.isdigit():
                if int(choice_item) > 2 and int(choice_item) < len(inv_list):
                    item_sell = inv_list[int(choice_item)-1]
                    for item_type in self.character.equipment:
                        if self.character.equipment[item_type] == item_sell:
                            check_equipped = True
                            break
                    if not check_equipped:
                        check = True
                        sell_price = item_sell.sell_value
            elif choice_item.lower() == 'l':
                check = True

        if choice_item.lower() != 'l':
            self.character.inventory['Gold'] += sell_price
            #https://note.nkmk.me/en/python-dict-clear-pop-popitem-del
            self.character.inventory.pop(item_sell)
            print("You have sold", item_sell.name, "and gained", str(sell_price), "Gold.")
            input("[Press enter to continue.]")
        else:
            print("Be sure to come back and sell items if you change your mind.")
            input("[Press enter to continue.]")
        
        
    def display_inventory_sell_price(self):
        os.system('cls')
        count = 0
        print("INVENTORY")
        print("{---------------------------------------------------------------}")
        for i in self.character.inventory.keys():
            if not isinstance(i, Sword) and not isinstance(i, Helmet) and not isinstance(i, Armor) and not isinstance(i, Ring):
                print("["+str(count+1)+"] "+i+":", self.character.inventory[i], "- N/A")
            else:
                print("["+str(count+1)+"] "+i.name+":", self.character.inventory[i], "-", str(i.sell_value)+"G")
            count+=1
        print("{---------------------------------------------------------------}")