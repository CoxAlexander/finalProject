#Alexander Cox
#tkinter display window

import tkinter as tk            # import the gui
import random
from tkinter.ttk import Label
from tkinter import font
import os

def buttons(window,word):            #list of every button, sending the letter corresponding to the button and the button name to be
    buttonHeight = 2
    buttonWidth=2
    
    aBtn = tk.Button(window,height=buttonHeight, width=buttonWidth, text="a", command=lambda: guess(aBtn,"a",word,window))
    aBtn.grid(row = 1, column = 1, pady = 2)
    bBtn = tk.Button(window,height=buttonHeight, width=buttonWidth, text="b", command=lambda: guess(bBtn,"b",word,window))
    bBtn.grid(row = 1, column = 2, pady = 2)
    cBtn = tk.Button(window,height=buttonHeight, width=buttonWidth, text="c", command=lambda: guess(cBtn,"c",word,window))
    cBtn.grid(row = 1, column = 3, pady = 2)
    dBtn = tk.Button(window,height=buttonHeight, width=buttonWidth, text="d", command=lambda: guess(dBtn,"d",word,window))
    dBtn.grid(row = 1, column = 4, pady = 2)
    eBtn = tk.Button(window,height=buttonHeight, width=buttonWidth, text="e", command=lambda: guess(eBtn,"e",word,window))
    eBtn.grid(row = 1, column = 5, pady = 2)
    fBtn = tk.Button(window,height=buttonHeight, width=buttonWidth, text="f", command=lambda: guess(fBtn,"f",word,window))
    fBtn.grid(row = 1, column = 6, pady = 2)
    gBtn = tk.Button(window,height=buttonHeight, width=buttonWidth, text="g", command=lambda: guess(gBtn,"g",word,window))
    gBtn.grid(row = 1, column = 7, pady = 2)
    hBtn = tk.Button(window,height=buttonHeight, width=buttonWidth, text="h", command=lambda: guess(hBtn,"h",word,window))
    hBtn.grid(row = 1, column = 8, pady = 2)
    iBtn = tk.Button(window,height=buttonHeight, width=buttonWidth, text="i", command=lambda: guess(iBtn,"i",word,window))
    iBtn.grid(row = 1, column = 9, pady = 2)
    jBtn = tk.Button(window,height=buttonHeight, width=buttonWidth, text="j", command=lambda: guess(jBtn,"j",word,window))
    jBtn.grid(row = 1, column = 10, pady = 2)
    kBtn = tk.Button(window,height=buttonHeight, width=buttonWidth, text="k", command=lambda: guess(kBtn,"k",word,window))
    kBtn.grid(row = 1, column = 11, pady = 2)
    lBtn = tk.Button(window,height=buttonHeight, width=buttonWidth, text="l", command=lambda: guess(lBtn,"l",word,window))
    lBtn.grid(row = 1, column = 12, pady = 2)
    mBtn = tk.Button(window,height=buttonHeight, width=buttonWidth, text="m", command=lambda: guess(mBtn,"m",word,window))
    mBtn.grid(row = 1, column = 13, pady = 2)
    nBtn = tk.Button(window,height=buttonHeight, width=buttonWidth, text="n", command=lambda: guess(nBtn,"n",word,window))
    nBtn.grid(row = 2, column = 1, pady = 2)
    oBtn = tk.Button(window,height=buttonHeight, width=buttonWidth, text="o", command=lambda: guess(oBtn,"o",word,window))
    oBtn.grid(row = 2, column = 2, pady = 2)
    pBtn = tk.Button(window,height=buttonHeight, width=buttonWidth, text="p", command=lambda: guess(pBtn,"p",word,window))
    pBtn.grid(row = 2, column = 3, pady = 2)
    qBtn = tk.Button(window,height=buttonHeight, width=buttonWidth, text="q", command=lambda: guess(qBtn,"q",word,window))
    qBtn.grid(row = 2, column = 4, pady = 2)
    rBtn = tk.Button(window,height=buttonHeight, width=buttonWidth, text="r", command=lambda: guess(rBtn,"r",word,window))
    rBtn.grid(row = 2, column = 5, pady = 2)
    sBtn = tk.Button(window,height=buttonHeight, width=buttonWidth, text="s", command=lambda: guess(sBtn,"s",word,window))
    sBtn.grid(row = 2, column = 6, pady = 2)
    tBtn = tk.Button(window,height=buttonHeight, width=buttonWidth, text="t", command=lambda: guess(tBtn,"t",word,window))
    tBtn.grid(row = 2, column = 7, pady = 2)
    uBtn = tk.Button(window,height=buttonHeight, width=buttonWidth, text="u", command=lambda: guess(uBtn,"u",word,window))
    uBtn.grid(row = 2, column = 8, pady = 2)
    vBtn = tk.Button(window,height=buttonHeight, width=buttonWidth, text="v", command=lambda: guess(vBtn,"v",word,window))
    vBtn.grid(row = 2, column = 9, pady = 2)
    wBtn = tk.Button(window,height=buttonHeight, width=buttonWidth, text="w", command=lambda: guess(wBtn,"w",word,window))
    wBtn.grid(row = 2, column = 10, pady = 2)
    xBtn = tk.Button(window,height=buttonHeight, width=buttonWidth, text="x", command=lambda: guess(xBtn,"x",word,window))
    xBtn.grid(row = 2, column = 11, pady = 2)
    yBtn = tk.Button(window,height=buttonHeight, width=buttonWidth, text="y", command=lambda: guess(yBtn,"y",word,window))
    yBtn.grid(row = 2, column = 12, pady = 2)
    zBtn = tk.Button(window,height=buttonHeight, width=buttonWidth, text="z", command=lambda: guess(zBtn,"z",word,window))
    zBtn.grid(row = 2, column = 13, pady = 2)
    nothing = Label(window,text="")
    nothing.grid(row=3,column=0,pady=50)
   
    
    



