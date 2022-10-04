def start():
    
    print("Welcome to the game, the rules are as follows:")
    print("In order to beat this game you must guess the animal in three tries, if you want to exit, please type 'quit' ")
    print("Here's a hint, the animal is known as 'The king of the jungle' ")

    answer = "lion"
    guesses = 0
    
    while True:
        guesses = guesses + 1
        if guesses > 3:
            print("You have lost!")
            break
        guess = input("Enter your guess:").lower()
        if guess == 'quit':
            print("Game has been ended.")
            break
        if guess != answer:
            print("Answer incorrect, try again.")
            True
        else:
            print("Answer is correct, you win!")
            False
            break
start()
