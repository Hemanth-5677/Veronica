from chatbot_time import *
from chatbot_general import *
from voice_tester import *
from chatbot_genral_2 import chatbot2
while True:
    querry=takecommand()
    # querry=input("enter text here: ")
    chatbot1(querry)
    chatbot2(querry)
    time_bot(querry)
    
