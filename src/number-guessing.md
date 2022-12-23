This is a simple guessing game where the user inputs a lower and upper bound for the range of numbers that the computer will randomly select from. The computer will then choose a random number from within this range and the user has to guess what the number is. The computer will tell the user if their guess is too high or too low and the user has a limited number of guesses to correctly guess the number. If the user guesses correctly within the allotted number of guesses, they win the game. If they are unable to guess correctly, they lose the game.

## Here is a breakdown of the code:

- The random and math modules are imported to allow for the use of the randint function to generate a random number and the log function to calculate the number of guesses allowed.

- The user is prompted to input the lower and upper bounds for the range of numbers to be used in the game. These values are stored as lower and upper respectively.

- A random number is chosen from within the range specified by the user and stored in the variable x.

- The number of guesses allowed is calculated using the log function and the range specified by the user. This value is printed to the screen.

- A while loop is initiated and will continue until the number of guesses (stored in the count variable) reaches the number of allowed guesses calculated earlier.

- Within the loop, the user is prompted to input their guess and this value is stored in the guess variable.

- An if statement is used to compare the value of x (the randomly chosen number) to the value of guess. If they are equal, the user has guessed the correct number and the loop is exited.

- If the values are not equal, an elif statement is used to check if x is greater than guess. If it is, the user is told that their guess was too low. If x is not greater than guess, it must be less than guess, so the user is told that their guess was too high.

- If the while loop completes without the user guessing the correct number, it means that they have used up all of their allowed guesses and the game is lost. A message is printed to the screen to inform the user of this.
