# Letum
Letum is an RPG turn-based text game, made with OOP, machine learning and Python. The majority of the game is made possible with classes and the machine learning generates dialogue for the player to interact with NPCs. Within the game, you are playing as a person who was summoned to the world by a Goddess. Your goal is to survive as long as possible by leveling up, upgrading your stats, buying and discovering new weapons and armors and fighting against all types of enemies including Rats, Goblins, Skeletons and Demons, each with their own tiers of strength.

## Features
- You are able to fight in turn based battles
   - Within these battles, there are status effects, buffs, damaging abilties, etc.
   - You can unlock weapons, armor, consumables and gold from these battles (opening chests and killing enemies)
- You are able to visit the shop
   - Within the shop, you can chat with the shopkeeper (work in progress)
   - You are able to buy various items that improve your stats and abilities
   - You can also sell items
- You are able to upgrade your stats by leveling up (this improves your survivability and damage)

## Installation and Running
### Prerequisites
1. **Python Version**: This project is able to run on most versions of Python. Ensure that you have Python installed (python.org).

2. **pip**: Ensure that you have pip installed. It typically comes with Python, but you can check and install it using:
```sh
   python -m ensurepip --upgrade
```

3. **Chatterbot**: Install the chatterbot library to be able to access the AI portions of this code:
```sh
   pip install chatterbot==1.0.4
```

### Installation
1. **Clone the Repository**:
```sh
   git clone git@github.com:LucasHJin/Letum.git
```

2. **Open the Repository**: Open the repository in any code editor of your preference (i.e. VSCode).

3. **Run the Program**: You should now be able to run the program.

## Known Bugs
- The chatbot isn't advanced enough to have a proper conversation most of the time. Only some of the time can it have a proper conversation (it can respond to basic greetings and goodbye)
- You are able to increase your health, armor class and damage by repeatedly equipping equipment
   - This will not repeatedly increase your stats (str/dex/con) only the aforementioned values

## Cheat codes
- There are no cheat codes within the game as the goal is simply to survive as long as possible
   - However, here are some tips to survive longer:
      - When looking through the weapons in the shop, the rarity of rare is probably the most cost efficient as it allows you an AOE attack that hits all enemies
         Note that the amount of enemies augments exponentially as rounds go by so buying a weapon with an AOE as soon as possible will be important
      - Investing in dexterity has diminishing returns but is more worthwhile earlier
         - On the other hand, investing in strength and constitution will help you deal more damage and stay alive consistently throughout the entire game
      - Target bosses and elites as well as harder mobs such as Demons instead of Rats
         - Use the AOE to take care of small mobs and focus on the larger enemies as they deal a lot more damage
      - Don't buy health potions from the shop
         - It is a waste of gold as many will drop from the enemies naturally

## Support
In case of any problems, contact:
- Lucas J. - kblazer20@gmail.com

## Sources
- https://docs.google.com/document/d/1F1rFOp_7X4bLbj4QpG3uGhUACjmGZ3tqvgm5Gg0bpM8/edit?usp=sharing
- ChatGPT:
   - Generating data to train the chatbot with chatgpt