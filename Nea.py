print("welcome to the....")
#hello i am the secret commenter, i write these comments to keep my sanity :)
import random
import time
import os
import sys
import datetime#defining things and importing functions...
from tkinter import *
import tkinter as tk
player1score=0
player2score=0
Round=1
total = 0
time.sleep(1)
yes = False
print("______ _____ _____  _____   _____   ___  ___  ___ _____ ")
print("|  _  \_   _/  __ \|  ___| |  __ \ / _ \ |  \/  ||  ___|")
print("| | | | | | | /  \/| |__   | |  \// /_\ \| .  . || |__  ")
print("| | | | | | | |    |  __|  | | __ |  _  || |\/| ||  __| ")
print("| |/ / _| |_| \__/\| |___  | |_\ \| | | || |  | || |___ ")
print("|___/  \___/ \____/\____/   \____/\_| |_/\_|  |_/\____/ ")
#below is a really ineffective way of doing this its late i cba to think-this could be done with one huge multidimesional array maybe?                                                      
print("A captcha has appeared somewhere, look for it ")

#----TODO------
#-add a cool 'logbook' of every game played and its results
#-fix the reultslist not sorting thing
#-work out exactly what to display when asked for scores----maybe even have a choice between top 5,10,15,20 etc...
#-make a 'main menu' where you can view scores,logbook,maybe even have a nice GUI if i can
#-comment/make it readable
#-make all the text the user sees look nice :)
#-add more 'stuff' because i can :)
#-check every sanitised input
#-get rid of repeatable thing(s)
#-turn (newresultslist into a multidimensional array for showing to end user :::))))
#--------------
def tkintermenu():

    def myClick():
    
        myLabel = Label(GUI_Window, text = 'VERIFIED-HUMAN-PLEASE-CLOSE-THIS-NOW')
        myLabel.grid(row =1, column = 0,)
        
    GUI_Window = tk.Tk()

    myButton = Button(GUI_Window, text='PRESS-HERE-TO-PROVE-YOU-ARE-HUMAN', command = myClick,fg = "green",bg = "black")
    myButton.grid(row =0, column = 0)
    time.sleep(1)
    
    GUI_Window.mainloop()


tkintermenu()

def rdiewas1():
    print("+-----+") 
    print("|     |")   
    print("|  o  |")  
    print("|     |")  
    print("+-----+")
    return
  
def rdiewas2():
    print("+-----+") 
    print("| o   |")   
    print("|     |")  
    print("|    o|")  
    print("+-----+")
    return

def rdiewas3():
    print("+-----+") 
    print("|o    |")   
    print("|  o  |")  
    print("|    o|")  
    print("+-----+")
    return

def rdiewas4():
    print("+-----+") 
    print("|o   o|")   
    print("|     |")  
    print("|o   o|")  
    print("+-----+")
    return

def rdiewas5():
    print("+-----+") 
    print("|o   o|")   
    print("|  o  |")  
    print("|o   o|")  
    print("+-----+")
    return

def rdiewas6():
    print("+-----+") 
    print("|o   o|")   
    print("|o   o|")  
    print("|o   o|")  
    print("+-----+")
    return
#---------------------------------------------

def ediewas1():
    print("+-----+") 
    print("|     |")   
    print("|  o  |")  
    print("|     |")  
    print("+-----+")
    return
  
def ediewas2():
    print("+-----+") 
    print("| o   |")   
    print("|     |")  
    print("|    o|")  
    print("+-----+")
    return

def ediewas3():
    print("+-----+") 
    print("|o    |")   
    print("|  o  |")  
    print("|    o|")  
    print("+-----+")
    return

def ediewas4():
    print("+-----+") 
    print("|o   o|")   
    print("|     |")  
    print("|o   o|")  
    print("+-----+")
    return

def ediewas5():
    print("+-----+") 
    print("|o   o|")   
    print("|  o  |")  
    print("|o   o|")  
    print("+-----+")
    return

def ediewas6():
    print("+-----+") 
    print("|o   o|")   
    print("|o   o|")  
    print("|o   o|")  
    print("+-----+")
    return

#I could probably have an algorithm that generates that ASCII art but 'nah'

logbookquery = input("before we start,would you like to view the logboooks entrys?(Y/N)")

if logbookquery == "Y":
    time.sleep(1)
    print("gaining access to the logbook...")
    f = open("LOGBOOK.txt","r")
    logbookboop = f.readlines()
    f.close()
    for line in logbookboop:
        print(line)

