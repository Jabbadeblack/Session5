from random import randint
lives = int
lives = 3
while lives > 0:
    roll = randint (a: 1, b: 6)
    if roll == 6
        print("You rolled a 6! You win!")
        break
    else:
        print(f"You rolled a {roll}! You lose a life")
        lived -= 1
        print (f"Lives left: {lives}")

    if lives == 0
        print("You Lost!")
