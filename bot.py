"""
Final Project
ICS3U
Lucas Jin
This file declares and initializes a chatbot using the chatterbot library from Python. It uses the built in functionalities (i.e. built in database and training) to train the chatbot based on a custom dataset relating to DnD and the lore of this world.
History:
    May 27, 2024: Program Creation
    May 30, 2024: Adding Comments
"""

#Tutorial: https://realpython.com/build-a-chatbot-python-chatterbot/
#chatterbot library: https://github.com/gunthercox/ChatterBot
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import time 
time.clock = time.time #because time.clock was depreceated

#initializing and declaring the chatbot
chatbot = ChatBot("Merchant")

#manually trained it -> didn't use a free database because there were none that conformed to my wishes (i.e. DnD setting)
trainer = ListTrainer(chatbot)

#function to talk with the merchant (to be added to main)
def chatKun():
    """
    Function to let the player communicate with the merchant with functions from chatterbot.
    
    Parameters
    ----------
    None
    
    Returns
    -------
    None
    """
    exit_conditions = ("Q", "q", "Quit", "quit", "L", "l", "Leave", "leave", "exit")
    #continue talking while the user doesn't leave
    while True:
        query = input(" >> ")
        if query in exit_conditions:
            break
        else:
            #print out the merchant's response
            print(f"[Kun] {chatbot.get_response(query)}")

