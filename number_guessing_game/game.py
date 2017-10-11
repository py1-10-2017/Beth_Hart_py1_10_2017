import random


def generate_num():
    num = random.randrange(1, 101)
    return num
num = generate_num()



def play_game():
    guess = 0
    while guess != num:
        guess = input("Take a guess! ")
        if guess == num:
            print "you guessed it!"
        elif guess > num:
            print "your guess if too high try again"
        elif guess < num:
            print " your guess is too low"


print "Welcome to the Great Number Game!"
print "I am thinking of a number between 1 and 100"
play_game()


