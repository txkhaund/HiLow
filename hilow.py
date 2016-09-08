import random
import sys

game = True
x = random.randint(0,100)
while game:
    guess = int(raw_input("Guess the number:"))

    if guess > x:
        print "Your guess is too high"
        ans = raw_input("Do you want to continue? (y/n)")
        if ans == 'y' or ans == 'Y':
            continue
        elif ans == 'n' or ans == 'N':
            sys.exit()
    if guess < x:
        print "Your guess is too low"
        ans = raw_input("Do you want to continue? (y/n)")
        if ans == 'y' or ans == 'Y':
            continue
        elif ans == 'n' or ans == "N":
            sys.exit()
    if guess == x:
        print "Congratulations!"
        game = False
        sys.exit()
