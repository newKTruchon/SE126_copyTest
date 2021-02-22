import csv
import random 


name = []
desc = []
powerA = []
powerD = []
level = []
records = 0

with open("midtermTest/YUGIOH.csv") as csvfile: 

    file = csv.reader(csvfile)

    for rec in file: 

        records = records + 1
        name.append(rec[0])
        desc.append(rec[1])
        powerA.append(rec[2])
        powerD.append(rec[3])
        level.append(rec[4])


#for i in range(0, records):

    #print("{0}\t{1}\t{2}\t{3}\t{4}".format(name[i], desc[i], powerA[i], powerD[i], level[i]))

#generate a random number; this will be the monster chosen 
monster = random.randint(0, 29)
warrior = random.randint(0, 29)

print("YOUR WARRIOR HAS BEEN CHOSEN!")
print("WARRIOR: {0}\nDESCRIPTION:{1}\nATTACK: {2}\t | \t DEFENSE: {3}\t | \tLEVEL:{4}".format(name[warrior], desc[warrior], powerA[warrior], powerD[warrior], level[warrior]))

print("YOUR OPPONENT HAS BEEN CHOSEN!")
print("MONSTER: {0}\nDESCRIPTION:{1}\nATTACK: {2}\t | \t DEFENSE: {3}\t | \tLEVEL:{4}".format(name[monster], desc[monster], powerA[monster], powerD[monster], level[monster]))

attack = input("Enter 'a' to attack: ")

warrior_health = powerD[warrior]
monster_health = powerD[monster]
attack_ct = 0

while attack == "a":

    attack_ct += 1

    if level[warrior] > level[monster]:

        monster_health -= powerA[warrior]

    elif level[monster] > level[warrior]:

        warrior_health -= powerA[monster]
    
    else:
        print("Even match. You walk away. ")
        attack = "n"


    print("ATTACK: {0}  MONSTER HEALTH:{1} WARRIOR HEALTH: {2}".format(attack_ct, monster_health, warrior_health))

    attack = input("Attack again? a for yes: ")