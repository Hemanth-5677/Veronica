from random import randint as ra
from time import sleep
import re
import pandas as pd
from bs4 import BeautifulSoup
import requests
from voice_tester import speak, takecommand
from datetime import datetime, timedelta
p1=["would you like to hear another one?","if you liked it maybe we can listen to the next one?","one more perhaps?"]

def time_bot(q):
    q=q.lower()
    if "veronica" in q:
        re.sub("veronica","",q)  
    if "date" in q:
        now=datetime.now()
        if "on" in q.lower():
            s=q.split()[-1]
            # print(s)
            for i in range(8):
                m=now+timedelta(days=i)
                # print(m.strftime("%A"))
                if s==m.strftime("%A").lower():
                    print("okay")
                    break
            # print(m)
            if "next" in q:
                m=m+timedelta(days=7)
                print(f"date on next {s} will be "+datetime.date(m).strftime('%d %B %Y'))
                speak(f"date on next {s} will be "+datetime.date(m).strftime('%d %B %Y'))
            elif "is" in q:
                if m==now:
                    print(f"date today is " + datetime.date(m).strftime('%d %B %Y'))
                    speak(f"date today is " + datetime.date(m).strftime('%d %B %Y'))
                else:
                    print(f"date on coming {s} is " + datetime.date(m).strftime('%d %B %Y'))
                    speak(f"date on coming {s} is " + datetime.date(m).strftime('%d %B %Y'))
            elif "was" in q:
                m=m-timedelta(days=7)
                print(f"date on previous {s} was "+datetime.date(m).strftime('%d %B %Y'))
                speak(f"date on previous {s} was "+datetime.date(m).strftime('%d %B %Y'))
        elif "today" in q.lower():print(now.strftime("TODAY is %B %#d %Y"))
        elif "day after" in q.lower():
            d=(datetime.now()+datetime.timedelta(days=2))
            speak(f"on {d.strftime('%A')} date is {d.strftime('is %B %#d %Y')}")
        elif "tomorrow" in q.lower():speak(now.strftime("Tomorrow  is %B %#d %Y")) 
    elif "day"in q:
        now=datetime.now()
        if "today" in q.lower():speak(now.strftime("TODAY is %A"))
        elif "day after" in q.lower():
            d=(datetime.now()+datetime.timedelta(days=2))
            speak(f"on {d.strftime('%A')} day is {d.strftime('is %A')}")
        elif "tomorrow" in q.lower():speak(now.strftime("Tomorrow  is %A"))
        elif "on" in q.lower():
            try:
                m=q.split("on")[1][1:]
                m=pd.to_datetime(m)
                s=int(re.split("-| |:",str(m))[0])
                t=int(re.split("-| |:",str(m))[2])
            except:
                try:
                    m=q.split("on")[1][1:]+" "+str(now.year)
                    m=pd.to_datetime(m)
                    s=int(re.split("-| |:",str(m))[0])
                    t=int(re.split("-| |:",str(m))[2])

                except:
                    m=q.split("on")[1][1:]+" "+str(now.month)+" "+str(now.year)
                    m=pd.to_datetime(m)
                    s=int(re.split("-| |:",str(m))[0])
                    t=int(re.split("-| |:",str(m))[2])
            if s<now.year or (t<now.day and s<now.year) or (t<now.day and s==now.year):
                speak("day on " + datetime.date(m).strftime('%d %B %Y was %A'))
            elif s==now.year and t==now.day:
                speak("day on "+datetime.date(m).strftime('%d %B is %A'))
            elif s>now.year or (t>now.day and s>now.year) or (t>now.day and s==now.year):
                speak("day on "+datetime.date(m).strftime('%d %B will be %A'))
    elif "what is the time" in q:
        now=datetime.now()
        speak(now.strftime("right now....time is %#I %#M %p"))

    elif "on this day" in q or "happned today" in q:
        m=datetime.now()
        month=m.strftime("%B").lower()
        day=m.day
        url = f"https://www.onthisday.com/day/{month}/{day}"
        req = requests.get(url)
        soup = BeautifulSoup(req.content,'html.parser')
        s=soup.main.find_all(lambda tag: tag.name == "li" or tag.name == "a" in tag.text)
        t=[tag.text for tag in s]
        s,ss,f=[],[],True
        for i in range(39,len(t)):
            if t[i]=="Historical Events":
                s.append(i)
                ss.append(t[i])
            if t[i]=="Famous Birthdays":
                s.append(i)
                ss.append(t[i])
                f=False
            if t[i]=="Famous Weddings":
                s.append(i)
                ss.append(t[i])
            if t[i]=="Famous Deaths":
                s.append(i)
                ss.append(t[i])
                f=True
            if t[i]=="Famous Divorces":
                s.append(i)
                ss.append(t[i])
            if t[i]!=t[i-1] and len(t[i].split())>3:
                m=re.findall("[0-9]{3,4}",t[i])
                n=re.findall("\(.{1,6}\)",t[i])
                o=re.findall("[a-zA-Z]{3,8} [0-9]{2}, [0-9]{1,4}",t[i])
                t[i]=re.sub("\.",".....",t[i])
                t[i]=re.sub(":"," - ",t[i])
                if len(n)>1:    t[i]=re.sub("(.+)","",t[i])
                elif len(m)==2 and f:   t[i]=re.sub("[0-9]{4} - [0-9]{4}",f" died on june 10th {m[1]}",t[i])
                elif len(m)==2 and not f:   t[i]=re.sub("[0-9]{4} - [0-9]{4}",f" born on june 10th {m[1]}",t[i])
                elif len(o)>=1: t[i]=re.sub("[a-zA-Z]{3,15} [0-9]{2}, [0-9]{1,4}",f".....{o[0]}" ,t[i])
                elif len(m)==1: t[i]=re.sub("[0-9]{4}",f"{str(m[0])} - " ,t[i])
            # t[i]=re.sub("\,",".............",t[i])
        j=0
        for i in range(len(t)-5):
            if i == s[j]:
                speak(ss[j])
                j+=1
            if t[i]!=t[i-1] and len(t[i].split())>3:
                if "Weekly Quiz" in t[i]:
                    break
                print(f"on {month},{day},"+t[i])
                if "died" not in t[i] and "born" not in t[i]:speak(f"on {day} {month} "+t[i])
                else: speak(t[i])
                sleep(1.5)
        print(o)

# while True:
#     # querry=takecommand()
#     querry=input("Enter the query here : ")
#     time_bot(querry)
