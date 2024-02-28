## Bagles Logic Game by github.com/strizzyallen inspired by  Al Sweigarts book 'The Big Book of Small Python Projects'.
## Bagels is a deductive logic game where the user must guess the secret 3 digit number.
## The user will get 10 chances to guess correctly. There will also be hints given, for example:

## When I say:      What it means:
## Pico             One number is correct but in the wrong position
## Fermi            One number is correct and in the right position
## Bagels           No number is correct

import random

NUM_DIGITS = 3
MAX_GUESSES = 15


def main():
    print(
        """Bagels, a deductive logic game.

    I am thinking of a secret {}-digit number with no repeated digits. Try to guess what it is. Here are some clues:

    When I say:      What it means:
    Pico             One number is correct but in the wrong position
    Fermi            One number is correct and in the right position
    Bagels           No number is correct

    For example, if the secret number is 248 and your guess is 843, the clues would be Fermi Pico.""".format(
            NUM_DIGITS
        )
    )

    while True:  # main game loop
        # this stores the secret number
        secretNum = getSecretNum()
        print("I have thought up a number")
        print(" You have {} guesses to get it.".format(MAX_GUESSES))

        numGuesses = 1
        while numGuesses <= MAX_GUESSES:
            guess = ""
            # keep looping until they enter a valid guess:
            while len(guess) != NUM_DIGITS or not guess.isdecimal():
                print("Guess #{}: ".format(numGuesses))
                guess = input("> ")
            clues = getClues(guess, secretNum)
            print(clues)
            numGuesses += 1

            if guess == secretNum:
                break  # they got it correct, break out of the loop
            if numGuesses > MAX_GUESSES:
                print("You ran out of guesses")
                print("The answer was {}.".format(secretNum))
        # Ask player if they want to play again
        print("Do you want to play again? (yes or no)")
        if not input("> ").lower().startswith("y"):
            break
    print("Thanks for playing!")


def getSecretNum():
    """Returns a string made up of NUM_DIGITS unique random digits."""
    numbers = list("0123456789")  # list of digits
    letters = list("abcde") # list of letters
    random.shuffle(numbers)  # shuffle into random order

    # Get the first NUM_DIGITS digits in the list for the secret number:
    secretNum = ""
    for i in range(NUM_DIGITS):
        secretNum += str(numbers[i])
    return secretNum


def getClues(guess, secretNum):
    """Retruns a string with the hints"""
    if guess == secretNum:
        return "You got it, good Job!"
    clues = []

    for i in range(len(guess)):
        if guess[i] == secretNum[i]:
            # correct digit in the correct place
            clues.append("Fermi")
        elif guess[i] in secretNum:
            # correct digit is in the wrong place
            clues.append("Pico")
        if len(clues) == 0:
            return "Bagels"  # no correct digits
        else:
            # sort the clues into alphabetical order so their original
            # order doesn't give information away
            clues.sort()
            # make a single string from the list of string clues
            return " ".join(clues)


# if the program is run (instead of imported), run the game:
if __name__ == "__main__":
    main()
