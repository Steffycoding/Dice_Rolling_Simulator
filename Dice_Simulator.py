import random
import time

def roll_dice():
    """Generate a random number between 1 and 6."""
    return random.randint(1, 6)

def main():
    """Main function to run the Dice Rolling Simulator."""
    print("Welcome to the Dice Rolling Simulator!")
    
    while True:
        input("Press Enter to roll the dice...")

        result = roll_dice()
        print(f"You rolled: {result}")

        repeat = input("Do you want to roll the dice again? (yes/no): ").lower()
        if repeat not in ['yes', 'y']:
            print("Thank you for using the Dice Rolling Simulator. Goodbye!")
            break

if __name__ == "__main__":
    main()
