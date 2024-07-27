from bin.calc import Calc
from sys import exit

def calculator(op,x,y):
    c = Calc(x,y)
    if op == 1:
        return c.add()
    elif op == 2:
        return c.subtract()
    elif op == 3:
        return c.multiply()
    elif op == 4:
        return round(c.division())

def run():
    try:
        print("\n Calculator \n\n 1: Add \n 2: Subtract \n 3: Multiply \n 4: Division \n 5: Exit")
        operation = int(input("\n> "))
        if type(operation) is not int or operation not in [1,2,3,4,5]:
            exit("invalid input :( ")
        if operation == 5:
            exit("bye :b")
        print("\nenter first and second number you wanna calculate like (13,88) :D")
        num = input("\nx,y> ")
        x , y = num.split(",")
        print(f"\n --------------\n result: {calculator(operation,int(x),int(y))}\n --------------")
        return run()
    except ValueError as e:
        exit("\n[ERR] please enter number as input :/")
if __name__ == "__main__":
    run()
