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
    "What is the name of Mario's twin brother? "
    ]

# Answers - correspond to each question
answers = ["Tetris", "Picade", "Python", "Sega", "Luigi"]

while True:
    print ("Welcome to the computer game quiz")

    # Score starts at 0 - add one for each correct answer 
    score = 0

    for i in range (0,len(questions)):
        if (ask_question (questions[i], answers[i]) == True):
            score += 1

    print ("You scored {} points\n".format(score))
