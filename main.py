"""
Final Project
ICS3U
Lucas Jin
This is a DnD based text-adventure role playing game. Based on the timeless genre, it is made with OOP and uses a variety of concepts such as functions, lists, dictionaries, variables, etc.
History:
April 13, 2023: Program Creation
"""
from characters import Character
from weapons import Sword

#CHARACTER CREATION
print("Welcome to the mystical realm of Letum, where Gods are born and killed. What is your name, oh fine warrior?")
name = input("  >>  ")
print("And of what origin are you "+name+"? [Enter your stats below (str, dex, con). Enter 'help' for an explanation.]")
stats_input = input("  >>  ")

if stats_input.lower()=="help":
    print("\nWithin the realm of Letum, your abilites are governed by 3 stats:")
    print("  >>  Strength: The stat of the strong and bold, strength grants you the ability to wield your weapon with more efficiency, granting extra damage.")
    print("  >>  Dexterity: The stat of the swift and unseen, dexterity grants you the ability to dodge damage and critically strike.")
    print("  >>  Constitution: The stat of the reliable and resilient, constitution grants you a health equalling your indominatable will.\n")
    print("With that knowledge, I ask you once again, of what origin are you? [Enter your stats below (str, dex, con).]")
    stats_input = input("  >>  ")
stats_input = stats_input.split(", ")

#change str to int in list
stats_input = [eval(i) for i in stats_input]

print(stats_input)

while (stats_input[0]+stats_input[1]+stats_input[2])!=30 or stats_input[0]==0 or stats_input[1]==0 or stats_input[2]==0 or len(stats_input)!=3:
    print("Your stats must sum up to 30 and each one must have at least 1 stat point assigned to it. [Enter your stats below (str, dex, con).]")
    stats_input = input("  >>  ")
    stats_input = stats_input.split(", ")



#START OF THE GAME



print("And what mighty weapon do you wield? [Sword, Dagger, Staff]")






weapon_input = input("  >>  ")

player = Character(name=name, str=int(stats_input[0]), dex=int(stats_input[1]), con=int(stats_input[2]), level=1, exp=0)

if weapon_input.lower()=="sword":
    weapon = Sword(name="Old Iron Sword", rarity="Common", character=player)

player.refresh_stats()

print(player.health)
print(player.attack_damage)
print(weapon.damage_multiplier)
print(weapon.damage)
print(weapon.slash())