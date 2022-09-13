import random
from gladiatorClass import gladiator

# List of names that can be chosen at random for the gladiators
names = ["Agustus", "Adrianus", "Cassius", "Felix", "Flavius", 
         "Justus", "Marcus", "Maximus", "Octavius", "Titus", 
         "Romulus", "Valerius", "Brutus", "Aurelius", "Linus"]

# Array of Gladiator(obj)'s with which to run the tournament 
combatants = []

# Collects Tournament size and creates 'n' many new gladiator objects
# and appends them to the combatants list.
tSize = int(input("Size of Tournament: "))
for i in range(0, tSize):
    nameIndex = random.randint(0, (len(names) - 1))
    newGladiator = gladiator(names[nameIndex], i, 100, 5, 5)
    combatants.append(newGladiator)


def calcDmg(attacker: gladiator, defender: gladiator):
        # Calculates attackers power
        strMultiplier = random.randint(0, 20)
        atkStr = attacker.strength * strMultiplier

        # Calculates defenders power
        defMultiplier = random.randint(0, 20)
        defStr = defender.defense * defMultiplier

        # Total damage inflicted, value cannot be less than zero
        damageDone = atkStr - defStr
        if damageDone < 0:
            damageDone = 0
        
        return damageDone

# Function defines a single "turn" of combat
def fightTurn(gladiatorA: gladiator, gladiatorB: gladiator):
    # Turn one, gladiatorA attacks, B defends
    gladiatorB.health -= calcDmg(gladiatorA, gladiatorB)
    if gladiatorB.health <= 0:
        return "A"

    # Turn Two, gladiatorB attacks, A defends 
    gladiatorA.health -= calcDmg(gladiatorB, gladiatorA)
    if gladiatorA.health <= 0:
        return "B"
    else:
        return

# Function defines a single match consisting of "turns" between gladiators
def simulateRound(gladiatorA: gladiator, gladiatorB: gladiator):
    # While neither combatant is dead ...aka health > 0
    winner = None
    while True:
        returnVal = fightTurn(gladiatorA, gladiatorB)
        if returnVal == "A":
            winner = gladiatorA.name
            break
        elif returnVal == "B":
            winner = gladiatorB.name
            break
        
    return winner
            
print(simulateRound(combatants[0], combatants[1]))
        

