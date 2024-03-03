#hangman game

word = "start"                                  #word that is being guessed
tempListWord = list(word)                       #list of every letter in the word that will be replaced with blanks as going on
length = len(word)                              # word length
counter = 0

def blankMaker(counter,length):
    blanks=""
    while (counter<length):                         #creates a blank word the same length as word
        blanks += "_"
        counter +=1
    print(blanks)
    return blanks
blanks = blankMaker(counter,length)    
tempListBlanks = list(blanks)                       #list of all blanks that will be replaced with letters
def game(blanks,word,templistWord):
    guessNum=0
    while(blanks != word and guessNum != 9):            #atm takes guesses until word is completed
        guess = input("Enter a letter: ")               #user input(Will be button presses later)
        counter=0
        guessNum+=1                                     #increases guess number, could be used to update what image is showing
        for x in (tempListWord):                        #checks every letter in the word
            if (x == guess):                            #checks if the current letter in the word is equal to the guess
                tempListWord.pop(counter)               #takes out the current letter in the index
                tempListWord.insert(counter, "_")       #inserts a blank
                tempListBlanks.pop(counter)             #takes out the blank at this position
                tempListBlanks.insert(counter, guess)   #places in the letter
                blanks = "".join(tempListBlanks)        #joins the blank list together
            counter+=1                                  #accounts for if the word has the same letter multiple times
        print(blanks)
game(tempListBlanks,word,tempListWord)        
    



