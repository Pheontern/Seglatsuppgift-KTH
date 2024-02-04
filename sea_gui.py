import base
import graphics
from sea_frame import SeaFrame
import tkinter as tk

class SeaGuiFrame(tk.Frame):
    """SeaGuiFrame-klassen är en tkinter-frame som innehåller alla grundläggande element av hela den högra delen av GUI:t.
    Koordinatlistorna, havsytan och scrollbarsen.
    """

    def __init__(self, parent, controller, menu_gui):
        """Initierar klassens tkinter-frame och alla andra nödvändiga instansattribut, widgetar etc."""
        
        self.controller = controller
        self.parent = parent
        
        # Dessa ser till så att havsytan expanderar till rutans storlek om i vanliga fall är mindre än den.
        self.y_scrolling = (len(self.controller.sea.matrix) >= 6)
        self.x_scrolling = (len(self.controller.sea.matrix[0]) >= 6)

        tk.Frame.__init__(self, parent, bg=graphics.Graphics.get_default_color())
        self.grid(row=0, column=1, sticky="NSEW")
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(1, weight=1)

        self.canvas = tk.Canvas(self, width=1, height=1)  # Av någon anledning krävs att start-bredd o -höjd specificeras för att allt ska funka korrekt, även om widgeten expanderar.
        self.canvas.grid(row=1, column=1, sticky="NSEW")
        
        self.sea_frame = SeaFrame(self, controller, menu_gui)
        self.window_frame = self.canvas.create_window((0, 0), window=self.sea_frame, anchor="nw")
        self.canvas.bind("<Configure>", self.update_canvas_properties)
        
        # Ordningen spelar roll här då de använder varandras objekt.
        self.coord_markings()
        self.scrolling()

        menu_gui.tkraise()  # Alla skrollande ytor ska hamna under menyn.

    def get_scrollable_area(self):
        """Returnerar en tuple med havsytans bredd och längd, hela den skrollande ytans storlek (inte bara den synliga rutan)."""
        
        scroll_region = self.canvas.cget("scrollregion")
        left, top, right, bottom = map(int, scroll_region.split())

        scrollable_width = right - left
        scrollable_height = bottom - top

        return (scrollable_width, scrollable_height)

    def update_canvas_properties(self, event):
        """Uppdaterar egenskaper hos olika canvaser i SeaGuiFramen som måste uppdateras dynamiskt."""

        if (not self.x_scrolling):
            self.canvas.itemconfig(self.window_frame, width=self.canvas.winfo_width() - 5)  # Subtraherar fem för att inkludera reliefen runt havs-framen.

        if (not self.y_scrolling):
            self.canvas.itemconfig(self.window_frame, height=self.canvas.winfo_height() - 5)

        self.canvas.config(scrollregion=self.canvas.bbox("all"))
        self.parent_x.config(scrollregion=self.parent_x.bbox("all"))
        self.parent_y.config(scrollregion=self.parent_y.bbox("all"))

        # Anpassar koordinatmarkeringarnas storlek till havsytans.
        self.parent_x.itemconfig(self.x_coords_frame, width=self.get_scrollable_area()[0] + 5)  # Adderar fem för att inkludera reliefen runt havs-framen (self.sea_frame).
        self.parent_y.itemconfig(self.y_coords_frame, height=self.get_scrollable_area()[1] + 5)
        self.parent_x.config(height=self.top_coords.winfo_height())
        self.parent_y.config(width=self.side_coords.winfo_width())

    def scrolling(self):
        """Definierar scrollbars och konfigurerar de korrekt."""
        
        scrollbar_y = tk.Scrollbar(self, width=20, orient="vertical", command=(self.double_scroll_y if self.y_scrolling else None))
        scrollbar_y.grid(column=2, row=1, rowspan=2, sticky="NSE")
        self.canvas.config(yscrollcommand=scrollbar_y.set, scrollregion=self.canvas.bbox("all"))
        self.parent_y.config(yscrollcommand=scrollbar_y.set, scrollregion=self.parent_y.bbox("all"))

        scrollbar_x = tk.Scrollbar(self, width=20, orient="horizontal", command=(self.double_scroll_x if self.x_scrolling else None))
        scrollbar_x.grid(row=2, column=1, sticky="EWS")
        self.canvas.config(xscrollcommand=scrollbar_x.set, scrollregion=self.canvas.bbox("all"))
        self.parent_x.config(xscrollcommand=scrollbar_x.set, scrollregion=self.parent_x.bbox("all"))

    def double_scroll_y(self, *args):
        """Skrollar havsytan och den vertikala koordinatlistan."""
        
        self.canvas.yview(*args)
        self.parent_y.yview(*args)
    
    def double_scroll_x(self, *args):
        """Skrollar havsytan och den horisontella koordinatlistan."""
        
        self.canvas.xview(*args)
        self.parent_x.xview(*args)

    def coord_markings(self):
        """Genererar koordinatlistorna som canvases och konfigurerar korrekt."""
        
        self.top_coords = tk.Frame(self.parent, bd=4)  # Den här widgeten placeras aldrig i griden utan läggs till via en canvasmetod senare, därför har den self.parent som ägare.
        for x in range(self.controller.sea.width):
            self.top_coords.grid_columnconfigure(x + 1, weight=1)
            coords_widget = tk.Label(self.top_coords, text=f"{x}", font=graphics.Graphics.standard_font)
            coords_widget.grid(row=0, column=x+1)
        
        self.side_coords = tk.Frame(self.parent, bd=4)  # Samma med den här.
        for y in range(self.controller.sea.height):
            self.side_coords.grid_rowconfigure(y + 1, weight=1)
            coords_widget = tk.Label(self.side_coords, text=f"{y}", font=graphics.Graphics.standard_font)
            coords_widget.grid(row=y+1, column=0, padx=6)

        self.parent_x = tk.Canvas(self, bg="red", height=self.top_coords.winfo_height(), width=1, highlightthickness=0)
        self.parent_x.grid(row=0, column=1, sticky="NEWS")
        self.x_coords_frame = self.parent_x.create_window((0, 0), window=self.top_coords, anchor="nw")

        self.parent_y = tk.Canvas(self, bg="red", width=self.side_coords.winfo_width(), height=1, highlightthickness=0)
        self.parent_y.grid(row=1, column=0, sticky="NSEW")
        self.y_coords_frame = self.parent_y.create_window((0, 0), window=self.side_coords, anchor="nw")

if __name__ == '__main__':
    base.Controller()
