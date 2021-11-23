import tkinter
from tkinter import ttk
number = 0
lastPressed = None

def windowChange(self):
    textLabel.configure(text=number)
    if number > 0:
        mainWindow.configure(bg="green")
    elif number < 0:
        mainWindow.configure(bg="red")
    else:
        mainWindow.configure(bg="grey")

def makeYellow(self):
    mainWindow.configure(bg="yellow")

def doubleClick(self):
    global number
    if lastPressed == "up":
        number *= 3
    elif lastPressed == "down":
        number /= 3
    windowChange("")

def autoClick():
    if autoClickOn.get() == 1:
        if lastPressed == "up":
            numUp("")
        elif lastPressed == "down":
            numDown("")
        mainWindow.after(200, autoClick)

def numUp(self):
    global number
    global lastPressed
    number += 1
    lastPressed = "up"
    windowChange("")

def numDown(self):
    global number
    global lastPressed
    number -= 1
    lastPressed = "down"
    windowChange("")

mainWindow = tkinter.Tk()
mainWindow.configure(
    padx=10,
    bg="grey"
)

upButton = tkinter.Button(mainWindow)
upButton.configure(
    bg="white",
    text="up",
    fg="black",
)
upButton.pack(pady=10, fill="x")
upButton.bind("<Button-1>", numUp)

textLabel = tkinter.Label(mainWindow)
textLabel.configure(
    bg="white",
    text=number,
    fg="black",
    justify="center"
)
textLabel.pack(pady=10, fill="x")
textLabel.bind("<Enter>", makeYellow)
textLabel.bind("<Leave>", windowChange)
textLabel.bind("<Double-Button-1>", doubleClick)

downButton = tkinter.Button(mainWindow)
downButton.configure(
    bg="white",
    text="down",
    fg="black"
)
downButton.pack(pady=10, fill="x")
downButton.bind("<Button-1>", numDown)

autoClickOn = tkinter.IntVar()
checkmark = ttk.Checkbutton(
    mainWindow,
    text="Turn this on for autoclick",
    command=autoClick,
    variable=autoClickOn
)
checkmark.pack(
    pady=5
)

mainWindow.bind("<space>", doubleClick)
mainWindow.bind("<Up>", numUp)
mainWindow.bind("<KP_Add>", numUp)
mainWindow.bind("<Down>", numDown)
mainWindow.bind("<KP_Subtract>", numDown)

mainWindow.mainloop()