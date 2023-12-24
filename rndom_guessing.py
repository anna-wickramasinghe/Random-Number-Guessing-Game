import random
import pyttsx3

eng=pyttsx3.init()
eng.setProperty("rate",140)
v=eng.getProperty("voices")[1]
eng.setProperty("voice",v.id)
def gamex(a,b):
    x=random.randint(a,b)
    t=0
    audio("please enter your name")
    name=input("Name: ")
    audio(f"Hello {name}, guess a number from {a} to {b}: ")
    while t<5:
        audio("Guess the number : ")
        y=int(input())
        t+=1
        if y>=a and y<=b:
            if y==x and t<5: 
                audio("You have won the game") 
                break
            elif y<x and t<5:
                audio("Try a higher value")
                continue
            elif y>x and t<5:
                audio("Try a lower value")
                continue
            elif t==5 and x==y:
                return audio("You have won the game")
            elif t>=5:
                return audio("You have lost the game, number of attempts are exceeded")
        else:
            return audio(f"Invalid entry! enter in the {a}-{b} range") 
def audio(msg):
    eng.say(msg)
    eng.runAndWait()
    
    
gamex(1,30) #any range