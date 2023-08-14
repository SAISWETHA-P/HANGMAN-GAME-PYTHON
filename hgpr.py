import random
from tkinter import *
from tkinter import messagebox
from string import ascii_uppercase
window=Tk()
window.title("Hangman")
word_list = ["MASTER","BEAST","VALIMAI","VIKRAM","DOCTOR","ALAIPAYUDHEY","SOORARAIPOTTRU","JAIBHIM","ASURAN","ANBESIVAM","VADACHENNAI","KAITHI"]
photos=[PhotoImage(file="C:/Users/Swetha/Desktop/hangman/hang0.png" ) ,PhotoImage(file="C:/Users/Swetha/Desktop/hangman/hang1.png"),PhotoImage(file="C:/Users/Swetha/Desktop/hangman/hang2.png"),PhotoImage(file="C:/Users/Swetha/Desktop/hangman/hang3.png"),
          PhotoImage(file="C:/Users/Swetha/Desktop/hangman/hang4.png"),PhotoImage(file="C:/Users/Swetha/Desktop/hangman/hang5.png"),PhotoImage(file="C:/Users/Swetha/Desktop/hangman/hang6.png"),PhotoImage(file="C:/Users/Swetha/Desktop/hangman/hang7.png"),
          PhotoImage(file="C:/Users/Swetha/Desktop/hangman/hang8.png"),PhotoImage(file="C:/Users/Swetha/Desktop/hangman/hang9.png"),PhotoImage(file="C:/Users/Swetha/Desktop/hangman/hang10.png"),PhotoImage(file="C:/Users/Swetha/Desktop/hangman/hang0.png"),]
numberOfGuesses = 0
the_word_withSpaces = ''
def newgame ():
    global the_word_withSpaces
    global numberOfGuesses
    numberOfGuesses=0
    imgLabel.config(image=photos[0])
    the_word=random.choice(word_list)
    the_word_withSpaces=" ".join(the_word)
    lblWord.set(" ".join("_"*len(the_word)))

def guess(letter):
    global numberOfGuesses
    if numberOfGuesses<11:
        txt=list(the_word_withSpaces)
        guessed=list(lblWord.get())
    if the_word_withSpaces.count(letter)>0:
        for c in range(len(txt)):
            if txt[c]==letter:
                guessed[c]=letter
            lblWord.set("".join(guessed))
            if lblWord.get()==the_word_withSpaces:
                messagebox.showinfo("Hangman", "You guessed it!")
    else:
        numberOfGuesses+=1
        imgLabel.config(image=photos[numberOfGuesses])
        if numberOfGuesses==11:
            messagebox.showwarning("Hangman","Game Over")
imgLabel=Label(window)
imgLabel.grid(row=0, column=0,columnspan=3, padx=10, pady=40)
imgLabel.config(image=photos[0])

lblWord=StringVar()
Label(window, textvariable=lblWord, font=("Consolas 24 bold")).grid(row=0, column=3, columnspan=6, padx=10)


n=0
for c in ascii_uppercase:
    Button(window, text=c, command=lambda c=c: guess(c), font=("helvetica 18"), width=4). grid(row=1+n//9, column=n%9)
    n+=1
Button(window, text="New\nGame", command=lambda:newgame(), font=("Helvetica 10 bold")).grid(row=3, column=8, sticky="NSWE")
    
newgame ()
window.mainloop()











