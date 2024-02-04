import base
import graphics
import tkinter as tk
from tkinter import messagebox

class MenuFrame(tk.Frame):
    """MenuFrame-klassen är en tkinter-frame och upptar den vänstra sidan av GUI:t (med orange ram).
    Den innehåller en knapp för att starta beräkningarna samt en textruta som ger resultat och felmeddelanden.
    """
    
    def __init__(self, parent, controller):
        """Initierar klassens tkinter-frame och dess widgets."""
        
        self.controller = controller
        
        tk.Frame.__init__(self, parent, bg="antiquewhite", highlightcolor="sandybrown", highlightbackground="sandybrown", highlightthickness=7)
        
        self.grid(row=0, column=0, rowspan=2, sticky="NSEW")
        self.grid_propagate(False)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_columnconfigure(0, weight=1)
        
        self.start_button = tk.Button(self, text="Calculate", bg="#d1cfcf", activebackground="red", font=graphics.Graphics.standard_font)
        self.start_button.config(command=self.calculate)
        self.start_button.grid(row=0, column=0, sticky=tk.S, pady=5)

        self.status_title = tk.Label(self, text="Last results", relief="groove", font=graphics.Graphics.standard_font)
        self.status_title.grid(row=1, column=0, sticky="S")

        self.status_output = tk.Text(self, width=40, height=10, state=tk.DISABLED)
        self.status_output.grid(row=2, column=0, sticky="N")

    def calculate(self):
        """Aktiveras av calculate-knappen "start_button".
        Startar segelbåtens beräkningar om start-/slut-position är markerade (annars visas varning), 
        hämtar in resultatet och visar upp det i GUI:t.
        """
        
        if (self.controller.sea.ready_to_measure):
            
            self.start_button.config(text="Working on it...")
            self.start_button.update()

            result = self.controller.sailboat.start_measuring()
            
            self.start_button.config(text="Calculate")

            self.status_output.config(state=tk.NORMAL)
            self.status_output.delete('1.0', tk.END)

            if (isinstance(result, dict)):
                coords_path = []
                for square in result["path"]:
                    coords_path.append(f"({square.x}, {square.y})")
                result["coords_path"] = coords_path

                result["path"].pop(0)
                result["path"].pop(-1)
                for i, passed_square in enumerate(result["path"]):
                    for square in self.controller.sea:
                        if (passed_square is square):
                            square.step_number = square.widget.create_text(3, 40, text=f"{i + 1}", fill="black", anchor=tk.NW, font=graphics.Graphics.standard_font, tag="step_number")
                            square.widget.config(bg="yellow")
            
                self.status_output.insert(tk.END, f'Best time: {round(result["time"], 5)} s\n\n')
                self.status_output.insert(tk.END, f'Best path: {", ".join(result["coords_path"])}\n\n')
                self.status_output.insert(tk.END, f'Execution time: {round(result["calc_time"], 5)} s')
            else:
                self.status_output.insert(tk.END, result)
            
            self.status_output.config(state=tk.DISABLED)
        
        else:
            error_message = messagebox.Message(self, title="A problem occurred", 
                                                message="You need to choose a new start and end position (left/right click on a square).")
            error_message.show()

    def check_marked_squares(self): 
        """Aktiveras om någon trycker på en ruta i havet.
        Kontrollerar om start och slut har markerats och gör calculate-knappen grön, ändrar annars tillbaka till standard-färg.
        'no_test' används enbart av calculate-metoden och vid True sätter alltid tillbaka till standard.
        """
        
        check_start = self.controller.sea.get_square("start")
        check_goal = self.controller.sea.get_square("goal")

        if (check_start and check_goal):
            self.start_button.config(bg="#5be854", activebackground="#5be854")
            self.controller.sea.ready_to_measure = True
        else:
            self.start_button.config(bg="#d1cfcf", activebackground="red")
            self.controller.sea.ready_to_measure = False

if __name__ == '__main__':
    base.Controller()
