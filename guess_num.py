import random
import sys
import time
from enum import Enum
 

def play():
  games_count = 0
  player_wins = 0
  # global player_wins

  user_name = input('please enter your name...').capitalize()

  #allows an attempt limit of 3 games
  while games_count < 3:

    print(f"{user_name} can you guess what number I'm thinking between 1 to 3..")

    computer_choice = int(random.choice('123'))


    user_input = input('enter your number...')
    convert_input = int(user_input)

    #delays it by a second
    time.sleep(1)
    print(' ') 

    if convert_input == computer_choice:
        player_wins += 1
        print(f'yayay congratulations {user_name}, you guessed right ')
        ply_guess_percent = format((convert_input / computer_choice), '.2%')
        print('Your guess percentage was ', ply_guess_percent)
    else:
        ply_guess_percent = format((computer_choice / convert_input), '.2%')
        print(f'Ahh you missed : ) {user_name}, heheheheheh\nI was thinking about the number ' , computer_choice)
        print('Your guess percentage was ', ply_guess_percent)

    

    print('Your number of wins from the game is ' , player_wins)

    print(' ') 
    games_count += 1

    #ask the user whether they would like to play again
    user_playagain = input('Would you like to play again\nY for Yes\nN for No\nenter either y or n...')
    user_playagain.lower
    print(' ')
    if (user_playagain == 'y'):
        print('your games count is ', games_count)
        print(' ') 
    elif((user_playagain == 'n')):
        sys.exit('bye bye , see you next time')

  print(' ')      
  print(f'You have reached the maximum number of attempts. Your final win count is {player_wins} \n👋        😁         👍 \nThanks for playing {user_name}')

play()

