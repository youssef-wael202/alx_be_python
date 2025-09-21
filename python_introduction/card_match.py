import random
while True:
    secret_number = random.randint(1,10)
    guess = int(input("guess the number between 1 to 10: "))
    print (secret_number)
    match guess:
        case _ if guess == secret_number:
                print("you guessed it right")
        case _ if guess > secret_number:
                print("your guess is high")
        case _:
                print("your guess is low")
    play_again = input("do you want to play again? (yes/no): ").lower()
    if play_again != 'yes':
        print("thank you for playing")
        break