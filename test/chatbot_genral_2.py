
from gtts import gTTS
from io import BytesIO
import pygame
import time
# Initialize pygame
pygame.init()
import json
import random
import re
import speech_recognition as sr
from urllib import request
import datetime
import os
# import whatsapp
from voice_tester import *
o= str(datetime.date(2004, 3, 8))
p="ayush gupta" 
age="17" 
r="student at r.i.s.c " 
s="creating ai like veronica and studying"
b="chandigarh"


def r(text):
    try:
        request.urlopen(f'http://192.168.29.42/{text}')
    except:
        pass

a =json.load(open(r"/home/ubuntu/veronica/data/data.txt","r"))
ss=a["data"][0]
s=list(a["data"][0].keys())
print(s)
t=[]
nd={}
for i in s:
    nd[f"#{i}"]=i
print(nd)

print(s,t)
for i in list(a["data"][0].keys()):
    t.append(f"#{i}")


# speak("veronica is now online sir")
# speak("what would you like to do?")

reflections =json.load(open(r"/home/ubuntu/veronica/data/reflections.txt","r"))

class Chat:
    def __init__(self, pairs, reflections={}):
        """
        Initialize the chatbot.  Pairs is a list of patterns and responses.  Each
        pattern is a regular expression matching the user's statement or question,
        e.g. r'I like (.*)'.  For each such pattern a list of possible responses
        is given, e.g. ['Why do you like %1', 'Did you ever dislike %1'].  Material
        which is matched by parenthesized sections of the patterns (e.g. .*) is mapped to
        the numbered positions in the responses, e.g. %1.

        :type pairs: list of tuple
        :param pairs: The patterns and responses
        :type reflections: dict
        :param reflections: A mapping between first and second person expressions
        :rtype: None
        """

        self._pairs = [(re.compile(x, re.IGNORECASE), y) for (x, y) in pairs]
        self._reflections = reflections
        self._regex = self._compile_reflections()

    def _compile_reflections(self):
        sorted_refl = sorted(self._reflections, key=len, reverse=True)
        return re.compile(
            r"\b({})\b".format("|".join(map(re.escape, sorted_refl))), re.IGNORECASE
        )

    def _substitute(self, str):
        """
        Substitute words in the string, according to the specified reflections,
        e.g. "I'm" -> "you are"

        :type str: str
        :param str: The string to be mapped
        :rtype: str
        """

        return self._regex.sub(
            lambda mo: self._reflections[mo.string[mo.start() : mo.end()]], str.lower()
        )

    def _wildcards(self, response, match):
        pos = response.find("%")
        while pos >= 0:
            num = int(response[pos + 1 : pos + 2])
            response = (
                response[:pos]
                + self._substitute(match.group(num))
                + response[pos + 2 :]
            )
            pos = response.find("%")
        return response

    def respond(self, str):
        """
        Generate a response to the user input.

        :type str: str
        :param str: The string to be mapped
        :rtype: str
        """

        # check each pattern
        for (pattern, response) in self._pairs:
            match = pattern.match(str)

            # did the pattern match?
            if match:
                resp = random.choice(response)  # pick a random response
                resp = self._wildcards(resp, match)  # process wildcards

                # fix munged punctuation at the end
                if resp[-2:] == "?.":
                    resp = resp[:-2] + "."
                if resp[-2:] == "??":
                    resp = resp[:-2] + "?"
                return resp
    # Hold a conversation with a chatbot
    def converse(self,query, quit="satisfied"):
        user_input = ""
        if user_input != quit:
            try:
                user_input = query
            except EOFError:
                print(user_input)
            if 'none' in user_input.lower() or 'none' in str(self.respond(user_input)).lower():
                pass
            elif user_input:
                while user_input[-1] in "!.":
                    user_input = user_input[:-1]
                m=self.respond(user_input)
                if "#" in m:
                    st=re.findall("#[a-zA-z0-9]{3,9},",m)
                    for i in range(len(st)):
                        f=st[i]
                        st[i]=f[:-1]
                    print(st)
                    for i in st:
                        try:m=re.sub(i,ss[nd[i]],m)
                        except:m=re.sub(i,f"{';'.join(list(ss[nd[i]][0]['email']))} and ;;{';'.join(list(ss[nd[i]][0]['password']))}",m)
                print(m)
                speak(m)
        return True

d1=json.load(open(r"/home/ubuntu/veronica/data/chat1.txt","r"))
d2=json.load(open(r"/home/ubuntu/veronica/data/chat2.txt","r"))

def chatbot2(query):
    query=query.replace("*",",")
    chat = Chat(d1, reflections)
    chat2 = Chat(d2, reflections)
    chat.converse(query=query)
    chat2.converse(query=query)



# while True:
# 	x=input("enter the query: ")
# 	y=takecommand()
# 	print(y)

# 	chatbot2(x)
# speak("Hello Raspberry Pi, this is spoken without file storage")
