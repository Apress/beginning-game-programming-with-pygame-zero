# Simple quiz game

# Score starts at 0 - add one for each correct answer 
score = 0

# List of questions
questions = [
    "What Russian tile matching game was popular in the 1980s? ",
    "What is the name of the Raspberry Pi arcade machine from Pimoroni? ",
    "What programming language has a logo featuring two snakes? ",
    "Which company created Sonic The Hedgehog? ",
    "What is the name of Mario's twin brother? "
    ]

# Answers - correspond to each question
answers = ["Tetris", "Picade", "Python", "Sega", "Luigi"]

print ("Welcome to the computer game quiz")

# Ask the first questions, store response in player_guess
player_guess = input (questions[0])
if (player_guess.lower() == answers[0].lower()):
    # If correct say so and add 1 point
    print ("Correct")
    score += 1
else:
    print ("Incorrect")
    
# Ask the second question
player_guess = input (questions[1])
if (player_guess.lower() == answers[1].lower()):
    # If correct say so and add 1 point
    print ("Correct")
    score += 1
else:
    print ("Incorrect")

# Ask the third questions
player_guess = input (questions[2])
if (player_guess.lower() == answers[2].lower()):
    # If correct say so and add 1 point
    print ("Correct")
    score += 1
else:
    print ("Incorrect")

print ("You scored {} points".format(score))