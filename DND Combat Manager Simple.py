import tkinter as tk
from tkinter import Entry

class PlayerCharacter():
    def __init__(self,name,maxhp,hp,ac,initiative):
        self.name = name
        self.maxhp = maxhp
        self.hp = hp
        self.ac = ac
        self.initiative = initiative

    def __str__(self):
        return f"{self.name} ({self.hp}/{self.maxhp}) HP, ({self.ac}) AC"

    def damage(self, amount):
        self.hp -= amount
        if self.hp < 0:
            self.hp = 0

    def heal(self, amount):
        self.hp += amount
        if self.hp > self.maxhp:
            self.hp = self.maxhp

p1 = PlayerCharacter("Thokk Himbostein",27,27,14,0)
p2 = PlayerCharacter("MTF--1218",41,41,18,0)
p3 = PlayerCharacter("Pellit Cliff",39,39,12,0)
p4 = PlayerCharacter("Splendis Praeconem",31,31,17,0)

e1 = PlayerCharacter("Goblin",20,20,11,0)

command = "None"
amount = 0
targets = [p1,p2,p3,p4]
clock = 0

def locate(user,targets):
    for target in targets:
        if user in target.name.lower():
            return target
    return None

def process(command, user, amount):
    player=locate(user,targets)
    if player!=None:
        if command in ["heal","h"]:
            PlayerCharacter.heal(player, amount)
        elif command in ["damage","d"]:
            PlayerCharacter.damage(player, amount)
        elif command == "None":
            pass
        else:
            print("Invalid input. Check for spelling mistakes.")
    else:
        print("Character not found. Check for spelling mistakes.")

def initiative():
    ROLLER = input("Who's the initative for? ")
    roller = ROLLER.lower()
    player_in = locate(roller,targets)
    if player_in!=None:
        rolled = int(input(print("What is ",player_in.name,"'s initiative roll?")))
        player_in.initiative = rolled
    else:
        print("Character not found. Check for spelling mistakes")

def main(targets,clock):
    try:
        while True:
            while clock < 1:
                for PlayerCharacter in targets:
                    initiative()
                clock =+ 1
            targets.sort(key = lambda x: x.initiative, reverse=True)
            for PlayerCharacter in targets:
                print(str(PlayerCharacter))
            comm = input("Heal, Damage, or Initiative? (h,d,i)\n")
            command = comm.lower()
            if command in ["heal","h","damage","d"]:   
                user = input("To whom?\n").strip().lower()
                amount = int(input("How much?\n"))
                process(command,user,amount)
            elif command in ["initiative","i"]:
                initiative()
            else:
                print("Invalid input. Check for spelling mistakes.\n")
    except KeyboardInterrupt:
        pass

main(targets,clock)