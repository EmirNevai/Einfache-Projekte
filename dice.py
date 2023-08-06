import random

def roll_dice():
    dice_roll = random.randint(1, 6)
    return dice_roll

def main():
    print("Welcome to the Dice Rolling Simulator!")
    while True:
        roll_again = input("Press enter to roll the dice or type 'quit' to exit: ")
        
        if roll_again == "quit":
            print("Thanks for playing!")
            break
        
        else:
            dice_roll = roll_dice()
            print("You rolled a", dice_roll)

if __name__ == '__main__':
    main()
