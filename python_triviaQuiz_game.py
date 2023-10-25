#this is a trivia game in python for questions in python programming language 
#And it stores the users name information is a json file along with their score

import sys
import json
import re
import time
from enum import Enum


trivia_data = [
    {
        "question": "What is Python?",
        "answers": ["A programming language", "A reptile", "A type of software", "A planet"],
        "correct": "A programming language"
    },
    {
        "question": "Which Python statement is used to catch and handle exceptions?",
        "answers": ["try-except", "if-else", "for-while", "switch-case"],
        "correct": "try-except"
    },
    {
        "question": "What is the purpose of 'finally' block in exception handling?",
        "answers": ["To raise an exception", "To specify the type of exception", "To execute code whether an exception is raised or not", "To stop the program"],
        "correct": "To execute code whether an exception is raised or not"
    },
    {
        "question": "How can you open a file in Python for reading?",
        "answers": ["open('file.txt', 'w')", "open('file.txt', 'r')", "read('file.txt')", "file.open('file.txt', 'r')"],
        "correct": "open('file.txt', 'r')"
    },
    {
        "question": "What is the purpose of the 'with' statement when working with files?",
        "answers": ["To create a new file", "To write to a file", "To ensure proper file closure and cleanup", "To check if a file exists"],
        "correct": "To ensure proper file closure and cleanup"
    },
    {
        "question": "What is the Python keyword for defining a custom exception?",
        "answers": ["raise", "except", "custom", "exception"],
        "correct": "raise"
    },
    {
        "question": "Which of the following is not a built-in Python exception?",
        "answers": ["ValueError", "IOException", "TypeError", "NameError"],
        "correct": "IOException"
    },
    {
        "question": "In Python, which statement is used to raise an exception manually?",
        "answers": ["raise", "try-except", "throw", "exception"],
        "correct": "raise"
    },
    {
        "question": "What does the 'os.path.exists' function do in Python?",
        "answers": ["Check if a file exists", "Create a file", "Open a file", "Read a file"],
        "correct": "Check if a file exists"
    },
    {
        "question": "Which Python module is used to work with regular expressions?",
        "answers": ["re", "regex", "regexp", "string"],
        "correct": "re"
    }
]

player_info_list = []

def players_information():
    global player_info_list
    is_valid = True
    #players name and we store them in json file
    #Load existing contacts from the JSON file (if it exists)
    try:
        with open('playerInfo.json', 'r') as json_file:
            player_info_list = json.load(json_file)
    except FileNotFoundError:
        player_info_list = []

    #user_name = input('Hello player....Welcome...enter you name...').capitalize()

    while is_valid:
        user_name = input('Hello player....Welcome...enter you name...').capitalize()
        if not user_name.strip():
            print('please enter a valid nickname...')
            is_valid = True
        else:
            # Check if the entered username already exists
            if any(player['Player Username'] == user_name for player in player_info_list):
                print('This username already exists. Please enter a new one.')
                is_valid = True
            else:
                print('Your username is valid and it has been saved')
                break

    while is_valid:
        user_email = input('Now enter your email address...')
        regex = '([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Za-z]{2,})+'
        if re.match(regex , user_email):
            print('email is valid and it has been successsfully saved')
            break
        else:
            print('email address is invlaid....try again please..')
            is_valid = True

    player_info = {
        'Player Username' : user_name,
        'Player Email Address' : user_email
    }
    player_info_list.append(player_info)
    with open('playerInfo.json', 'w') as json_file:
        json.dump(player_info_list , json_file)
    

def play_again():
    play_again = input('would you like to play again (y | n)...').lower()
    if play_again == 'y':
        return 'y'
    elif play_again == 'n':
        return 'n'
    else:
        print('invalid..response..Exiting..')
        sys.exit(0)


def play_trivia_game():
    class AnswerChoice(Enum):
        A = 0
        B = 1
        C = 2
        D = 3


    players_information()
    #Load existing contacts from the JSON file (if it exists)
    try:
        with open('playerInfo.json', 'r') as json_file:
            player_info_list = json.load(json_file)
    except FileNotFoundError:
        player_info_list = []
    
    player_score = 0
    #this code gets the users name
    last_player = player_info_list[-1]
    player_name = last_player["Player Username"].capitalize()

    print('')
    print(f'******** Hello {player_name} ******** ')
    print(f'******** WELCOME TO THE TRIVIA GAME ******** ')
    print('You are going to answer 10 question from python programming language \nAnd your scores will declared afterwards')
    print(f'ARE YOU READY...... in..')

    # Countdown from 3 seconds
    for i in range(5, 0, -1):
        print(i)
        time.sleep(1)

    print("GO!")
    print('')
    print(f'Answer the question by choosing either A or B or C or D')
    # here are the questions to the trivia questions
    for multiple_choice in range(0, len(trivia_data)):
        player_question = trivia_data[multiple_choice]['question']
        print(player_question)
        # Create a dictionary to map user input to answer choices
        answer_choices = {
            'A': trivia_data[multiple_choice]["answers"][0],
            'B': trivia_data[multiple_choice]["answers"][1],
            'C': trivia_data[multiple_choice]["answers"][2],
            'D': trivia_data[multiple_choice]["answers"][3],
        }
        print(f'A : {trivia_data[multiple_choice]["answers"][AnswerChoice.A.value]} \nB : {trivia_data[multiple_choice]["answers"][AnswerChoice.B.value]}  \nC : {trivia_data[multiple_choice]["answers"][AnswerChoice.C.value]} \nD : {trivia_data[multiple_choice]["answers"][AnswerChoice.D.value]}')
        print('')

        is_valid = True
        while is_valid:
            player_answer = input('enter your answer(A\B\C\D)..').upper()


            if player_answer in answer_choices:
                player_answer = answer_choices[player_answer]
            else:
                print('Invalid input. Please enter A, B, C, or D.')
                continue

            if player_answer == trivia_data[multiple_choice]["correct"]:
                player_score += 1
                print('yayaya you got the answer right..one points for you 🙂')
                print('')
                is_valid = False
            elif player_answer != trivia_data[multiple_choice]["correct"]:
                player_score += 0
                print(f'sorry but the right answer was {trivia_data[multiple_choice]["correct"]}, no points gained this time...🥲')
                print('')
                is_valid = False
            else:
                print('your answer was invalid, please try again....💀')
                print('')
                is_valid = True

    last_player['Player Score'] = player_score

    # Save the updated player_info_list to the file
    with open('playerInfo.json', 'w') as json_file:
        json.dump(player_info_list, json_file)


    if player_score > 5 and player_score < 10:
        print(f'you did well {player_name}, at least you got more than half the marks...BE PROUD😊')
        time.sleep(2)
        print(f'your overall score from the game was {player_score} / 10 ')
    elif player_score <= 5:
        print(f'well your results was okk {player_name} ,but i know you could do better....NEXT TIME get your gears up😏')
        time.sleep(2)
        print(f'your overall score from the game was {player_score} / 10 ')
    elif player_score == 10:
        print(f'OHHH WOWWW, never thought you were this smart {player_name}, you are amazing....YOU\'VE MADE ME PROUD..🥰')
        time.sleep(2)
        print(f'your overall score from the game was {player_score} / 10 ')

    print('')

    player_play_request = play_again()
    if player_play_request == 'y':
        play_trivia_game()
    elif player_play_request == 'n':
        print('thanks for playing TRIVIA CHALLENGE...see ya next time 👋')
 


if __name__ == '__main__':
    play_trivia_game()
        