else:
    print("righty tighty,moving on..not diplaying logbook")









def newuser():#um so it doesnt work if both players are new.....meh why would they be im the only one using this so it probs doesnt matter
    print("NEW-USER-PLEASE-REGISTER-")
    file = open("accountfile.txt","r+")
    text = file.read().strip().split()
    check = True
    while check:
        username=input("Please enter appropiate username: ") #Takes input of a username from user
        if username == "": #if no value is entered for the username
            continue
        if username in text: #username in present in the text file
            print("Username is taken please try another one")
        else: #username is absent in the text file
            print("Username has been accepted")
            check = False
            check = True
            while check:
                password1=input("Please enter password: ")
                password2=input("Please re-enter password for security: ")
                if password1 == password2:
                    if password2 in text:
                        print("Password has been taken please try another one")
                    else:
                        print("Username and Password have sucessfully been made Thankyou")
                        file.write("username: " + username + " " + "password: " + password2 + "\n")
                        file.close()
                        check = False
                        
                else:
                    print("passwords do not match please try again")                         
    file.close()


def existing():
    global username1
    global username2
    global player1cred
    global player2cred
    counter = 0 
    check_failed = True
    while check_failed:
        print("Could player 1 enter their username and password")
        username1=input("Please enter your username ")
        password=input("Please enter your password ")
        with open("accountfile.txt","r") as username_finder:
            for line in username_finder:
                if ("username: " + username1 + " password: " + password) == line.strip():
                    player1cred = line.strip()
                    print("player1,you are logged in")
                    check_failed = False
                    check_failed = True
                    while check_failed:
                        print("Could player 2 enter their username and password")
                        username2=input("Please enter your username ")
                        password=input("Please enter your password ")
                        with open("accountfile.txt","r") as username_finder:
                            for line in username_finder:
                                if ("username: " + username2 + " password: " + password) == line.strip():
                                    player2cred = line.strip()
                                    print("player2,you are logged in,locoked and loaded...")
                                    check_failed = False


#---------------------------------------------------
#carry = True
print("--MAIN-MENU--")
print("Please enter 'n' if you are a new user(REGISTER) or 'e' if you are a exsiting user!(LOGIN)")
ens=input("")
while ens not in ('e', 'n', 's',"L"): # if anything else but these characters are entered it will loop until it is correct
    print("Please enter 'n' if you are a new user(REGISTER) ,And 'e' if you are a exsiting user!(LOGIN)")
    ens = input()

if ens == "e":
    existing()

elif ens == "n":
    newuser()
    print("okay,lets try out the new username/passwords.(for security of course)")
    existing()


        
           
    
    

#---------------------------------------------------
print("--PLAYER-1-(logged in as")
print(player1cred)#this is mostly a tool to check that existing() was correctly performed.
time.sleep(1)
print("--PLAYER-2--(logged in as)")
print(player2cred)
#---------------------------------------------------
time.sleep(1)
print("in this game,2 players compete to roll 2 D6 each for a total of 5 rounds, different rolls on the dice give different scores...")
time.sleep(5)
def rules():
    print("--------HERE-IS-THE-SCORING-SYSTEM------")
    time.sleep(1)
    print("scoring:")
    print("★The total of the 2 dice is added to the score to begin with")
    print("★total is odd = -5 points")
    print("★total is even = +10 points")
    print("★doubles = roll one extra die and add the number of points to their score")
    print("★note that scores cannot go below 0 at any point")
    print("★If both players have the same score at the end of the 5 rounds, they each roll 1 die and whoever gets the highest score wins (this repeats until someone wins)")
    print("★as a punishment, everytime you press something that isnt 'r' when prompted.(and i guess enter duh)you will score 0 points that round!")
    print("-------------------------------------------")
    time.sleep(10)
    return
print("-------------------------------------")
print("Y = yes")
print("N = No")
print("anything else = No")
print("-------------------------------------")
rule = input("would you like to read the rules/scoring system?")

ruleup = rule.upper()
#print(ruleup)
if ruleup == "Y":
    rules() 

else:
    print("okie dokie,skippin")

    
    
