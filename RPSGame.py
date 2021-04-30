import random
import pyttsx3
#import time
options = ['Rock','Paper','Scissors']
name = input("Enter Your Name : ")
voice=pyttsx3.init()
c,p = 0,0
print("")
print("SCORE: COMPUTER - "+str(c)+" "+name.upper()+" - "+str(p))
voice.say("Welcome to the game"+name)
voice.runAndWait()
while(True):
    computer = random.choice(options)
    print("")
    player = input("Rock, Paper, Scissors or Quit : ")
    if computer.lower() == player.lower():
        print("Tie")
        voice.say("Sorry! It's A Tie")
        voice.runAndWait()
    elif player.lower() == 'rock':
        if computer == 'Scissors':
            print(name+" Won! ")
            voice.say(name+"Won!")
            voice.runAndWait()
            p+=1
        else:
            #Venkata Sai Sabbineni
            print("Computer Won! ")
            voice.say("Computer Won!")
            voice.runAndWait()
            c+=1
    elif player.lower() == 'paper':
        if computer == 'Rock':
            print(name+" Won! ")
            voice.say(name+"Won!")
            voice.runAndWait()
            p+=1 
        else:
            print("Computer Won! ")
            voice.say("Computer Won!")
            voice.runAndWait()
            c+=1
    elif player.lower() == 'scissors':
        if computer == 'Paper':
            print(name+" Won! ")
            voice.say(name+"Won!")
            voice.runAndWait()
            p+=1 
        else:
            print("Computer Won! ")
            voice.say("Computer Won!")
            voice.runAndWait()
            c+=1
    elif player.lower() == 'quit' or player.lower() == 'exit':
        voice.say("Thank You For Playing My Rock Paper Scissors Game!"+name)
        voice.runAndWait()
        break
    else:
        print("Wrong Command:(")
        voice.say("Please Enter A Valid Command!")
        voice.runAndWait()
    print(name+" : "+player.upper())
    print("Computer : "+computer.upper())
    print("")
    print("SCORE: COMPUTER - "+str(c)+" "+name.upper()+" - "+str(p))
