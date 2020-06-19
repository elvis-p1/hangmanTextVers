import os
import random
import string

direc = os.getcwd()  # current working directory
files = os.listdir(direc)  # get files from the directory
print("Files in %r: %s" % (direc, files))

f = open("Hangman_Phrases.txt", "r").read().split("\n") #remove newlines

# the list of alphabet
alphabet = list(string.ascii_letters)

# for when the player chooses a category of words/phrases to play
idioms_flag = False 
#list of words/phrases under this category 
idioms = []

# for when the player chooses a category of words/phrases to play
countries_flag = False
#list of words/phrases under this category 
countries = [] 

# for when the player chooses a category of words/phrases to play
difficult_flag = False
# list of words/phrases under this category 
difficult = []

# store the phrase being played in this variable
phrase = ""
phrase_list = []

# store the phrase being played in this variable
phrase = ""
phrase_list = []

# will contain blanks to guess from
blank_phrase = ""
blank = "|_|"

# flag is true if user has won by putting in all the correct charaters
winning = False

# what will be shown to the user
show_board = []

# categories 
categories = ["Countries:", "Idioms:", "Difficult:", ""]

# a list of letter already played by a user
played_letters = []
# will remain true if the program were to reset for more games
reset = True
def restart():
    global countries,countries_flag,idioms,idioms_flag,difficult,difficult_flag,played_letters,winning,show_board,phrase,phrase_list
    # for when the player chooses a category of words/phrases to play
    idioms_flag = False 
    #list of words/phrases under this category 
    idioms = []

    # for when the player chooses a category of words/phrases to play
    countries_flag = False
    #list of words/phrases under this category 
    countries = [] 

    # for when the player chooses a category of words/phrases to play
    difficult_flag = False
    # list of words/phrases under this category 
    difficult = []

    # store the phrase being played in this variable
    phrase = ""
    phrase_list = []

    # a list of letter already played by a user
    played_letters = []

    # flag is true if user has won by putting in all the correct charaters
    winning = False

    # what will be shown to the user
    show_board = []

    # store the phrase being played in this variable
    phrase = ""
    phrase_list = []

# set the phrases/words into the category lists to be selected from
def set():
    global countries,countries_flag,idioms,idioms_flag,difficult,difficult_flag
    for line in f:
        # Append words under 'Idioms' into a list
        if "Idioms:" in line:
            idioms_flag = True
            difficult_flag = False
            countries_flag = False
        elif idioms_flag and line not in categories:
            idioms.append(line)
        # Append words under 'Countries' into a list
        if "Countries:" in line:
            countries_flag = True
            idioms_flag = False
            difficult_flag = False
        elif countries_flag and line not in categories:
            countries.append(line)
        # Append words under 'Difficult' into a list
        if "Difficult:" in line:
            difficult_flag = True
            idioms_flag = False
            countries_flag = False
        elif difficult_flag and line not in categories:
            difficult.append(line)
        else:
            continue

# set the playing phrase to something
def get_phrase():
    global phrase, phrase_list, blank_phrase, show_board
    # User input for the category they want to play from 
    user = input("Enter one of the categories: Countries , Difficult , Idioms ")
    if user.lower() == "countries":
        r = random.randint(0,len(countries)-1)
        # a phrase is randomly selected 
        phrase = countries[r]

    elif user.lower() == "difficult":
        r = random.randint(0,len(difficult)-1)
        # a phrase is randomly selected
        phrase = difficult[r]

    elif user.lower() == "idioms":
        r = random.randint(0,len(idioms)-1)
        # a phrase is randomly selected
        phrase = idioms[r]

    else:
        print("\nEnter a valid category\n")
        get_phrase()

    phrase_list = list(phrase)
    for i in range(len(phrase)):
        # check if the element is a letter
        if phrase[i].isalpha():
            # replacing each letter with a blank
            phrase_list[i] = blank
    
    # what will be shown to the user
    show_board = phrase_list

    blank_phrase = ''.join(phrase_list)

    # will be used to check if a character is in a phrase
    phrase_list = list(phrase)
    
# for the user to guess letters and play hangman
def play():
    global blank_phrase,guess_amount,show_board,winning,played_letters
    print("you have " + str(guess_amount) + " attempts")
    print(blank_phrase)
    char_in = input("Enter a character ")
    if char_in == "!p" or char_in == "!P":
        if len(played_letters) == 0:
            print("You have not guessed any letters yet")
        else:
            played_string = " ".join(played_letters)
            print("Played: "  + played_string)
    # invalid input, not a letter or more than one character
    elif not char_in.isalpha() or len(char_in) > 1:
        print(char_in + " is an invalid input")
    else:
        #if the input character is in the phrase
        if char_in.lower() in phrase_list or char_in.upper() in phrase_list:
            # Add the input to the list of played letters if not already
            if char_in.upper() not in played_letters and char_in.lower() not in played_letters:
                played_letters.append(char_in.lower())
            # Do not add it to the list if it is already in
            else:
                print("You have already guessed the letter " + char_in)
            for i in range(len(phrase_list)):
                if char_in.upper() == phrase_list[i] or char_in.lower() == phrase_list[i]:
                    show_board[i] = phrase_list[i]       
        # wrong answer
        else:
            # if it has not been played before
            if char_in.upper() not in played_letters and char_in.lower() not in played_letters:
                played_letters.append(char_in.lower())    
                print("Wrong")
                guess_amount -= 1
            else:
                print("You have already guessed the letter " + char_in)
            print("You have " + str(guess_amount) + " attempts left")

    # display which letters you have as a string
    blank_phrase = ''.join(show_board)  

    #No more blanks in the board means you have guessed all the letters and won     
    if blank not in show_board:
        winning = True
            
# setting the guess amount (difficulty)
guess_amount = 6
def set_difficulty():
    global guess_amount
    # User input on the number amount of letter guesses they want
    print("Perfect = No mistakes  \nTough = 4 wrong attempts  \nNormal = 6 wrong attempts  \nEasy = 10 Wrong Attempts")
    hard_input = input("Enter a difficulty: ")
    
    if hard_input.lower() == "perfect":
        guess_amount = 0
        print("Set to " + hard_input.lower())
    elif hard_input.lower() == "tough":
        guess_amount = 4
        print("Set to " + hard_input.lower())
    elif hard_input.lower() == "normal":
        guess_amount = 6
        print("Set to " + hard_input.lower())
    elif hard_input.lower() == "easy":
        guess_amount = 10
        print("Set to " + hard_input.lower())
    else:
        print("\nInvalid difficulty\n")
        print("PLEASE ENTER A VALID DIFFICULTY")
        set_difficulty()
# main function
def main_function():
    global guess_amount,reset
    set()
    get_phrase()
    set_difficulty()
    print("Type !p to see the letters you have played")
    while guess_amount > 0 and winning == False:
        play()

    if winning == False:
        print("The phrase/word was " + phrase)
        print("Better luck next time!")
    else:
        print("The phrase/word was " + phrase)
        print("Congratulations, you win!")

    # prompt to reset/play again
    rInput = input("Enter y/Y to play again ")
    if rInput.lower() == "y":
        reset = True
    else:
        reset = False

# main loop
while reset:
    main_function()
    restart()
    if reset:
        print("resetting..")

# exit message
print("Thank you for playing ")

# exit