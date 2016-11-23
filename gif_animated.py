from threading import Thread
from tkinter import *
import time
import os


class Application(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.pack(fill=BOTH)
        root.protocol("WM_DELETE_WINDOW", self.close)

        self.num = 0

        self.create_widgets()

    def create_widgets(self):
        self.label = Label(self, bd=0)
        self.label.pack()

        Thread(target=self.animate).start()

    def animate(self):
        while True:
            try:
                time.sleep(0.001)
                img = PhotoImage(file="title.gif", format="gif - {}".format(self.num))

                self.label.config(image=img)
                self.label.image = img

                self.num += 1
            except:
                self.num = 0

    def close(self):
        os._exit(0)


root = Tk()

app = Application(root)

root.mainloop()