def main():
    window=tk.Tk() #creates window
    window.title("Hangman game") #changes the title of the window
   
    
    word=word_generator()   #generates a word
    length=len(word)        #shows length of generated word
    global wrongnum         #globally updates how many wrong answers have happened
    wrongnum=0              
    
    global blanks           #makes the blanks global
    blanks=blankMaker(length)   #generates the blanks

    print(word)                 #prints what the word is for ease of testing 
    
    buttons(window,word)        #displays buttons
    hangmanImg = tk.PhotoImage(file='final project/images/hangman.png')
    hangman=Label(window, image=hangmanImg)
    hangman.grid(row=6,column=0, padx=50)       #shows the base image for hangman
    dashImageRef=[]             
  
    
    

    quit = tk.Button(window, text='Quit', width=10, command=(window.destroy))    #defines the buttons
    quit.grid(row = 7, column = 0, pady = 100)                                  #creates the buttons
    for x in range(length):                                                          #makes the blank images appear  
        dashimage = tk.PhotoImage(file='final project/images/dash.png')
        blankimg=Label(window, image=dashimage)
        blankimg.grid(row = 5, column = (x+1))
        
        dashImageRef.append(dashimage)
    
    
    window.mainloop()   #infinite loop of making the window, must be after everything that wants to be displayed

def guess(button,letter,word,window):
    
    button['state']=tk.DISABLED #disables the button after the button is pressed once, to prevent guesses being used multiple times
    game(letter,word,window)    #runs the logic of the game
    return(letter)
    

def word_generator():               #random generator of a random word
    number=random.randint(1,15)

    switcher = {
        1:"start",
        2:"program",
        3:"python",
        4:"integer",
        5:"software",
        6:"homework",
        7:"tkinter",
        8:"import",
        9:"random",
        10:"breezy",
        11:"filler",
        12:"float",
        13:"string",
        14:"condition",
        15:"loop"
    }
    word=switcher.get(number)
    return word
def blankMaker(length):                             #makes the blanks
    counter=0
    
    blanks=""
    while (counter<length):                         #creates a blank word the same length as word
        blanks += "_"
        counter +=1
        
    return blanks
def restart(window):
    window.destroy()
    main()
    
    
def game(letter,word,window):                       #logic of the game
    global wrongnum
    global blanks
    tempListBlanks = list(blanks) 
    tempListWord=list(word) 
    
    incorrectGuess=True                             #sets the base to false of if its correct
    

    counter=0
    guess = letter                                     
    for x in (tempListWord):                        #checks every letter in the word
                                    
        if (x == guess):                            #checks if the current letter in the word is equal to the guess
            tempListWord.pop(counter)               #takes out the current letter in the index
            tempListWord.insert(counter, "_")       #inserts a blank
            tempListBlanks.pop(counter)             #takes out the blank at this position
            tempListBlanks.insert(counter, guess)   #places in the letter
            blanks = "".join(tempListBlanks)        #joins the blank list together
            label_font = font.Font(size=24)         #Displays the guessed letters
            correct=Label(window,text=letter,font=label_font)
            correct.grid(row=4, column=counter+1)
            incorrectGuess=False                    #updates to true if correct
        counter+=1 
    if incorrectGuess:                              #updates the hangman image by overlaying images to show more of the guy
        wrongnum+=1
        
        wrongImg= tk.PhotoImage(file='final project/images/'+str(wrongnum)+'.png')  #selects which image
        wrongImgDisplay=Label(window,image=wrongImg)
        wrongImgDisplay.grid(row=6,column=0,padx=50)
        wrongImgDisplay.config(image=wrongImg)
        wrongImgDisplay.image=wrongImg
        counter+=1                                       
        if (wrongnum==6):
                                               #displays a you lose window if incorrect too often
            lose = tk.Toplevel(window) #creates window
            lose.title("You lose")
           
            loseLabel=Label(lose,text="You have lost")
            loseLabel.grid(row=0,column=0)
            restartBtn=tk.Button(lose,text="Restart?",width=10, command=lambda:restart(window))
            restartBtn.grid(row=1,column=0)
            quit = tk.Button(lose, text='Quit', width=10, command=(window.destroy))    #defines the buttons
            quit.grid(row = 1, column = 1)
            
    if (word==blanks):                      #checks to see if the player has won and displays a window asking if they want to restart or quit
        win=tk.Toplevel(window)
        
        win.title("you win!!")
        winLabel=Label(win,text="You have won")
        winLabel.grid(row=0,column=0)
        restartBtn=tk.Button(win,text="Restart?",width=10, command=lambda:restart(window))
        restartBtn.grid(row=1,column=0)
        quit = tk.Button(win, text='Quit', width=10, command=(window.destroy))    #defines the buttons
        quit.grid(row = 1, column = 1)
        

    return wrongnum

main()

 
