# number guessing with python

## steps to build the game

- import [math](https://docs.python.org/3/library/math.html),[random](https://docs.python.org/3/library/random.html) packages
- User inputs the lower bound and upper bound of the range.
- The compiler generates a random integer between the range and store it in a variable for future references.
- used [math.log()](https://docs.python.org/3/library/math.html#math.log) method to limit the guess chances
- For repetitive guessing, a while loop will be initialized.
- If the user guessed a number which is greater than a randomly selected number, the user gets an output “Try Again! You guessed too high“
- Else If the user guessed a number which is smaller than a randomly selected number, the user gets an output “Try Again! You guessed - too small”
- And if the user guessed in a minimum number of guesses, the user gets a “Congratulations! ” Output.
- Else if the user didn’t guess the integer in the minimum number of guesses, he/she will get “Better Luck Next Time!” output.
