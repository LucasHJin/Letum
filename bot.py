from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import time 
time.clock = time.time

chatbot = ChatBot("Merchant")

conversations = [
    "This field seems endless, and the monsters keep coming!",
    "Indeed, it feels like we're trapped in a never-ending nightmare.",
    "We must keep fighting, lest we be overwhelmed by the horde!",
    "Agreed! With each monster we defeat, we gain a moment of respite.",
    "Look out! A group of goblins is approaching from the east!",
    "I'll take care of the goblins. You focus on defending our flank.",
    "Skeletons are emerging from the ground! We're surrounded!",
    "Stay calm! We'll fight our way out of this together.",
    "Rats! They're crawling out of every crevice!",
    "I'll create a barrier with my spells. You focus on taking out the rats.",
    "A demon! Its presence fills the air with dread!",
    "We cannot let fear paralyze us. We must stand firm and face the demon!",
    "We've been fighting for hours. Will this ever end?",
    "It may seem endless, but we must not lose hope. Our perseverance will prevail.",
    "I see a portal opening in the distance! We must make a break for it!",
    "To the portal! Let us escape this endless onslaught and live to fight another day!",
    "We made it through the portal! We're safe... for now.",
    "Indeed, but our journey is far from over. We must continue to hone our skills and prepare for the next challenge."
]

trainer = ListTrainer(chatbot)
trainer.train(conversations)

exit_conditions = (":q", "quit", "exit")
while True:
    query = input(" >> ")
    if query in exit_conditions:
        break
    else:
        print(f"[Kun] {chatbot.get_response(query)}")

