import tkinter

mainWindow = tkinter.Tk()
mainWindow.geometry("1050x1050")
array = []
currentColor = "black"

for currentRow in range(0, 10):
    array.append([])
    for currentColumn in range(0, 10):
        box = tkinter.Frame(bg=currentColor)
        box.grid(
            column=currentColumn,
            row=currentRow,
            ipadx=50,
            ipady=50
        )
        array[currentRow].append(box)
        currentColor = "white" if currentColor == "black" else "black"
    currentColor = "white" if currentColor == "black" else "black"

mainWindow.mainloop()