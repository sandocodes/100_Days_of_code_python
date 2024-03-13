# Learning Tkinter a Python GUI library
import tkinter

window = tkinter.Tk()

window.title("My First GUI Program")
window
window.minsize(width=500, height=300)

# Label
my_label = tkinter.Label(text="I am a label", font=("Arial", 24, "bold"))
my_label.pack()





window.mainloop()