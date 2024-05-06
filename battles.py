from enemies import Rat
from enemies import Goblin
from enemies import Skeleton
from enemies import Demon
import random
from main import player

class Battle:
    def __init__(self, enemies, character):
        self.enemies = enemies
        self.character = character
        turn = 1

    def turn(self):
        #have each enemy and character go once in a turn (loop iterate) AND check for death and if so remove that character
        temp = 1

    def create_enemy_instances(self):
        enemy_instances = {
            'Rat': [],
            'Goblin': [],
            'Skeleton': [],
            'Demon': []
        }
        for enemy_key in self.enemies:
            enemy_amount = 0
            for type_amount in self.enemies[enemy_key]:
                counter = 1
                for count in range(type_amount):
                    #https://www.w3schools.com/python/ref_string_format.asp -> for naming instance
                    instance_name = "{}{}".format(enemy_key, count)
                    if enemy_key == "Rat":
                        if counter == 1:
                            instance = Rat(instance_name, "Common", player)
                        elif counter == 2:
                            instance = Rat(instance_name, "Elite", player)
                        else:
                            instance = Rat(instance_name, "Boss", player)
                        enemy_instances['Rat'].append(instance)
                    elif enemy_key == "Goblin":
                        if counter == 1:
                            instance = Goblin(instance_name, "Common", player)
                        elif counter == 2:
                            instance = Goblin(instance_name, "Elite", player)
                        else:
                            instance = Goblin(instance_name, "Boss", player)
                        enemy_instances['Goblin'].append(instance)
                    elif enemy_key == "Skeleton":
                        if counter == 1:
                            instance = Skeleton(instance_name, "Common", player)
                        elif counter == 2:
                            instance = Skeleton(instance_name, "Elite", player)
                        else:
                            instance = Skeleton(instance_name, "Boss", player)
                        enemy_instances['Skeleton'].append(instance)
                    else:
                        if counter == 1:
                            instance = Demon(instance_name, "Common", player)
                        elif counter == 2:
                            instance = Demon(instance_name, "Elite", player)
                        else:
                            instance = Demon(instance_name, "Boss", player)
                        enemy_instances['Demon'].append(instance)
                counter+=1

