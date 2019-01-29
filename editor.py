from tkinter import *
from tkinter import scrolledtext
from tkinter import filedialog

#root for main window
window = Tk()
window.geometry('350x200')
window.title("NoteMadeEasy")
TextArea  = scrolledtext.ScrolledText(window, width = 300, height = 150)

#
#functions:
#
def openFile():
    file = filedialog.askopenfile(parent = window, title = "select a text file")
    print(file)
    if file != None:
        content = file.read()
        TextArea.insert('1.0',content)

        file.close()

def saveFile():
    file = filedialog.asksaveasfile(mode="w")
    if file != None:
        data = TextArea.get('1.0',END)
        file.write(data)
        file.close()

#menu options
menubar = Menu(window)
filemenu = Menu(menubar, tearoff = 0)
menubar.add_cascade(label='File',menu=filemenu)
filemenu.add_command(label="New")
filemenu.add_command(label="Open", command= openFile)
filemenu.add_command(label="Save", command= saveFile)
filemenu.add_command(label="Print")
filemenu.add_separator()
filemenu.add_command(label="Exit")


helpmenu = Menu(menubar)
menubar.add_cascade(label="Help")

TextArea.pack()

window.config(menu = menubar)
#keep window open
window.mainloop()
