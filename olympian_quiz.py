"""
Name: olympian_quiz.py 
Author: Andrew peterson
Created: 09/11/2024
Purpose: A fun little quiz about anceint greece
"""
# declare intial variables
total = 0

# print intro
print("+--------------------------------------------+")
print("|        Welcome to the Olypian Quiz         |")
print("+--------------------------------------------+")

# print first question
print("Question 1: Who was the king of the gods in Greek mythology?")
answer = str(input("Is it A )Zeus, B)Poseidon, C)Hades, or D)Apollo: "))
if answer == "a":
    total += 1
    print("Correct")
else:
    print("Incorrect")

# print second question
print("Question 2: Which hero slew the monstrous Gorgon Medusa?")
answer = str(input("Is it A )Theseus, B)Perseus, C)Odysseus, or D)Hercules: "))
if answer == "b":
    total += 1
    print("Correct")
else:
    print("Incorrect")

# print third question
print("Question 3: What river did souls have to cross to reach the Underworld?")
answer = str(input("Is it A )Cocytus, B)Lethe, C)Acheron, or D)Styx: "))
if answer == "d":
    total += 1
    print("Correct")
else:
    print("Incorrect")

# print fourth question
print("Question 4: Which goddess is associated with wisdom, warfare strategy, and handicrafts?")
answer = str(input("Is it A )Aphrodite, B)Athena, C)Demeter, or D)Hera: "))
if answer == "b":
    total += 1
    print("Correct")
else:
    print("Incorrect")

# print fifth question
print("Question 5: Who was cursed to turn everything they touched into gold?")
answer = str(input("Is it A )Icarus, B)Daedalus, C)King Midas, or D)Narcissus: "))
if answer == "c":
    total += 1
    print("Correct")
else:
    print("Incorrect")

# print sixth question
print("Question 6: Which mythical creature guarded the entrance to the Labyrinth?")
answer = str(input("Is it A )Minotaur, B)Sphinix, C)Chimera, or D)Harpy: "))
if answer == "a":
    total += 1
    print("Correct")
else:
    print("Incorrect")

# print seventh question
print("Question 7: Who was the goddess of love and beauty?")
answer = str(input("Is it A )Nike, B)Artemis, C)Persephone, or D)Aphrodite: "))
if answer == "d":
    total += 1
    print("Correct")
else:
    print("Incorrect")

# print eighth question
print("Question 8: Which titan was punished by having to hold up the sky for eternity?")
answer = str(input("Is it A )Prometheus, B)Atlas, C)Cronus, or D)Hyperion: "))
if answer == "b":
    total += 1
    print("Correct")
else:
    print("Incorrect")

# print ninth question
print("Question 9: What hero completed the Twelve Labors as penance for killing his family in a fit of madness?")
answer = str(input("Is it A )Hercules, B)Jason, C)Achilles, or D)Perseus: "))
if answer == "a":
    total += 1
    print("Correct")
else:
    print("Incorrect")

# print tenth question
print("Question 10: Which enchanting nymph lured sailors to their doom with her mesmerizing voice?")
answer = str(input("Is it A )Circe, B)Calypso, C)Sirens, or D)Echo: "))
if answer == "c":
    total += 1
    print("Correct")
else:
    print("Incorrect")

print(f"{total} out of 10")
