#Alexander Cox
#tkinter display window

import tkinter as tk            # import the gui
def buttons(window):            #list of every button, sending the letter corresponding to the button and the button name to be
    buttonHeight = 2
    buttonWidth=2
    aBtn = tk.Button(window,height=buttonHeight, width=buttonWidth, text="a", command=lambda: guess("a",aBtn))
    aBtn.place(x=50,y=400)
    bBtn = tk.Button(window,height=buttonHeight, width=buttonWidth, text="b", command=lambda: guess("b",bBtn))
    bBtn.place(x=70,y=400)
    cBtn = tk.Button(window,height=buttonHeight, width=buttonWidth, text="c", command=lambda: guess("c",cBtn))
    cBtn.place(x=90, y=400)
    dBtn = tk.Button(window,height=buttonHeight, width=buttonWidth, text="d", command=lambda: guess("d",dBtn))
    dBtn.place(x=110, y=400)
    eBtn = tk.Button(window,height=buttonHeight, width=buttonWidth, text="e", command=lambda: guess("e",eBtn))
    eBtn.place(x=130, y=400)
    fBtn = tk.Button(window,height=buttonHeight, width=buttonWidth, text="f", command=lambda: guess("f",fBtn))
    fBtn.place(x=150, y=400)
    gBtn = tk.Button(window,height=buttonHeight, width=buttonWidth, text="g", command=lambda: guess("g",gBtn))
    gBtn.place(x=170, y=400)
    hBtn = tk.Button(window,height=buttonHeight, width=buttonWidth, text="h", command=lambda: guess("h",hBtn))
    hBtn.place(x=190,y=400)
    iBtn = tk.Button(window,height=buttonHeight, width=buttonWidth, text="i", command=lambda: guess("i",iBtn))
    iBtn.place(x=210, y=400)
    jBtn = tk.Button(window,height=buttonHeight, width=buttonWidth, text="j", command=lambda: guess("j",jBtn))
    jBtn.place(x=230, y=400)
    kBtn = tk.Button(window,height=buttonHeight, width=buttonWidth, text="k", command=lambda: guess("k",kBtn))
    kBtn.place(x=250, y=400)
    lBtn = tk.Button(window,height=buttonHeight, width=buttonWidth, text="l", command=lambda: guess("l",lBtn))
    lBtn.place(x=270, y=400)
    mBtn = tk.Button(window,height=buttonHeight, width=buttonWidth, text="m", command=lambda: guess("m",mBtn))
    mBtn.place(x=290,y=400)
    nBtn = tk.Button(window,height=buttonHeight, width=buttonWidth, text="n", command=lambda: guess("n",nBtn))
    nBtn.place(x=50, y=475)
    oBtn = tk.Button(window,height=buttonHeight, width=buttonWidth, text="o", command=lambda: guess("o",oBtn))
    oBtn.place(x=70, y=475)
    pBtn = tk.Button(window,height=buttonHeight, width=buttonWidth, text="p", command=lambda: guess("p",pBtn))
    pBtn.place(x=90, y=475)
    qBtn = tk.Button(window,height=buttonHeight, width=buttonWidth, text="q", command=lambda: guess("q",qBtn))
    qBtn.place(x=110, y=475)
    rBtn = tk.Button(window,height=buttonHeight, width=buttonWidth, text="r", command=lambda: guess("r",rBtn))
    rBtn.place(x=130, y=475)
    sBtn = tk.Button(window,height=buttonHeight, width=buttonWidth, text="s", command=lambda: guess("s",sBtn))
    sBtn.place(x=150, y=475)
    tBtn = tk.Button(window,height=buttonHeight, width=buttonWidth, text="t", command=lambda: guess("t",tBtn))
    tBtn.place(x=170, y=475)
    uBtn = tk.Button(window,height=buttonHeight, width=buttonWidth, text="u", command=lambda: guess("u",uBtn))
    uBtn.place(x=190, y=475)
    vBtn = tk.Button(window,height=buttonHeight, width=buttonWidth, text="v", command=lambda: guess("v",vBtn))
    vBtn.place(x=210, y=475)
    wBtn = tk.Button(window,height=buttonHeight, width=buttonWidth, text="w", command=lambda: guess("w",wBtn))
    wBtn.place(x=230, y=475)
    xBtn = tk.Button(window,height=buttonHeight, width=buttonWidth, text="x", command=lambda: guess("x",xBtn))
    xBtn.place(x=250, y=475)
    yBtn = tk.Button(window,height=buttonHeight, width=buttonWidth, text="y", command=lambda: guess("y",yBtn))
    yBtn.place(x=270, y=475)
    zBtn = tk.Button(window,height=buttonHeight, width=buttonWidth, text="z", command=lambda: guess("z",zBtn))
    zBtn.place(x=290, y=475)

    
    



def main():
    window=tk.Tk() #creates window
    window.title("Hangman game") #changes the title of the window
    window.geometry("600x600")
    window.maxsize(600,600)
    window.minsize(600,600)
    
    buttons(window)
    button = tk.Button(window, text='Quit',width=10, command=window.destroy)    #defines the buttons
    button.place(x=280,y=550)   #creates the buttons


    window.mainloop()   #infinite loop of making the window, must be after everything that wants to be displayed

def guess(letter, button):
    
    print(letter)
    button['state']=tk.DISABLED #disables the button after the button is pressed once, to prevent guesses being used multiple times




main()
 