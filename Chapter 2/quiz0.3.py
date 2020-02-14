import random

# Simple quiz game
def ask_question (question, answer):
    player_guess = input(question)
    if (player_guess.lower() == answer.lower()):
        print ("Correct")
        return 1
    else:
        print ("Incorrect")
        return 0

# List of questions
questions = [
    "What Russian tile matching game was popular in the 1980s? ",
    "What is the name of the Raspberry Pi arcade machine from Pimoroni? ",
    "What programming language has a logo featuring two snakes? ",
    "Which company created Sonic The Hedgehog? ",
    "What is the name of Mario's twin brother? ",
    "What is the name of the company that makes the Playstation? ",
    "What is the name of the block based game crated by Mojang? "
    ]

# Answers - correspond to each question
answers = ["Tetris", "Picade", "Python", "Sega", "Luigi", "Sony", "Minecraft" ]

while True:
    print ("Welcome to the computer game quiz")

    # Score starts at 0 - add one for each correct answer 
    score = 0

    for i in range (0,3):
        question_num = random.randint(0,len(questions)-1)
        if (ask_question (questions[question_num], answers[question_num]) == True):
            score += 1

    if (score < 1):
        print ("You did not score any points\n")
    elif (score < 3):
        print ("You scored {} points\n".format(score))
    else:
        print ("Top score\nWell done\n")
