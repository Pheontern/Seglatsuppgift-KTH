import base
import tkinter as tk
import menu_gui as menu_g
import sea_gui as sea_g

class Graphics:
    """Graphics-klassen hanterar all grafik i programmet med hjälp av Tkinter."""

    standard_font = ("Consolas", 15, "bold")

    def __init__(self, controller):
        """Initierar klassen med alla de mest grundläggande widgetarna som i sin tur hanterar mer specifika widgets."""

        self.root = tk.Tk()
        self.root.title("Havet")
        self.root.config(bg="snow")

        window_height = 600
        window_width = 1000
        
        self.root.minsize(width=window_width, height=window_height)
        self.root.resizable(width=False, height=False)
    
        base_frame = tk.Frame(self.root, bg="gray")
        base_frame.pack(fill="both", expand=True, padx=10, pady=10)
        
        # Detta innebär att SeaGuiFrame får 6 av 10 andelar av bredden och därför blir en kvadrat med höjd 600.
        base_frame.grid_columnconfigure(0, weight=window_width-window_height)
        base_frame.grid_columnconfigure(1, weight=window_height)
        base_frame.grid_rowconfigure(0, weight=1)
        
        menu_gui = menu_g.MenuFrame(base_frame, controller)
        sea_gui = sea_g.SeaGuiFrame(base_frame, controller, menu_gui)
        
        self.root.mainloop()

    @staticmethod
    def get_default_color():
        """Hämtar standardfärgen för tkinter-knappar/labels etc.
        Detta krävs då olika operativsystem har olika standarder.
        """
        
        return tk.Label().cget("background")

if __name__ == '__main__':
    base.Controller()
