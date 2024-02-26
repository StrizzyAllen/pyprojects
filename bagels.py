# Bagels is a deductive logic game where you must guess the secret number 
# strizzyallen @ github.com/strizzyallen

import random

NUM_DIGITS = 3 
MAX_GUESSES = 10 


def main():
    print('''Bagels, a deductive logic game. 
          
     I am thinking of a {}-digit number with no repeated digits.
     Try to guess what it is. Here are some hints:
     When I say:   That means:
     Pico          One digit is correct but in the wrong place.
     Fermi         One digit is correct and in the right place.
     Bagels        No digit is correct.

     Example, if the secret number is 248 and your guess was 843, the hint would be fermi pico'''.format(NUM_DIGITS))
    
    while True: # main game loop
        # This stores the secret number the player needs to guess:
        secretNum = getSecretNum()
        print('I have thought of a secret number.')
        print(' You have {} guesses to get it.'.format(MAX_GUESSES))

        numGuesses = 1 
        while numGuesses <= MAX_GUESSES:
            guess = ''
            # keep looping until valid guess is entered
            while len(guess) != NUM_DIGITS or not guess.isdecimal():
                print('Guess #{}: '.format(numGuesses))
                guess = input('> ')
            
            clues = getClues(guess, secretNum)
            print(clues)
            numGuesses += 1

            if guess == secretNum: 
                break # correct guess, so break out of this loop:
            if numGuesses > MAX_GUESSES:
                print('You ran out of guesses.')
                print('The answer was {}.'.format(secretNum))

        # Ask player if they want to play again
        print('Do you want to play again? (yes or no)')
        if not input('> ').lower().startswith('y'):
            break
        print('Thanks for playing!')

def getSecretNum():
    """Returns a string made up of NUM_DIGITS unique random digits."""
    numbers = list('0123456789') # Create a list of digits 0 to 9.
    random.shuffle(numbers) # shuffle them into random order.

    # Get the first NUM_DIGITS digits in the list for the secret number:
    secretNum = ''
    for i in range(NUM_DIGITS):
        secretNum += str(numbers[i])
        return secretNum
    
def getClues(guess, secretNum):
    """Returns a string with the pico, fermi bagels clues for the guess and secret number pair."""
    if guess == secretNum:
        return 'You got it!!'
    
    clues = []

    for i in range(len(guess)):
        if guess[i] == secretNum[i]:
            # A correct digit is in the correct place.
            clues.append('Fermi')
        elif guess[i] in secretNum:
            # A correct digit is in the wrong place.
            clues.append('Pico')
            if len(clues) == 0:
                return 'Bagels' # There are no correct digits
            else:
                # sort the clues into alphabetical order so their original order doesnt give information away
                clues.short()
                # make a single string form the list of string clues
                return ' '.join(clues)
            
# if the program is run (instead of imported), run the game:
if __name__ == '__main__':
    main()

    
