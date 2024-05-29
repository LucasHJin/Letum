from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import time 
from convokit import Corpus, download
time.clock = time.time #because time.clock was depreceated

chatbot = ChatBot("Merchant")

#manually trained it -> didn't use a free database because there were none that conformed to my wishes (i.e. DnD setting)
trainer = ListTrainer(chatbot)
trainer.train([
    "Tell me about this world.",
    "Ah, this world of Letum is a tapestry woven with threads of magic and mystery. It is a realm where gods rise and fall, where heroes are forged in the fires of adversity, and where every step taken may lead to glory or doom.",
])

trainer.train([
    "What can you tell me about this world?",
    "This world of Letum is a place of wonders and dangers, where the boundaries between reality and myth blur. It is a realm where ancient secrets lie buried beneath the earth, waiting to be unearthed by those brave enough to seek them.",
])

trainer.train([
    "I want to know more about this world.",
    "Ah, this world of Letum is a realm of endless possibilities and infinite mysteries. It is a land where the very fabric of reality is shaped by the whims of gods and the will of mortals, where every corner holds a new adventure and every shadow hides a secret.",
])

trainer.train([
    "What's the story behind this world?",
    "The story of this world of Letum is a tale as old as time itself, filled with heroes and villains, triumphs and tragedies. It is a saga of gods and mortals, of battles fought and lost, of destinies intertwined and fates foretold.",
])

trainer.train([
    "Can you describe this world?",
    "This world of Letum is a realm of wonder and peril, where magic flows like a river and danger lurks around every corner. It is a land of ancient ruins and forgotten cities, of dark forests and towering mountains, where adventure awaits those brave enough to seek it.",
])


exit_conditions = ("Q", "q", "Quit", "quit", "L", "l", "Leave", "leave", "exit")
while True:
    query = input(" >> ")
    if query in exit_conditions:
        break
    else:
        print(f"[Kun] {chatbot.get_response(query)}")

