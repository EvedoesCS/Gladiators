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

