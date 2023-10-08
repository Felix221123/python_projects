# # Rock beats Scissors: Rock wins by smashing scissors.
# # Scissors beats Paper: Scissors win by cutting paper.
# # Paper beats Rock: Paper wins by covering rock.
# # Game Flow:

# # Both players choose one of the three options: Rock, Paper, or Scissors.
# # The winner is determined based on the rules mentioned above.
# # If both players choose the same item, the game is a tie, and it can be played again.

#this rock paper scissors uses argparse in the cmd line interface

import sys
import random
import time
from enum import Enum



def rps(name):
    capitalized_name = name.capitalize()
    

    game_count = 0
    player_wins = 0
    laptop_wins = 0
    games_limit = 4

    while games_limit:

        def playrockpaperscissor():

            nonlocal games_limit

            

            class games_rules(Enum):
                scissor = 1
                rock = 2
                paper = 3


            #we access the global variables in the first function
            nonlocal player_wins
            nonlocal laptop_wins
            nonlocal game_count
            nonlocal name
            nonlocal capitalized_name

            playagain = True

            while playagain:

                print("please enter a value")
                print(' ')

                print(f"{capitalized_name} , enter....\n1 for rock\n2 for scissor\n3 for paper ")


                is_valid = True

                while is_valid:
                    print(' ')
                    player_1 = input(f"{capitalized_name} enter any number...")
                    player_1Intvalue = int(player_1)
                    if (player_1Intvalue > 0 and player_1Intvalue <= 3):
                        is_valid = False
                        break
                    else:
                        is_valid = True
                        print(' ')
                        print(f"{capitalized_name} , please enter another number as the previous one\nis outside range... ")
                        return playrockpaperscissor()


                #it choses number between the ranges of 123
                pc_choice = random.choice("123")
                computer = int(pc_choice)

                print("")
                print(f"{capitalized_name}, you chose " + str(games_rules(player_1Intvalue)).replace("games_rules.",""))

                #Introduce a delay of 2 seconds
                time.sleep(2)


                print("The laptop chose " + str(games_rules(computer)).replace("games_rules.",""))
                print("")
                
                time.sleep(1)



                def whoIsTheWinner(player, computer):
                    #we can also access our global variables here in other to get the wins
                    nonlocal player_wins
                    nonlocal laptop_wins
                    nonlocal capitalized_name
                    nonlocal name

                    if player == 1 and computer == 2 :
                        player_wins += 1
                        return f"🏆 {capitalized_name} wins!"
                    elif player == 2 and computer == 1:
                        player_wins += 1
                        return f"🏆 {capitalized_name} wins!"
                    elif player == 3 and computer == 2:
                        player_wins += 1
                        return f"🏆 {capitalized_name} wins!"
                    elif player == computer:
                        return "💀 its a tie!"
                    else:
                        laptop_wins += 1
                        return f"🖥️ Laptop wins!\nSorry {capitalized_name}....😢"
                    

                game_results = whoIsTheWinner(player_1Intvalue, computer)    
                
                print(" ")
                print(game_results)

                
                game_count += 1

                print(" ")
                print('\nYour game count is ' + str(game_count))

                print(f'{capitalized_name}, your win streak is ' , player_wins)
                print('\nLaptop win streak is ' , laptop_wins)

                playagain = input(f"\n{capitalized_name} , would you like to play again...?\nY for Yes\nN for No\n....").lower()
                if (playagain == "y"):
                    print(' ')
                elif playagain == "n":
                    print(f'bye bye {capitalized_name},see you next time 👋😘')
                    break
                else:
                    print(f'bye bye {capitalized_name},see you next time 👋😘')
                    break

        return playrockpaperscissor()  
    
    print('You have reached your maximum limit which is ', games_limit)  
            

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        prog='Rock Paper Scissor',
        description='display\'s the name of a person',
        epilog='Text at the bottom for help'
    )

    parser.add_argument(
        '-n','--name', metavar='name',
        required=True , help='displays the persons name'
    )

    args = parser.parse_args()

    play = rps(args.name)
    play(args.name)

