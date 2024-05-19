from weapons import Sword
from armor import Helmet
from armor import Armor
from armor import Ring
import random
import os


#CREATE DICTIONARY OF POSSIBLE ADJECTIVES, SUFFIXES, PREFIXES, MATERIALS, etc. for describing weapons/armor

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
                    inst.decide_stats()
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
                    inst.decide_stats()
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
                    inst.decide_stats()
                    item_cost = 0
                    for extra in inst.added_extra:
                        item_cost += inst.added_extra[extra]*50
                    for stat in inst.added_stats:
                        item_cost += inst.added_stats[stat]*100
                    inst.buy_value = item_cost
                    inst.sell_value = int(item_cost * 0.7)
                    self.items['Rings'].append(inst)
            
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
            print("  >>  "+item.name, "-", item.buy_value, "["+str(counter)+"]")
            counter+=1
        print("{---------------------------------------------------------------}\n")
        print("Helmets")
        print("{---------------------------------------------------------------}")
        counter = 1
        for item in self.items['Helmets']:
            print("  >>  "+item.name, "-", item.buy_value, "["+str(counter)+"]")
            counter+=1
        print("{---------------------------------------------------------------}\n")
        print("Armor")
        print("{---------------------------------------------------------------}")
        counter = 1
        for item in self.items['Armor']:
            print("  >>  "+item.name, "-", item.buy_value, "["+str(counter)+"]")
            counter+=1
        print("{---------------------------------------------------------------}\n")
        print("Rings")
        print("{---------------------------------------------------------------}")
        counter = 1
        for item in self.items['Rings']:
            print("  >>  "+item.name, "-", item.buy_value, "["+str(counter)+"]")
            counter+=1
        print("{---------------------------------------------------------------}\n")

    def open_shop(self):
        self.display_shop()
        self.print_instructions()
        choice = input("  >>  ")
        if choice == "":
            choice = self.not_option()
        choice = choice.split()
            
        while choice[0].lower() != "l":
            if choice[0].lower() == "u":
                if len(choice) == 2:
                    if choice[1].isdigit():
                        if int(choice[1])>=1 and int(choice[1])<=10:
                            os.system('cls')
                            print("Heals 40HP. Takes up 1 turn.")
                            input("[Press any button to return.]")
                            self.display_shop()
                            self.print_instructions()
                            choice = input("  >>  ")
                            if choice == "":
                                choice = self.not_option()
                            choice = choice.split()
                        else:
                            choice = self.not_option()
                    else:
                        choice = self.not_option()
                else:
                    choice = self.not_option()
            elif choice[0].lower() == "w":
                if len(choice) == 2:
                    if choice[1].isdigit():
                        if int(choice[1])>=1 and int(choice[1])<=10:
                            self.print_item(1, choice, choice[0].lower())
                            self.display_shop()
                            self.print_instructions()
                            choice = input("  >>  ")
                            if choice == "":
                                choice = self.not_option()
                            choice = choice.split()
                        else:
                            choice = self.not_option()
                    else:
                        choice = self.not_option()
                else:
                    choice = self.not_option()
            elif choice[0].lower() == "h":
                if len(choice) == 2:
                    if choice[1].isdigit():
                        if int(choice[1])>=1 and int(choice[1])<=10:
                            self.print_item(0, choice, choice[0].lower())
                            self.display_shop()
                            self.print_instructions()
                            choice = input("  >>  ")
                            if choice == "":
                                choice = self.not_option()
                            choice = choice.split()
                        else:
                            choice = self.not_option()
                    else:
                        choice = self.not_option()
                else:
                    choice = self.not_option()
            elif choice[0].lower() == "a":
                if len(choice) == 2:
                    if choice[1].isdigit():
                        if int(choice[1])>=1 and int(choice[1])<=10:
                            self.print_item(0, choice, choice[0].lower())
                            self.display_shop()
                            self.print_instructions()
                            choice = input("  >>  ")
                            if choice == "":
                                choice = self.not_option()
                            choice = choice.split()
                        else:
                            choice = self.not_option()
                    else:
                        choice = self.not_option()
                else:
                    choice = self.not_option()
            elif choice[0].lower() == "r":
                if len(choice) == 2:
                    if choice[1].isdigit():
                        if int(choice[1])>=1 and int(choice[1])<=10:
                            self.print_item(0, choice, choice[0].lower())
                            self.display_shop()
                            self.print_instructions()
                            choice = input("  >>  ")
                            if choice == "":
                                choice = self.not_option()
                            choice = choice.split()
                        else:
                            choice = self.not_option()
                    else:
                        choice = self.not_option()
                else:
                    choice = self.not_option()
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
                        choice = self.not_option()
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
                                    if choice == "":
                                        choice = self.not_option()
                                    choice = choice.split()
                                else:
                                    print("Sorry, you do not have enough Gold. Would you like to buy anything else?")
                                    self.print_instructions()
                                    choice = input("  >>  ")
                                    if choice == "":
                                        choice = self.not_option()
                                    choice = choice.split()
                            else:
                                choice = self.not_option()
                        else:
                            choice = self.not_option()
                        
                else:
                    choice = self.not_option()
            else:
                choice = self.not_option()
                
                
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
            print("  >>  Damage:", int(inst.damage * inst.damage_multiplier))
            if inst.added_stats['str']>0 or inst.added_stats['dex']>0 or inst.added_stats['con']>0:
                print("  >>  Added Stats:")
                if inst.added_stats['str']>0:
                    print("    >>  Strength: +"+str(inst.added_stats['str']))
                if inst.added_stats['dex']>0:
                    print("    >>  Dexterity: +"+str(inst.added_stats['dex']))
                if inst.added_stats['con']>0:
                    print("    >>  Constitution: +"+str(inst.added_stats['con']))
            input("[Press any button to return.]")

    def print_instructions(self):
        print("[Enter the FIRST LETTER of the CATEGORY and NUMBER of the item, WITH SPACES, to see more about it.]")
        print("[Enter [B], followed by the FIRST LETTER of the CATEGORY and NUMBER of the item, WITH SPACES, to buy an item.]")
        print("[Press L to return.]")

    def not_option(self):
        print("That was not an option.")
        self.print_instructions()
        choice = input("  >>  ")
        while choice == "":
            print("That was not an option.")
            self.print_instructions()
            choice = input("  >>  ")
        choice = choice.split()
        return choice