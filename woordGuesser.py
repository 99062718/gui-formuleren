import tkinter
import string
import random
from tkinter import StringVar, ttk, messagebox
from typing import Collection

mainWindow = tkinter.Tk()
mainWindow.configure(bg="white")
mainWindow.geometry("600x300")

topText = StringVar(mainWindow, "")
btnText = StringVar(mainWindow, "")

topTextLabel = tkinter.Label(
    fg="black",
    bg="white",
    textvariable=topText,
    width=20
)
topTextLabel.grid(
    pady=10,
    column=2,
    columnspan=3,
    row=1
)

btn = tkinter.Button(
    bg="white",
    fg="black",
    textvariable=btnText
)
btn.grid(
    pady=10,
    ipadx=5,
    column=3,
    columnspan=2,
    row=4
)

def vulWoordInScreen():
    global wordToGuess
    global vulInHier
    global entryLabel
    wordToGuess = StringVar(mainWindow, "")
    vulInHier = ttk.Entry(
        textvariable=wordToGuess
    )
    vulInHier.grid(
        column=2,
        columnspan=3,
        row=2,
        padx=20
    )

    entryLabel = tkinter.Label(
        mainWindow,
        bg="white",
        fg="black",
        text="4 tot 7 characters lang"
    )
    entryLabel.configure(font=("helvetica", 5))
    entryLabel.grid(
        column=3,
        columnspan=2,
        row=3,
        pady=2
    )

    btn.configure(command=checkWordLength)
    btnText.set("Stel woord in")
    topText.set("Vul hier een woord in:")
    
def checkWordLength():
    if len(wordToGuess.get()) > 7 or len(wordToGuess.get()) < 4:
        messagebox.showerror(message="Woord moet 4 tot en met 7 letters zijn!")
    else:
        generateGuessScreen()

def generateGuessScreen():
    global spinboxArray
    global spinboxContentArray
    global wordLength
    global score

    vulInHier.destroy()
    entryLabel.destroy()
    topText.set("Raad het woord")
    btnText.set("Raad woord")
    btn.configure(command=raadWoord)

    wordLength = len(wordToGuess.get())
    score = wordLength * wordLength
    spinboxArray = []
    alphabet = list(string.ascii_lowercase)
    spinboxContentArray = []

    for x in range(0, wordLength):
        randomValues = random.sample(alphabet, 5)
        randomValues[random.randint(0, 4)] = wordToGuess.get()[x]
        spinboxContentArray.append(StringVar(mainWindow, ""))

        spinboxArray.append(
            ttk.Spinbox(
                mainWindow,
                width=5,
                values=randomValues,
                textvariable=spinboxContentArray[x]
            )
        )
        spinboxArray[x].grid(
            row=2,
            column=x,
            ipadx=10
        )

def raadWoord():
    global score

    goodAndWrong = [0, 0]

    for x in range(0, wordLength):
        if spinboxContentArray[x].get() == wordToGuess.get()[x]:
            goodAndWrong[0] += 1
        else:
            goodAndWrong[1] += 1
    
    if goodAndWrong[0] == wordLength:
        messagebox.showinfo(message="U heeft het woord goed geraden!")
        for box in spinboxArray:
            box.destroy()
        vulWoordInScreen()
    else:
        messagebox.showerror(message="Helaas! U heeft er {} fout! Probeer het nog eens".format(goodAndWrong[1]))
        score -= goodAndWrong[1] * 2
        if score <= 0:
            messagebox.showerror(message="U heeft verloren!")
            mainWindow.destroy()

vulWoordInScreen()

mainWindow.mainloop()