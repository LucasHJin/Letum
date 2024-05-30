from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import time 
time.clock = time.time #because time.clock was depreceated

chatbot = ChatBot("Merchant")

#manually trained it -> didn't use a free database because there were none that conformed to my wishes (i.e. DnD setting)
trainer = ListTrainer(chatbot)

def chatKun():
    exit_conditions = ("Q", "q", "Quit", "quit", "L", "l", "Leave", "leave", "exit")
    while True:
        query = input(" >> ")
        if query in exit_conditions:
            break
        else:
            print(f"[Kun] {chatbot.get_response(query)}")

