import random

letters_guessed = []
lives = 7

def load_word():
    '''
    A function that reads a text file of words and randomly selects one to use as the secret word
        from the list.

    Returns: 
           string: The secret word to be used in the spaceman guessing game
    '''
    f = open('words.txt', 'r')
    words_list = f.readlines()
    f.close()
    
    words_list = words_list[0].split(' ') #comment this line out if you use a words.txt file with each word on a new line
    secret_word = random.choice(words_list)
    return secret_word

def is_word_guessed(secret_word, letters_guessed):
    '''
    A function that checks if all the letters of the secret word have been guessed.

    Args:
        secret_word (string): the random word the user is trying to guess.
        letters_guessed (list of strings): list of letters that have been guessed so far.

    Returns: 
        bool: True only if all the letters of secret_word are in letters_guessed, False otherwise
    '''
    # TODO: Loop through the letters in the secret_word and check if a letter is not in lettersGuessed

    for letter in secret_word:
        if letter not in letters_guessed:
            return False
        
    return True

def get_guessed_word(secret_word, letters_guessed):
    '''
    A function that is used to get a string showing the letters guessed so far in the secret word and underscores for letters that have not been guessed yet.

    Args: 
        secret_word (string): the random word the user is trying to guess.
        letters_guessed (list of strings): list of letters that have been guessed so far.

    Returns: 
        string: letters and underscores.  For letters in the word that the user has guessed correctly, the string should contain the letter at the correct position.  For letters in the word that the user has not yet guessed, shown an _ (underscore) instead.
    '''

    #TODO: Loop through the letters in secret word and build a string that shows the letters that have been guessed correctly so far that are saved in letters_guessed and underscores for the letters that have not been guessed yet

    for letter in secret_word:
        if letter in letters_guessed:
            print(letter, "", end=''),
        else:
            print(' _ ', end=''),
    print('\n')


def is_guess_in_word(guess, secret_word):
    '''
    A function to check if the guessed letter is in the secret word

    Args:
        guess (string): The letter the player guessed this round
        secret_word (string): The secret word

    Returns:
        bool: True if the guess is in the secret_word, False otherwise

    '''
    #TODO: check if the letter guess is in the secret word

    global lives
    if guess in secret_word:
        print('Congrats you got a letter! Letters guessed: ', letters_guessed)
        return True
    else:
        lives -= 1
        print("Wrong choice, guess again! Letters guessed: ", letters_guessed)
        print(f"You have", lives, "guesses left")
        return False




def spaceman(secret_word):
    '''
    A function that controls the game of spaceman. Will start spaceman in the command line.

    Args:
      secret_word (string): the secret word to guess.

    '''

    missedGuesses = 0
    guesses = 0
    guessed_letters = []

    print("----------------- WELCOME TO SPACEMAN --------------------")
    print("Welcome to Spaceman. A new and epic guessing game.")
    print('')
    print("--------------------- INSTRUCTIONS -----------------------")
    print("How it works is simple. There is a word you are trying to guess.")
    print("You will be guessing letters that you think are in the secret word")
    print("If you guess a letter in the word, it will fill in the blank.")
    print("You will have 7 guess attempts to figure out the secret word of you will lose.")
    print("")
    print("------------------- LETS GET STARTED --------------------")
    print("Are you read to start the game!")
    startGame = input("Are you ready to start the game [Y/N]: ")

    if startGame.upper() == "N":
        print("Thanks for playing. Hope to see you soon.")
    if startGame.upper() == "Y":
        get_guessed_word(secret_word, guessed_letters)
        while missedGuesses < 7:
            guessesLeft = 7 - missedGuesses
            print(guessed_secret_word)
            guessed_letter = input(F'You have {guessesLeft} guesses left! Guess a letter: ')
            guessed_letters.append(guessed_letter)
            guessedCorrectly = is_guess_in_word(guessed_letter, secret_word)
            if guessedCorrectly == False:
                missedGuesses += 1
            if guessedCorrectly == True:
                missedGuesses += 0
            correctlyGuessedWord = is_word_guessed(secret_word, guessed_letters)
            if correctlyGuessedWord == True:
                print("Congrats on guessing the word")
                break
        if missedGuesses == 7:
            print("Sorry you ran out of guesses. Better luck next time!")

    #TODO: show the player information about the game according to the project spec

    #TODO: Ask the player to guess one letter per round and check that it is only one letter

    #TODO: Check if the guessed letter is in the secret or not and give the player feedback

    #TODO: show the guessed word so far

    #TODO: check if the game has been won or lost






#These function calls that will start the game
secret_word = load_word()
spaceman(secret_word)
