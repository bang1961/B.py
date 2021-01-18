from tkinter import *
main = Tk()
main.title("Tk Test")
main.geometry("300x200")

lbl = Label(main, text="Label", font="Arial 20")
lbl.pack()

def appleclick():
    lbl["text"] = "Apple"
apple = Button(main, text="Apple", foreground="Red", command=appleclick)
apple.pack()

def orangeclick():
    lbl["text"] = "Orange"
orange = Button(main, text="Orange", foreground="Green", command=orangeclick)
orange.pack()

main.mainloop()

