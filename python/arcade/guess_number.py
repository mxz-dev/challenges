# project: guess number game
# this project just a small challenge for my programming knowledge.

from random import choice
from sys import exit



def calc_win_percentage(fn,sn):
    # this is special win percentage calculator!
    # We have two different formulas because sometimes division leads to bugs like this: 2/1 * 100 = 200% or 3/1 * 100 = 300%, and this is a problem. So we changed the position of the some numbers!
    f1 = (fn / sn) * 100 # first formula
    f2 = (sn / fn) * 100 # second formula
    if fn == 1:
        return f1
    elif fn == 2 and sn == 3:
        return f1
    else:
        return f2

def gussgame(person):
    # local veriables
    game_count = 0
    winning_percentage = 0.0
    player_wins = 0
    python_wins = 0
    name = person
    # nested defined function
    def play_game():
        nonlocal game_count
        print(f"\n\nWelcome to Guess Number Game\U0001F47E.\nI'm thinking of one of the three numbers (1, 2, 3)! {name}, can you guess which one i'm thinking of?... \U0001F914\n")
        player_choice = int(input("1,2,3> "))
        random_num = choice("123")
        num = int(random_num)
        if type(player_choice) is not int or player_choice > 3:
            return True
        def winning_decide(p,n): # p parameter for player choice and n parameter for number generated randomly.
            nonlocal winning_percentage
            nonlocal player_wins
            nonlocal python_wins
            winning_percentage = calc_win_percentage(p,n)
            if winning_percentage >= 50.1:
                player_wins += 1 
                return f"{name} is win \U0001F973\n"
            elif winning_percentage == 50:
                python_wins += 1
                return f"Very close {name} \U0001F632\n"
            else:
                python_wins += 1
                return f"{name} is lose \U0001F4A9\n"
        game_result = winning_decide(player_choice,num)
        if game_result:
            game_count += 1
            print(f"python choose: {num}\U0001F40D\n{game_result}\nyou'r winning percentage {round(winning_percentage)}%\n{name} won: {player_wins}\U0001F9D1\npython won: {python_wins}\U0001F40D\nplayed game: {game_count}\n\ngame is over {name}! do you wanna play again?\U0001F917	 \ny for yes\nq for quite.")
            play_again = str(input("Y/Q> "))
            if play_again.lower() == "y":
                play_game() # recursive function
            else:
                return False
    return play_game
