import base
import graphics
import tkinter as tk
from PIL import Image, ImageTk  # Kräver pip-installationen Pillow för bildhantering

class SeaFrame(tk.Frame):
    """SeaFrame-klassen är en tkinter-frame och 
    definierar hela den ljusblå havsytan med rutor som visar vindhastighet och riktning.
    """
    
    def __init__(self, parent, controller, menu_gui):
        """Initierar klassens tkinter frame och genererar havet."""
        
        self.controller = controller
        self.menu_gui = menu_gui

        tk.Frame.__init__(self, parent, bg="skyblue", bd=5, relief="groove")
        
        self.generate_sea()

    def generate_sea(self):
        """Genererar havsytan och alla canvases som utgör rutorna."""
        
        for y, row in enumerate(self.controller.sea.matrix):
            self.grid_rowconfigure(y, weight=1)
            for x, square in enumerate(row):
                self.grid_columnconfigure(x, weight=1)
                
                square.widget = tk.Canvas(self, width=60, height=60, bd=2, relief="sunken", highlightthickness=0, bg="skyblue")
                square.widget.grid(row=square.y, column=square.x, padx=22, pady=22)

                square.widget.create_text(3, 0, text=square.wind_speed, fill="black", anchor=tk.NW, font=graphics.Graphics.standard_font)
                square.widget.create_text(28, 0, text="m/s", fill="black", anchor=tk.NW, font=graphics.Graphics.standard_font)
                
                square.raw_arrow = Image.open('arrow.gif')
                adjusted_angle = 90 - square.wind_dir  # Vinkeln som ger korrekt riktning på pilen med tanke på bildens originalriktning osv.
                square.image_arrow = ImageTk.PhotoImage(square.raw_arrow.rotate(adjusted_angle))
                square.widget.create_image(40, 40, image=square.image_arrow)

                square.widget.bind("<Button-1>", lambda event : self.mark_start(event=event))
                square.widget.bind("<Button-3>", lambda event : self.mark_goal(event=event))

    def mark_goal(self, event):
        """Reagerar på högerklick på rutor. 
        Sköter färger och 'square'-objektets instansattribut.
        """
        
        self.controller.sea.clear_result("goal")

        for square in self.controller.sea:
            if (event.widget is square.widget):
                square.is_start = False
                square.is_goal = True
                event.widget.config(bg="tomato")
        
        self.menu_gui.check_marked_squares()

    def mark_start(self, event):
        """Reagerar på vänsterklick på rutor. 
        Sköter färger och 'square'-objektets instansattribut.
        """
        
        self.controller.sea.clear_result("start")

        for square in self.controller.sea:
            if (event.widget is square.widget):
                square.is_goal = False
                square.is_start = True
                event.widget.config(bg="#5be854")
        
        self.menu_gui.check_marked_squares()

if __name__ == '__main__':
    base.Controller()
