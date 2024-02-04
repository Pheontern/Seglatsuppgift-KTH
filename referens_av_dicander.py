"""Använder Frame som Ram som samlar komponenterna.
Visar en "Avsluta"-knapp som stänger Tk-fönstret."""

from tkinter import *


class Ram(Frame):
    """Ett fönster med en knapp för att avsluta."""
    def __init__(self, parent=None):
        Frame.__init__(self, parent)
        self.pack()
        self.avsluta = Button(self, text="Avsluta", command=self.quit)
        self.avsluta.pack()


def main():
    root = Tk()
    t = Ram(root)
    t.mainloop()
    root.destroy()


main()
