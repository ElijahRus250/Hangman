
'''
This is assignment 5A for CISC101.
The assignment is to create a hangman game using loops and functions.
I will NOT be using the skeleton code, and I will be creating this from skratch to challenge myself.
Author: Elijah T
Student Number: <Blocked>
Date: October 23, 2024

'''

import hangmanwordbank # This is a file with ASCII art and a word bank, I did not write this file.
import random
def chooseWord():
    options = hangmanwordbank.words #List containing a lot of words
    word = random.choice(options) # Choose a word at random
    return word.upper()


def boardManager(word, currentBoard, newGuess):
    '''This function will generate the board, 
    It will fill in any guesses and _ for non guesed letters.
    
    Maintain two lists:
    ['W', 'O', 'R', 'D'] 
    ['_', '_', 'R', '_']
    - This function will use the two boards to compare and also slot in any inputed guesses
    - Function will NOT run unless the validateGuess function returned true (guess in word)
    '''

    for letterIndex in len(word): 
        if word[letterIndex] == newGuess: # Find ALL instances of the letter in the word
            currentBoard[letterIndex] = newGuess # Set them on the empty board

    return currentBoard



def validateGuess(word, guesses, guess):
    # This function does the following:
    # check if guess in word, 
    # Check if guess alr been guessed
    # check if its only one letter (no numbers)
    # Capitalize it - Make all words all capitals to ensure consitancy
    # string of all vaid letters, if not send back and ask for a user
    validLetters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    if len(guess) != 1:
        return 'LENGTH_ERROR'
    elif guess not in validLetters:
        return 'LETTER_ERROR'
    elif guess in guesses:
        return 'PREVIOUS_GUESS'
    elif guess not in word:
        return 'NOT_FOUND'
    
    elif guess in word:
        return 'FOUND'
    
    else:
        return 'ERROR'
    
def getGuess():
    """This function will get the input from the user and return it"""
    guess = input('Please enter a letter for your next guess: ')
    guess = guess.upper()
    return guess

def picturePrinter(errors, guessBoard, previousGuesses):
    """This function will use the inputs to display the visual
    of how far into the game the user is. Please see the hangmanwordbank.py file for more details
    It uses an online resource for the visuals.
    Inputs
    Errors: Total # of wrong guesses the user has at the moment
    guessBoard: A list containing blank _ spots for each letter and filled in for correct guesses
    previousGuesses: a list containing all of the users past guesses (Letter bank)"""
    print("PREVIOUS GUESSES: ", " ".join(previousGuesses))
    ascii_art = hangmanwordbank.HANGMANPICS
    print(ascii_art[errors])
    print (" ".join(guessBoard))

def generateBoards(word):
    """This function is called at the start of the game with the variable word: String, one english word
    The function generates two lists one with the full word with each letter an index in the string
    The other list is one with the length of the word with _ blank spots in each index, to be filled in"""
    masterBoard = []
    empty =[]
    for letter in word:
        # loop and add!
        masterBoard.append(letter)
        empty.append('_')
    return masterBoard, empty


def userScreen():
    # Very simple function to ensure the user has a big enough terminal window to actually use the program
    # Uses input() function to pause the program until the user hits enter
    print('|\n'*15)
    input('Please expand your terminal window so you can see all of the horizontal lines\nPress the enter key to start')

def main():
    userScreen() # Make sure the user has their terminal window big enough to see all data
    # IMPORTANT VARIABLES
    ERRORS = 0 # Max is 6
    TOTAL_GUESSES = 0
    GAME_WON = False
    WORD = chooseWord().upper()
    
    genBoards = generateBoards(WORD)
    MASTER_BOARD = genBoards[0]
    GUESS_BOARD = genBoards[1]
    previousGuesses = []
    '''
    # DEBUG STATION: - Leave commented out unless needed

    print('WORD', WORD)
    print('MASTER', MASTER_BOARD)
    print('EMPTY', GUESS_BOARD)
    '''

    while ERRORS <= 6: 
      """This is the main loop of the function,
      It will continue to loop until either the user has guessed the word correctly or max num of wrong guesses has been reached.
      There is built in break functions for both cases and will print a message a long with it.
      If for some reason they do not check, the program will only run for a MAX of 7 errors! (It will never reach this)"""
      if MASTER_BOARD == GUESS_BOARD:
        # Check to see if the user won before asking for a new guess
        print('YOU WON!\n\nGAME STATS: \n {ERRORS}/6 wrong guesses\nYou have used {TOTAL_GUESSES} total gueses')
        picturePrinter(ERRORS, GUESS_BOARD, previousGuesses) # Display the visual
        break
  # Keep playing the game if the user has not won yet.
      print('_'*20) 
      print(f'You currently have {ERRORS}/6 wrong guesses\nYou have used {TOTAL_GUESSES} total gueses')
      picturePrinter(ERRORS, GUESS_BOARD, previousGuesses) # Display the picture

      newGuess = getGuess() # Get inputs
      checkGuess = validateGuess(WORD, previousGuesses, newGuess) # Ensure its a normal guess
      print(f'\n--------------------------------\nGuess Result: ({newGuess})') 
      # All cases for the inputs
      if checkGuess == "LENGTH_ERROR" or checkGuess == "LETTER_ERROR":
          print('Your guess must be ONE character (A-Z) Er:', checkGuess)
          
      elif checkGuess == 'PREVIOUS_GUESS':
          print('You have already guessed that! Er:', checkGuess)
          
      elif checkGuess == 'NOT_FOUND': # IS a valid guess, is NOT in word
          ERRORS += 1
          TOTAL_GUESSES += 1
          previousGuesses.append(newGuess)
          print(f'\n{newGuess} is NOT in the word!')
          
      elif checkGuess == 'FOUND': # Is in the word and is a valid guess
          print(f'YAY! {newGuess} IS in the word!!')
          TOTAL_GUESSES += 1
          for x in range(len(MASTER_BOARD)):
              if MASTER_BOARD[x] == newGuess:
                  GUESS_BOARD[x] = newGuess

      else:
          print('There was an error with your Guess!')
      print('--------------------------------')

      if ERRORS == 6: # Max # of guesses
          print(f'YOU LOST! \nThe word was: {WORD}')
          break


main() # Run the program