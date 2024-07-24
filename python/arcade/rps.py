# rock, paper, scissor game :)
# this project just created for test my knowledge.
from random import choice
def rps(player):
    player_wins = 0
    python_wins = 0
    tie_games = 0
    game_count = 0
    name = player
    def play():
        nonlocal game_count

        print(f"\nwelcome to RPS game {name} \U0001F40D")
        print("\n1 for Rock\n2 for paper\n3 for scissor\n")

        player_choice = int(input("1,2,3> "))
        random_choice = int(choice("123"))
        if type(player_choice) is not int or player_choice > 3: return True
        def win_decide(p,c):
            nonlocal player_wins
            nonlocal tie_games
            nonlocal python_wins
            # winning comination list for check the winner
            winning_comination = {
                (1,2) :"won",
                (2,1) :"won",
                (3,2) :"won",
            }
            if p == c:
                tie_games += 1 
                return "\U0001F632 Tie game!\n"
            elif (p,c) in winning_comination:
                player_wins += 1
                return f"\U0001F389 {name} you won!\n"
            else:
                python_wins +1
                return  "\U0001F40D python won!\n"
        if random_choice and player_choice: winner = win_decide(player_choice,random_choice)
        if winner:
            game_count += 1
            print(f"\n{winner}\n{name} wins {player_wins} \U0001F389\npython wins {python_wins} \U0001F40D\ndraws {tie_games} \U0001F632\nplayed game {game_count} \U0001F64C\n\ngame is over {name}, do you wanna play again?\ny for yes\nq for quite")
            play_again = str(input("Y/Q>"))
        if play_again.lower() == "y":
            play()
        else:
            return False
    return play