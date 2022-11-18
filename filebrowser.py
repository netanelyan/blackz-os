from tkinter import *
from tkinter import filedialog
import os

def openFile():
    filepath = filedialog.askopenfilename(initialdir="/",
                                          title="Open your file",
                                          filetypes= (("text files","*.txt"),
                                          ("all files","*.*")))
    os.startfile(filepath)

window = Tk()
button = Button(text="Open a file",command=openFile)
button.pack()
window.mainloop()
