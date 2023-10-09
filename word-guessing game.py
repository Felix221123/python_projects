import random 
import sys


#word guessing game with hints displayed in it, and whenever the player
#guess the game with or without the guess ,the points are caculated
def word_guessing_game():
    my_words = ['pencil', "pen", 'cat', 'head', 'bag']
    words_hint = {
        my_words[0] : 'a writing utensil with a graphite lead embedded in a wooden shaft',
        my_words[1] : 'a universal tool used for writing on paper',
        my_words[2] : 'an animal with two beautiful eyes, adorably tiny paws, sharp claws, and two perky ears which are very sensitive to sounds.',
        my_words[3] : 'is a part of the body which usually includes the ears, brain, forehead, cheeks, chin, eyes, nose, and mouth',
        my_words[4] : 'a lightweight, flexible container meant for carrying things'
    }
    random.shuffle(my_words)
    player_points = 0
    game_chances = 0
    to_continue = True
    half_points = 0.5


    while game_chances < 5 and to_continue:
        computer_choice = random.choice(my_words)
        get_lengthOfword = len(computer_choice)
        print(f'so i picked a word and the word is {get_lengthOfword} characters long..')
        print('')
        # Ask if the player wants a hint
        hint_choice = input('Do you want a hint? (Y/N): ').strip().lower()
        if hint_choice == 'y':
            # Player wants a hint
            hint_word = words_hint[computer_choice]
            print(f"Hint: {hint_word}")
            # Deduct points (cut in half)
            hint_requested = True

        elif hint_choice == 'n':
            hint_requested = False
            print('well okkk , good luck playing...')
        else:
            print('well your option was invalid..or out of range so we are continuing..🤪')


        user_guess = input('can you guess what word it was..').strip().lower()
        print('')
        if user_guess == computer_choice and hint_requested == True:
            player_points += 1 * half_points
            print('yaay you guessed right..however your points has been halved because you asked for hint..💀')
            print('')
        elif user_guess == computer_choice and hint_requested == False:
            player_points += 1
            print('yaay you guessed right..')
            print('')
        elif user_guess != computer_choice and hint_requested == True:
            player_points += 0 - half_points
            print('hahah you guessed wrong..and 0.5 has been deducted from your points because you asked for hints..PATHETIC💀')
            print('')
        elif user_guess != computer_choice and hint_requested == False:
            player_points += 0
            print('hahah you guessed wrong..')
            print('')
        else:
            print('mate your words were out of range...Exiting')
            sys.exit(0)

        print(f'your win points is {player_points:.1f}')  
        print('')  
        
        user_Playagain = input('would you like to playagain..\nEnter Y for Yes..\nEnter N for No..\n').strip().lower()
        if user_Playagain == 'y':
            game_chances += 1
            to_continue
        elif user_Playagain == 'n':
            game_chances += 1
            print(f'your win points is {player_points:.1f} out of {game_chances} games')
            to_continue = False
            sys.exit(0)

    print('')        
    print('you have reached your maximum game chances to guess the words')
    print(f'you overall score was {player_points:.1f} out of {game_chances}')

        

word_guessing_game()