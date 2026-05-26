from tkinter import *
from text_to_speech import speak

root = Tk()
root.title("Jarvis Assistant")
root.geometry("400x300")

label = Label(root, text="Enter Message")
label.pack(pady=10)

entry = Entry(root, width=40)
entry.pack(pady=10)


def speak_text():
    text = entry.get()
    speak(text)


button = Button(root, text="Speak", command=speak_text)
button.pack(pady=20)

root.mainloop()
