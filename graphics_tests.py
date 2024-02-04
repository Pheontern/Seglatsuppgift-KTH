import base
from tkinter import *

"""Den här filen användes bara för att testa tkinter och se hur det fungerar."""

def change_text(button):
    button["text"] = "test"

def add_item(list_box):
    list_box.insert(0, "TV_KONTROLL SOM INTE FUNGERAR")


def initialize():
    
    root = Tk()

    root.title("Kanon")

    #root.geometry("800x900")
    root.minsize(width=600, height=500)

    root.resizable(width=False, height=False)


    frame=Frame(root, width=330, height=350, bd=200, relief="groove")
    frame2=Frame(root, width=330, height=350, bg="red")
    
    label_test = Label(root, text="TESTA")
    
    button = Button(root, text="Rad 0 center", command=lambda:add_item(list_box2))
    button2 = Button(root, text="Tryck inte", command=lambda:add_item(list_box))
    button3 = Button(root, text="Tryck", command=lambda:change_text(button3))
    
    list_box = Listbox(frame, height=20, width=50)
    list_box2 = Listbox(frame2, height=20, width=50)

    frame.grid(row=0, column=2, rowspan=20, padx=10, pady=100)
    frame2.grid(row=6, column=3, rowspan=20)

    button.grid(row=0, column=1)
    button2.grid(row=1, column=1)
    button3.grid(row=6, column=1)

    label_test.grid(row=6, column=0, sticky=W)
    
    list_box.grid(row=0, column=2, rowspan=20, padx=10, pady=10)
    list_box2.grid(row=6, column=3, rowspan=20, padx=20, pady=10)
    
    
    for i in range(3):
        list_box.insert(i, "TV_KONTROLL")

    root.mainloop()


if __name__ == '__main__':
    base.main()