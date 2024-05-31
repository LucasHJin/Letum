"""
Final Project
ICS3U
Lucas Jin
This is a DnD based text-adventure role playing game. Based on the timeless genre, it is made with OOP and uses a variety of concepts such as functions, lists, dictionaries, variables, etc.
History:
    April 13, 2024: Program Creation
    May 23, 2024: Adding Comments
"""

#ADD COMMENTS
#ADD CLEAR SCREEN WHERE APPROPRIATE

from characters import Character
from weapons import Sword
from battles import Battle
from armor import Helmet
from armor import Armor
from armor import Ring
from shops import Shop
from bot import chatKun
import os
import random

#FUNCTIONS
#--------------------------------------------------------------------------------------------------------------------------
def open_chest(items):
    """
    Function to print out all the items inside a chest.
    
    Parameters
    ----------
    items: {str/Sword/Helmet/Armor/Ring: int}
        Dictionary with all the items and amounts found within a cheset.
    
    Returns
    -------
    None
    """
    print("\nCHEST")
    print("{---------------------------------------------------------------}")
    for i in items.keys():
        if not isinstance(i, Sword) and not isinstance(i, Helmet) and not isinstance(i, Armor) and not isinstance(i, Ring):
            print("  >>  "+i+":", items[i])
        else:
            print("  >>  "+i.name+":", items[i])
    print("{---------------------------------------------------------------}")

def print_options(statements):
    """
    Function to print out all the possible options the player can do.
    
    Parameters
    ----------
    statements: {str: str}
        The key they shuold input and the description of the action.
    
    Returns
    -------
    None
    """
    for k, v in statements.items():
        print("  ["+k+"] "+v)

