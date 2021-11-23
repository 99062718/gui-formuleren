import tkinter
import random
from tkinter import messagebox

mainWindow = tkinter.Tk()
mainWindow.geometry("900x600")

time = 20
timeText = tkinter.StringVar(mainWindow, "Time remaining: {}".format(time))
score = 0
scoreText = tkinter.StringVar(mainWindow, "Score: {}".format(score))

#---------Frames and labels

textFrame = tkinter.Frame(
    mainWindow,
    height=20,
    bg="black"
)
textFrame.pack(
    fill="x",
    side="top"
)

timeLabel = tkinter.Label(
    textFrame,
    textvariable=timeText,
    bg="black",
    anchor=tkinter.W
)
timeLabel.pack(
    fill='x', 
    side='left'
)

scoreLabel = tkinter.Label(
    textFrame,
    textvariable=scoreText,
    bg="black",
    anchor=tkinter.E
)
scoreLabel.pack(
    fill='x', 
    side='right'
)

playWindow = tkinter.Frame(
    mainWindow,
    bg="white"
)
playWindow.pack(
    expand=True,
    fill="both",
    side="top"
)

#---------Functions
def createNewBtn():
    global toPress
    global randNum1
    global randNum2
    global choices
    choices = [["<space>", "<w>", "<a>", "<s>", "<d>"],["<Button>", "<Double-Button>", "<Triple-Button>"]]
    randNum1 = random.randint(0, 1)
    randNum2 = random.randint(0, len(choices[randNum1]) - 1)

    toPress = tkinter.Label(
        playWindow,
        height=2,
        width=20,
        text=choices[randNum1][randNum2],
        fg="white",
        bg="red"
    )
    toPress.place(
        x=random.randint(1, 700),
        y=random.randint(1, 500)
    )

    if randNum1 == 0:
        mainWindow.bind(choices[randNum1][randNum2], destroyBtn)
    else:
        toPress.bind(choices[randNum1][randNum2], destroyBtn)

def destroyBtn(self, endOfGame="no"):
    global score
    toPress.destroy()
    if randNum1 == 0:
        mainWindow.unbind(choices[randNum1][randNum2])
        score += 1
    else:
        score += 2
    scoreText.set("Score: {}".format(score))
    if endOfGame != "yes":
        createNewBtn()

def startGame():
    createNewBtn()
    mainWindow.after(1000, timer)

def timer():
    global time
    time -= 1
    timeText.set("Time remaining: {}".format(time))
    if time != 0:
        mainWindow.after(1000, timer)
    else:
        endScreen()

def endScreen():
    destroyBtn("", "yes")
    answer = messagebox.askyesno("play again?", "Your final score is {}! \nWould you like to try again?".format(score))
    if answer:
        createStartMenu()
    else:
        mainWindow.destroy()

def deleteStartMenu():
    global time
    btn.destroy()
    time = int(entryBox.get())
    entryBox.destroy()
    startGame()

def createStartMenu():
    global btn
    global score
    global time
    global entryBox
    score = 0
    time = 20
    timeVar = tkinter.IntVar(mainWindow, time)
    entryBox = tkinter.Entry(
        playWindow,
        bg="white",
        fg="black",
        justify="center",
        textvariable=timeVar
    )
    entryBox.pack(
        pady=200
    )
    btn = tkinter.Button(
        playWindow,
        bg="white",
        fg="black",
        text="Click to start game",
        command=deleteStartMenu,
        height=6,
        width=30,
        justify="center"
    )
    btn.pack(
        pady=10
    )

#---------Start of program

createStartMenu()

mainWindow.mainloop()