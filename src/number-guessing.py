# guessing number game
# import random
# import math
import random
import math

# user inputs lower bound
lower = int(input("enter lower bound: "))

# user inputs upper bound
upper = int(input("enter upper bound: "))

# choose a random number between lower and upper bound
# stored it in varible 'x'
x = random.randint(lower, upper)

print("number of guesses: ", math.log(upper-lower+1, 2))

# initlizing the number of guesses
count = 0

while count < math.log(upper-lower+1, 2):
    count += 1

    # taking guessing number as input
    guess = int(input("enter your guess: "))

    # condition testing
    if x == guess:
        print("you guessed the number in ", count," count")
        break

    elif x > guess:
        print("guess is too low")
    elif x < guess:
        print("guess is too high")

if count >= math.log(upper-lower+1, 2):
    print("you lost")
    print("the number was", x)
