"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie

author: Veronika Pindíková
email: veronika.pindikova@gmail.com
discord: Veronika77
"""
import random
import time
import csv

def print_bulls_and_cows(bulls, cows):
    bull_word = "bull" if bulls == 1 else "bulls"
    cow_word = "cow" if cows == 1 else "cows"
    print(f"{bulls} {bull_word}, {cows} {cow_word}")
def guess_numbers():
    while True:
        guessed_numbers = set()
        secret_number = str(random.randint(1000, 9999))
        print(f"Secret number: {secret_number}")
        start_time = time.time()
        attempts = 0
        print("Hi there!")
        print("-"*45)
        print("I've generated a random 4 digit number for you.\nLet's play a bulls and cows game.")
        print("-"*45)
        while True:
            guessed_number = input("Enter your guess: ")   
            if not guessed_number.isdigit():  
                print("Warning: Please enter a valid number.")
            elif len(guessed_number) != 4:
                print("Warning: The number must have exactly 4 digits.")
            elif guessed_number in guessed_numbers:
                print("You've already guessed this number.")
            elif guessed_number.startswith("0"):
                print("Warning: The number should not start with zero.")
            else:
                guessed_numbers.add(guessed_number)
                bulls, cows = 0, 0
                for i in range(4):
                    if guessed_number[i] == secret_number[i]:    
                        bulls += 1
                    elif guessed_number[i] in secret_number:                 
                        cows += 1
                print_bulls_and_cows(bulls, cows)
                attempts += 1
                if bulls == 4:
                    end_time = time.time()
                    elapsed_time = end_time - start_time      
                    if 1 <= (attempts) <= 3:
                        print(f"Congratulations! That´s amazing! You've guessed the secret number! In time: {elapsed_time:.2f} seconds.\nin {attempts} guesses!")
                    elif 4 <= (attempts) <= 10:
                        print(f"Congratulations! That´s very good! You've guessed the secret number! In time: {elapsed_time:.2f} seconds.\nin {attempts} guesses!") 
                    else:
                        print(f"Congratulations! You've guessed the secret number! In time: {elapsed_time:.2f} seconds.\nin {attempts} guesses!")
                    with open("game_stats.csv", "a", newline="") as csvfile:
                        writer = csv.writer(csvfile)
                        writer.writerow([attempts, elapsed_time])
                    with open("game_stats.csv", "r" ) as csvfile:
                        writer = csv.reader(csvfile)
                        for line in writer:
                            print(line)
                    break
        play_again = input("Do you want to play again? (y/n): ")
        if play_again.lower() != "y":
            break
guess_numbers()
