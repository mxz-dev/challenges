import argparse
from games.rps import rps
from games.guess_number import gussgame
from sys import exit

parser = argparse.ArgumentParser(prog="arcade program", description="just a little game for enjoy.")
parser.add_argument("-n","--name",metavar="name",type=str,help="enter your name for better experince :)",required=True)
args = parser.parse_args()
name = args.name

def main():
    print(f"welcome to the arcade {name}")
    print("\nenter 1 for rps (rock,paper,scissor) game\nenter 2 for guess number game.\n\nor press x to exit.")
    game = input("\n1,2> ")
    if type(game) is str and game == "x":
        exit("bye!") 
    elif int(game) == 1:
        play = rps(name)
        res = play()
    elif int(game) == 2:
        play = gussgame(name)
        res = play()

    else:
        exit("[ERR], invalid err :(, check the input!")
    
    if res == True:
        exit("[ERR], invalid input!")
    elif res == False:
        print(f"Good bye {name}!")
        main()

if __name__ == "__main__":
   main()