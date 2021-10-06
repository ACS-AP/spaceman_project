import random

letters_guessed = []
lives = 7

def load_word():
 
    f = open('words.txt', 'r')
    words_list = f.readlines()
    f.close()
    
    words_list = words_list[0].split(' ') #comment this line out if you use a words.txt file with each word on a new line
    secret_word = random.choice(words_list)
    return secret_word

def indexsOf(secret_word, letter):

    index = []
    for i in range(len(secret_word)):
        if letter == secret_word[i]:
            index.append(i)
    return index

def inWord(secret_word, guess):
    
    for letter in secret_word:
        if letter == guess:
            return True
    return False


def toString(guessedLetters):

    str = ''
    for letter in guessedLetters:
        str += letter
    return str

def spaceman(secret_word):

    gameIsOver = False
    gameIsWin = False
    incorrectGuesses = 0
    guessedLetters = []
    allGuessed = []
    for i in range(len(secret_word)):
        guessedLetters.append("_")

    while(not gameIsOver):
        print("----------------")
        guess = input("Guess a letter: ")
        if inWord(toString(allGuessed), guess):
            print(f"You already guessed: {guess}")
        elif inWord(secret_word, guess):
            indexesOfLetter = indexsOf(secret_word, guess)
            for i in indexesOfLetter:
                guessedLetters[i] = guess
            if toString(guessedLetters) == secret_word:
                gameIsOver = True
                gameIsWin = True
            print(f"Guess: {toString(guessedLetters)}\n{7 - incorrectGuesses} guesses left")
        else:
            print("Wrong Guess! Guess Again.")
            incorrectGuesses += 1
            print(f"Guess: {toString(guessedLetters)}\n{7 - incorrectGuesses} guesses left")
            if incorrectGuesses == 7:
                gameIsOver = True
        allGuessed.append(guess)

    if gameIsWin:
        print("YOU WIN!")
    else:
        print(f"GAME OVER! The Secret Word was {secret_word}.")


secret_word = load_word()
spaceman(secret_word)