def random_items(round_num, shop_inst):
    """
    Function to create the items dropped from a chest.
    
    Parameters
    ----------
    round_num: int
        The round number. To be used in determining likelihood of increased rarity, etc. of the items.
    shop_inst: Shop
        The instance of the shop. To access the create_items() method
    
    Returns
    -------
    contain_items: {str/Sword/Helmet/Armor/Ring: int}
        The items obtained from the chest.
    """
    contain_items = {}
    #how much gold
    gold_amount = random.randint(75, 110) * round_num // 2
    player.inventory['Gold'] += gold_amount
    contain_items['Gold'] = gold_amount
    #how many health potions
    hp_amount = random.randint(0, 1) * round_num // 2
    if hp_amount != 0:
        player.inventory['Health Potion'] += hp_amount
        contain_items['Health Potion'] = hp_amount
    #Items
    chance = random.random()
    #based on probability (affected by round number)
    if chance < (0.1 * round_num // 2):
        item_type = random.choices(["Weapons", "Helmets", "Armor", "Rings"], weights = [25, 25, 25, 25], k=1)
        if item_type[0] == "Weapons":
            item_am = [1, 0, 0, 0]
        elif item_type[0] == "Helmets":
            item_am = [0, 1, 0, 0]
        elif item_type[0] == "Armor":
            item_am = [0, 0, 1, 0]
        else:
            item_am = [0, 0, 0, 1]
        temp_item = shop_inst.create_items(item_am)[item_type[0]][0]
        #add to inventory and the contain_items to print later
        player.inventory[temp_item] = 1
        contain_items[temp_item] = 1
    
    return contain_items
    
    

#CHARACTER CREATION
#--------------------------------------------------------------------------------------------------------------------------
os.system('cls')

print(" ~ Hello, I am the Creator. I have brought you to the mystical realm of Letum, where Gods are born and killed. You will recognize my communications with you through '~' symbols. ~ ")
print(" ~ What is your name, oh fine warrior? ~ ")
name = input("  >>  ")
print(" ~ And of what origin are you "+name+"? [Enter your stats below (str, dex, con). Enter [help] for an explanation. **Make sure to separate with a comma and a space.] ~ ")
stats_input = input("  >>  ").split(", ")

if stats_input[0].lower()=="help":
    print("\nWithin the realm of Letum, your abilites are governed by 3 stats:")
    print("  >>  Strength: The stat of the strong and bold, strength grants you the ability to wield your weapon with more efficiency, granting extra damage.")
    print("  >>  Dexterity: The stat of the swift and unseen, dexterity grants you the ability to dodge damage and critically strike.")
    print("  >>  Constitution: The stat of the reliable and resilient, constitution grants you a health equalling your indominatable will.\n")
    print(" ~ With that knowledge, I ask you once again, of what origin are you? [Enter your stats below (str, dex, con). **Make sure to separate with a comma and a space.] ~ ")
    stats_input = input("  >>  ")
    stats_input.split(", ")

check = False

#input validation
while not check:
    #must have 3 stats
    if (len(stats_input)!=3):
        print(" ~ You must have 3 stats and they must all be integers. [Enter your stats below (str, dex, con). **Make sure to separate with a comma and a space.] ~ ")
        #refresh stats_input just in case
        stats_input = ""
        stats_input = input("  >>  ").split(", ")
    #stats can't be letters
    elif stats_input[0].isalpha() or stats_input[1].isalpha() or stats_input[2].isalpha():
        print(" ~ Your stats must be numbers. [Enter your stats below (str, dex, con). **Make sure to separate with a comma and a space.] ~ ")
        stats_input = ""
        stats_input = input("  >>  ").split(", ")
    #stats must be digits
    elif stats_input[0].lstrip("-").isdigit() and stats_input[1].lstrip("-").isdigit() and stats_input[2].lstrip("-").isdigit():
        #change str to int in list
        for i in range(len(stats_input)):
            stats_input[i] = int(stats_input[i])
        #stats must sum to 30
        if (stats_input[0]+stats_input[1]+stats_input[2])!=30 or stats_input[0]<=0 or stats_input[1]<=0 or stats_input[2]<=0:
            print(" ~ Your stats must sum up to 30 and be greater than zero. [Enter your stats below (str, dex, con). **Make sure to separate with a comma and a space.] ~ ")
            stats_input = ""
            stats_input = input("  >>  ").split(", ")
        else:
            check = True
    else:
        check = True

print("\n ~ Thank you for revealing our stats. ~ ")
print(" ~ Your goal is simple. It is to survive as long as possible against an endless horde of monsters. ~ ")
print(" ~ Good luck, and may you leave behind a legacy worthy of your name. ~ ")

input("[Press enter to continue.]")


#START OF THE GAME
#--------------------------------------------------------------------------------------------------------------------------

#clear screen
os.system('cls')

possible = {"L": "Look Around"}

print("You awake groggily, your eyes slowly adapting to the darkness that envelops you. As you lie there, wondering if it is simply a bad dream, you hear a noise skitter by you.")
print_options(possible)
choice = input("  >>  ")
#input validation
while choice.lower() != "l":
    print("That is not an option. The option(s) are: ")
    print_options(possible)
    choice = input("  >>  ")

print("As you look around, you see a rotten wooden chest a few metres to your left. You approach it, wondering what it could possibly contain.")

possible = {"O": "Open The Chest"}
print("What will you do?")
print_options(possible)
choice = input("  >>  ")
#input validation
while choice.lower() != "o":
    print("That is not an option. The option(s) are: ")
    print_options(possible)
    choice = input("  >>  ")


print("\nAs you open the rotting chest, its hinges slowly creaking like the gutteral roar of a ghastly beast, you notice a reflective piece of metal within it. Looking closer, you make out the shape of a sword. Suddenly, it disappears, followed by vocal notifications, seemingly from the same 'Creator' you spoke to previously.")

#initializing the character and weapon and making sure they all have the proper stats
player = Character(name, int(stats_input[0]), int(stats_input[1]), int(stats_input[2]))
weapon = Sword("Old Iron Sword", "Common", player, 0, 0, 0, 0, 0)
player.equipment['Weapon'] = weapon
#refresh stats to set proper stats (like initializing) for player
player.refresh_stats()

contain = {
    'Gold': 50,
    'Health Potion': 5,
    weapon: 1
}
#printing what the chest contains
open_chest(contain)
#adding obtained items to inventory
player.add_inventory(contain)

print(" ~ This is a magical chest. Each time you defeat a wave of monsters, it will be refilled with random items. It may contain gold, health potions, weapons or armor. ~ ")
print(" ~ You might have seen notifications earlier stating that you obtained 100 Gold and 5 Health Potions. All material things will be put in your inventory or equipped onto your body. To check your equipped items, stats, health and more, you will need to access your status. ~ ")
print(" ~ To check what is in your inventory, press [I] when prompted for an input. ~ ")
print(" ~ If you want to check your status and your equipped items, press [S] when prompted for an input. ~ ")
print(" ~ Once finished learning the basics, press [C] to continue. ~ ")

possible = {
    "I": "Open Inventory",
    "S": "Open Status",
    "C": "Continue"
}
print("\nWhat will you do?")
print_options(possible)
choice = input("  >>  ")
#while not continuing
while choice.lower() != "c":
    #check inventory
    if choice.lower() == "i":
        player.check_inventory()
        os.system('cls')
        print_options(possible)
        choice = input("  >>  ")
    elif choice.lower() == "s":
        #check status
        player.check_profile()
        os.system('cls')
        print_options(possible)
        choice = input("  >>  ")
    elif choice.lower() != "c":
        #input validation
        print(" ~ That was not one of the options. The options are: ~ ")
        os.system('cls')
        print_options(possible)
        choice = input("  >>  ")

print("As you wonder what to do now, you here once again the voice in your head.")
print(" ~ I'm unable to say much else due to restrictions but I will try to reveal as much as possible. ~ ")
print(" ~ Very soon, you will be thrust into your first battle. You will have to fight all sorts of horrendous monsters but, if you manage to escape unscathed, you will be much stronger. ~ ")
print(" ~ Additionally, there is one more way to get better equipment and weapons. ~")
print(" ~ Look to your right. ~")
print("Looking to your right, you see a stall, populated with a human like figure. Looking closer, you realise it is a dwarf. Wondering how you never noticed it, the voice suddenly exclaims")
print(" ~ Be not scared. I teleported my loyal follower, Kun, to your location to aid you in your survival. He will sell you items and... who knows, maybe he'll be able to help you with your mentality as well. ~")
print("With that statement, you hear a sudden bang.")
print(" ~ Sorry, it appears I am unable to say more. Good luck! ~ ")
input("[Press enter to continue.]")

#creating the first round's enemy dict -> will always be this regardless of who runs the program
eyDict = {
    'Rat': [1, 0, 0],
    'Goblin': [0, 0, 0],
    'Skeleton': [0, 0, 0],
    'Demon': [0, 0, 0]
}
#instantiating the shop and creating all the items
shop = Shop(player)
shop.call_create()
shop.sort_items()

#instantiating the battles and creating all the necessary variables
rnd = Battle(eyDict, player, weapon, shop)
#result is temp -> filled in later with won or dead, need to not be either to enter the loop
result = "TEMP"
round_counter = 1


POSSIBLE = {
    "I": "Open Inventory",
    "S": "Open Status",
    "B": "Buy Items from the Shop",
    "E": "Equip Equipment",
    "T": "Talk with Kun",
    "F": "Fight"
}
first_talking = True

os.system('cls')
print("What will you do now?")
print_options(POSSIBLE)
choice = input("  >>  ")

#input validation
while choice.upper() not in POSSIBLE:
    os.system('cls')
    print(" ~ That was not one of the options. The options are: ~ ")
    print_options(POSSIBLE)
    choice = input("  >>  ")

while result != "DEAD":
    #while not fight
    while choice.lower() != "f":
        #check invenotry
        if choice.lower() == "i":
            player.check_inventory()
            os.system('cls')
            print_options(POSSIBLE)
            choice = input("  >>  ")
        #check status
        elif choice.lower() == "s":
            player.check_profile()
            os.system('cls')
            print_options(POSSIBLE)
            choice = input("  >>  ")
        #buy items
        elif choice.lower() == "b":
            shop.open_shop()
            os.system('cls')
            print_options(POSSIBLE)
            choice = input("  >>  ")
        #equip items
        elif choice.lower() == "e":
            player.equip_equipment()
            os.system('cls')
            print_options(POSSIBLE)
            choice = input("  >>  ")
        #talking with the merchant
        elif choice.lower() == "t":
            if first_talking:
                #adding this message because chatbot doesn't always work because of lack of training -> incorporating it into the game
                print(" ~ You will now begin talking to my loyal follower, Kun. ~ ")
                print(" ~ But be warned, he has followed me for millenia upon millenia and it has started to corrupt his mind and soul. ~ ")
                print(" ~ So, when talking with him, please phrase your questions properly and try to humour him if he temporarily becomes incoherent. ~ ")
                input("[Press input to continue.]")
                first_talking = False
            os.system('cls')
            print("Conversation")
            print(" ~ Enter 'Q', 'Quit', 'Leave', 'L' or 'Exit' precisely to stop the conversation.")
            print("{---------------------------------------------------------------}")
            chatKun()
            os.system('cls')
            print_options(POSSIBLE)
            choice = input("  >>  ")
        #input validation
        elif choice.lower() != "f":
            os.system('cls')
            print(" ~ That was not one of the options. The options are: ~ ")
            print_options(POSSIBLE)
            choice = input("  >>  ")

    #calling one round
    result = rnd.one_round()
    #if the player survives:
    if result != "DEAD":
        round_counter += 1

        #likelihood of being created
        generate_multipliers = {
            'Rat': [1, 1, 1],    
            'Goblin': [1, 1, 1], 
            'Skeleton': [1, 1, 1], 
            'Demon': [1, 1, 1]
        }
        
        #when the round passes these numbers, the type of enemy can be created and the level (common, elite, boss)
        GENERATE_ROUND_RESTRICTION = {
            'Rat': [1, 5, 10],
            'Goblin': [5, 10, 15],
            'Skeleton': [10, 15, 20],
            'Demon': [15, 20, 25]
        }

        #creating the enemies
        for enemy in eyDict:
            for enemy_type_num in range(len(eyDict[enemy])):
                #adding on likelihood to more earlier types like rats to be created (higher number later on)
                if round_counter % GENERATE_ROUND_RESTRICTION[enemy][enemy_type_num] == 0 and GENERATE_ROUND_RESTRICTION[enemy][enemy_type_num] != 1:
                    generate_multipliers[enemy][enemy_type_num] += 0.5
                else:
                    #Rats increase at a different rate -> so that there aren't hundreds of rats
                    if round_counter % 3 == 0:
                        generate_multipliers['Rat'][0] += 0.5
                
                #amount of enemies
                amount_enemies = 0
                #creating enemies
                if round_counter >= GENERATE_ROUND_RESTRICTION[enemy][enemy_type_num]:
                    #if its the first round they can be created -> always 1
                    if round_counter == GENERATE_ROUND_RESTRICTION[enemy][enemy_type_num]:
                        amount_enemies = 1
                    else:
                        #else use this formula
                        amount_enemies = round_counter//GENERATE_ROUND_RESTRICTION[enemy][enemy_type_num] + random.randint(1, round_counter//GENERATE_ROUND_RESTRICTION[enemy][enemy_type_num]+1)
                #multiply by multiplier for having more weaker enemies and less stronger enemies
                amount_enemies *= int(generate_multipliers[enemy][enemy_type_num])
                #let the enemy dict of this type and rarity be the amount generated
                eyDict[enemy][enemy_type_num] = amount_enemies

        #set the attribute enemiesDict of the Battles class to the new set of enemies
        rnd.enemiesDict = eyDict
        
        print("Congratulations for surviving Round", str(round_counter-1)+". Press [O] to open up your reward chest.")
        choice = input("  >>  ")
        
        #input validation
        while choice.lower() != 'o':
            print("That was not an option. Press [O] to open up your reward chest.")
            choice = input("  >>  ")
        
        #printing out items obtained from the chest and adding to inventory
        contain = random_items(round_counter, shop)
        open_chest(contain)
        input("[Press enter to continue.]")
        
        os.system('cls')
        print("What will you do now?")
        print_options(POSSIBLE)
        choice = input("  >>  ")
        
        #input validation
        while choice.upper() not in POSSIBLE:
            os.system('cls')
            print(" ~ That was not one of the options. The options are: ~ ")
            print_options(POSSIBLE)
            choice = input("  >>  ")
        
#when game is over
print("\n{---------------------------------------------------------------}")
print("YOU SURVIVED FOR", round_counter-1, "ROUNDS. CONGRATULATIONS,", player.name+".")
print("To try again, run the program once more.")