player1 = input("What would player 1 prefer to be called for this game(this will appear on the leaderboard ): ")#doin this because its possible for 2 players to use the same account, this is a feature,not a flaw >:)
player2 = input("What would player 2 prefer to be called for this game(this will appear on the leaderboard ): ")
player1upper = player1.upper()
player2upper = player2.upper()
def playround():
    global total
    global player
    total1=0
    
    rollstart = input(player + " Your turn press r to roll the dice: ")
    
#all for the ASCII stuff dont worry id never be this inefficient for real rolls....     

    if rollstart == "r":
        dice1=random.randint(1,6)
        dice2=random.randint(1,6)
        time.sleep(0.5)
        print("rolling...")
        time.sleep(0.5)
        print("You rolled a " + str(dice1) + " and a " + str(dice2))
        total1 = dice1 + dice2

        if dice1 == 1:
            rdiewas1()
        if dice1 == 2:
            rdiewas2()
        if dice1 == 3:
            rdiewas3()
        if dice1 == 4:
            rdiewas4()
        if dice1 == 5:
            rdiewas5()
        if dice1 == 6:
            rdiewas6()

        if dice2 == 1:
            ediewas1()
        if dice2 == 2:
            ediewas2()
        if dice2 == 3:
            ediewas3()
        if dice2 == 4:
            ediewas4()
        if dice2 == 5:
            ediewas5()
        if dice2 == 6:
            ediewas6()

        
        
        if dice1 == dice2:
            rollstart=input("Woah doubles press r to roll another dice: ")
            if rollstart == "r":
                dice3=random.randint(1,6)
                print("You rolled a "+str(dice3))
                if dice3 == 1:
                    rdiewas1()
                if dice3 == 2:
                    rdiewas2()
                if dice3 == 3:
                   rdiewas3()
                if dice3 == 4:
                    rdiewas4()
                if dice3 == 5:
                    rdiewas5()
                if dice3 == 6:
                    rdiewas6()
                total1=dice1+dice2+dice3
                if total1 % 2 == 0:
                    total=10+total1

                    print("Thats even so you got an extra ten points")
                    print("Thats a total of " +str(total)+"\n")
                elif total1 % 2 != 0:
                    total=total1-5
                    print("Unlucky thats an odd number you lose 5 points")
                    print("thats a total score of " +str(total)+"\n")
            else:
                print("wuh oh")
        else:
            if total1 % 2 == 0:
                total=10+total1
                print("Thats even so you got an extra ten points")
                print("Thats a total of " +str(total)+"\n")
            elif total1 % 2 != 0:
                total=total1-5
                print("Unlucky thats an odd number you lose 5 points")
                print("Thats a total score of " +str(total)+"\n")
    else:
        print("Hey,Can you read? as a punishment, everytime you press something that isnt r(and i guess enter)you will score 0 points that round!because, you are a horrible human being :)")
        
def writetofile():
        with open("scores.txt", "r") as file:
            #the section of the code that deals with the text file, i couldve had a real nice lookin 2d array, but nope.
            #welp i incredibly overcomplicated this :0
            read = [0,1,2,3,4]#reading array
            resultslist = [0,0,0,0,0]
            global newresultslist
            newresultslist = [0,0,0,0,0]
            global winnername
            global playerscore#to be used anywhere in program
            d = 0         #most single letter variables are just counters
            linenum = 0
            p = 1
            q = 0
            for position, line in enumerate(file):   #adds a counter
                if position in read:
                    result = ''.join([i for i in line if i.isdigit()])  #remove digit from a string
                    result=int(result)
                    resultslist[d] += result
                    d+=1
        with open("scores.txt", "r") as file:  #opens file to read and reads data
            data = file.readlines()
        newresultslist = resultslist.copy()   #copies and sorts the result list
        newresultslist.sort()
        if int(playerscore) > newresultslist[0]:     #checks if it is viable fot the leaderboard (index 0 obviously)
            linenum = resultslist.index(newresultslist[0])
            playerscore=str(playerscore) #has to be sting,this was an annoyance to spot :/ 
            writeline=winnername + "," + playerscore + "\n"
            with open("scores.txt", "w") as file:
                data.pop(linenum)    #removes and returns last value from the list
                data.append(writeline)
                for q in range(len(data)):
                    file.write(data[q])
                    q+=1                                   

def gameround():
    global player1score
    global player2score
    global total
    global Round
    global player
    print("Round " + str(Round))
    player = player1
    playround()
    player1score=player1score+total
    if player1score < 0:
        player1score = 0
    player = player2
    playround()
    player2score=player2score+total
    if player2score < 0:
        player2score = 0
    print("so, at the end of Round ",Round,"",player1 + " has " + str(player1score) + " points and " + str(player2) + " has " + str(player2score) + " points \n")
    Round+=1

