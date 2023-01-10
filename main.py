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
def simulateMatch(gladiatorA: gladiator, gladiatorB: gladiator):
    # While neither combatant is dead ...aka health > 0
    winner = None
    while True:
        returnVal = fightTurn(gladiatorA, gladiatorB)
        if returnVal == "A":
            winner = gladiatorA
            break
        elif returnVal == "B":
            winner = gladiatorB
            break
        
    winner.health = 100
    return winner
            
# Function defines a full round of matches. Function returns an array of 
# "Victor" gladiator objects 
def simulateRound(combatants: list):
    victors = []

    # Appends the victors list by simulating matches in groups of two
    for i in range(0, (len(combatants) - 1), 2):
        victors.append(simulateMatch(combatants[i], combatants[i + 1]))

    return victors

# Function defines the entire tournament. simulateTournament() re-calls the
# simulateRound() function until a victor is determined.
def simulateTournament(combatants: list):
    while len(combatants) > 1:
        combatants = simulateRound(combatants)

    return combatants[0].name

print(simulateTournament(combatants))