import tkinter
from tkinter import ttk
from tkinter import messagebox
from datetime import datetime

mainWindow = tkinter.Tk()
mainWindow.geometry("300x300")

currentTime = datetime.now()
chosenDag = tkinter.IntVar(mainWindow, int(currentTime.strftime("%d")))
chosenMaand = tkinter.IntVar(mainWindow, int(currentTime.strftime("%m")))
chosenJaar = tkinter.IntVar(mainWindow, int(currentTime.strftime("%Y")))

def calculate():
    endDate = "{}/{}/{}".format(chosenDag.get(), chosenMaand.get(), chosenJaar.get())
    start = datetime.strptime(currentTime.strftime("%d/%m/%Y"), "%d/%m/%Y")
    end =   datetime.strptime(endDate, "%d/%m/%Y")
    diff = end.date() - start.date()
    if diff.days < 0:
        messageText = "Dat is was {} dagen geleden".format(-diff.days)
    elif diff.days > 0:
        messageText = "Dat is over {} dagen".format(diff.days)
    else:
        messageText = "Dat is vandaag"
    messagebox.showinfo(message=messageText)

textBox = tkinter.Label(
    text="Date:"
)
textBox.grid(
    column=2,
    row=1,
    ipady=30,
)

comboboxDagen = ttk.Combobox(
    mainWindow,
    textvariable=chosenDag,
    width=5,
    values=[x for x in range(1,32)]
)
comboboxDagen.grid(
    column=1,
    row=2,
    padx=5
)

comboboxMaanden = ttk.Combobox(
    mainWindow,
    textvariable=chosenMaand,
    width=5,
    values=[x for x in range(1,13)]
)
comboboxMaanden.grid(
    column=2,
    row=2,
    padx=5
)

comboboxJaren = tkinter.Entry(
    mainWindow,
    bg="white",
    fg="black",
    textvariable=chosenJaar,
    width=5
)
comboboxJaren.grid(
    column=3,
    row=2,
    padx=5
)

btn = tkinter.Button(
    mainWindow,
    text="click here to calculate",
    command=calculate,
    bg="white",
    fg="black"
)
btn.grid(
    column=2,
    row=3,
    pady=5
)


mainWindow.mainloop()