gameround()#R1
gameround()#R2
gameround()#R3
gameround()#R4
gameround()#R5
if player1score == player2score:
    print("You have the same score! Bonus Dice roll \n")
    o = 0
    p = 0
    while o == p:
        rollstart = input(player1 + " Press r to roll ")
        if rollstart == "r":
            o = random.randint(1,6)
            print(" You rolled a \n" + str(o))
        else:
            print("wuh oh")
        rollstart = input(player2 + " Press r to roll ")
        if rollstart == "r":
            p = random.randint(1,6)
            print(" You rolled a \n" + str(o))
    if o > p :
        player1score+=o
        print(player1 + " Wins with a total of \n" + str(player1score))
        winnername = player1
        playerscore=player1score
    else:
        player2score+=p
        print(player2 + " Wins with a total of \n" + str(player2score))
        winnername = player2
        playerscore=player2score
if player1score > player2score :
    print(player1 + " Wins with a total of \n" + str(player1score))
    winnername = player1
    playerscore=player1score
else:
    
    print(player2 + " Wins with a total of \n" + str(player2score))
    winnername = player2
    playerscore=player2score

try:
    writetofile()
except:
    n=1
    with open("scores.txt", "w") as file:
        for n in range (1,6):
            file.write("user,000\n")
            n+=1
    writetofile()


time.sleep(2)
if int(playerscore) > newresultslist[0]:
    print("congrats! you made it to the top 5! WOOP WOOOOOOP,you should see your score on the leaderboard!")

print("---------------------------------")
print("CONGRATULATIONS ON THE WIN!!!")
f = list(newresultslist)
#print(f)
scoreboard = [f'{str(i)}' for i in f]
#print(scoreboard)
scoreboard.sort()

yes = True
f = open("scoreboard.txt","w")#the more scoring files the merrier, this on is cleaner anyway...
f.write("-----HIGHSCORES----- \n")

for score in scoreboard:
    f.write(score + "\n")
f.close()

security = input("are you comfortable with seeing names on the leaderboard?(Y/N)(it looks nicer without)")
if security == "N":
    while yes == True:
        iterativeq = input("would you like to see the scoreboard then?")
        if iterativeq == "yes":
            yes = False
            time.sleep(1)
            print("gaining access to the scoreboard...")
            f = open("scoreboard.txt","r")
            scoreoutput = f.readlines()
            f.close()
            for score in scoreoutput:
                print(score)
                yes = True
        #print("the current record holder is "

        else:
            print("well,thanks for playing anyway :)")
            print("heres a weird python turtle loading scren i made.")
            yes = False
            time.sleep(1)
elif security == "Y":
    text_file = open("scores.txt", "r+")
    lines = text_file.readlines()


    sorted_list = sorted(lines, key=lambda x: x[1])

    print(sorted_list)
    sorted_list = str(sorted_list)

    text_file.write(sorted_list)

#--------------------------------------------------------------------logbook
playerscore = str(playerscore)


def logbook():
    e = datetime.datetime.now()
    logbookfile = open("LOGBOOK.txt","a")
    logbookfile.write("----THIS-IS-THE-LOGBOOK---- \n")
    logbookfile.write("there was a game played on the date/ time of: %s" % e)
    logbookfile.write("\nthe winner was: \n")
    logbookfile.write( winnername)
    logbookfile.write("\nthey had a score of: \n")
    logbookfile.write(playerscore)
    logbookfile.close()         



    
#--------------------------------------------------------------------        
        

logbook()
print("logbook written...")
    
time.sleep(1)#comments below to remind me how to use turtle graphics
import turtle, random# random for colour choice
screen = turtle.Screen()
turtle.hideturtle()                 
screen.setup(400,500)
turtle.pensize(10)# thick pen
turtle.colormode(255)# RGB colour format
x = 0                                
while (x < 10):
    x = x + 1                        
    r = random.randint(0,255) # choose random r
    g = random.randint(0,255)# choose random g
    b = random.randint(0,255) # choose random b
    turtle.color((r,g,b)) # new colour every loop
    turtle.circle(100) # actually draw circle

#this was made by SAMUEL PIPER don't steal pls

