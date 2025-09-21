import random
from unittest import case

while True:
    secret_number = random.randint(1, 10)
    guess = int(input("i am thinking of a number between 1 to 10. can you guess it? "))
    match guess:
        case _ if guess == secret_number:
            print("you guessed it right")
        case _:
            guess = int(input("you guessed it wrong, try again: "))
            match guess:
                case _ if guess == secret_number:
                    print("you guessed it right")
                case _:
                    print("you guessed it wrong, the number was", secret_number)
    play_again = input("want to play again? yes/no ").lower()
    if play_again != 'yes':
        print("thank you for playing") 
        break