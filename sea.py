from sea_square import SeaSquare

class Sea:
    """Havsklassen innehåller all data ett hav kräver, alla rutor och deras egenskaper."""
    
    def __init__(self, filepath):
        """Läser in datan från havsmatris-filen och definierar instansattribut som höjd och bredd."""
        
        self.filepath = filepath
        
        try:
            self.matrix = self.read_matrix_file()
        except Exception as error:
            if ("Matrisfilen" in str(error)):
                print(error)
            else:
                print("Matrisfilen hittades inte eller var felaktigt formaterad på något sätt.")
                print("Se till så att filen heter 'havsmatris.utf8' och ligger i samma mapp som programmet.")
            exit()
        
        self.height = len(self.matrix)
        self.width = len(self.matrix[0])

        self.ready_to_measure = False  # Redo att mäta endast om start och mål markerats.

    def __iter__(self):
        """Ser till så att man slipper gå igenom listorna i listan (matrisen) manuellt 
        utan direkt kan iterera på klassobjektet för att få rutorna i ordning.
        """

        for row in self.matrix:
            for square in row:
                yield square

    def read_matrix_file(self):
        """Läser in matrisfilen och returnerar datan i en 2D-lista."""
        
        with open(self.filepath, "r", encoding="utf8") as handle:
            lines = handle.read().splitlines()
        
        # Tar bort tomma rader och kommentarer så att enbart matrisen är kvar.
        length = len(lines)
        for i in reversed(range(length)): 
            if (lines[i] == "" or lines[i][0] == "#"): 
                lines.pop(i)

        # Sätter ihop värdena till en korrekt matris.
        matrix = []
        for line_index, line in enumerate(lines):
            line = line.replace(" ", "").split(',') 
            row = []
            for row_index, values in enumerate(line):
                split_values = values.split('/')
                values = (int(split_values[0]), int(split_values[1]))
                
                if (values[0] < 0):
                    raise Exception("Matrisfilen är felaktig: Vindhastigheten får inte vara negativ.")
                elif (values[1] not in (0, 45, 90, 135, 180, 225, 270, 315)):
                    raise Exception("Matrisfilen är felaktig: Vindriktningen måste vara någon av följande (grader): (0, 45, 90, 135, 180, 225, 270, 315)")

                row.append(SeaSquare((row_index, line_index), values))
            matrix.append(row)
        
        return matrix

    def get_square(self, type):
        """Returnerar den antingen den startmarkerade eller målmarkerade rutan."""
        
        attr = "is_start"
        if (type == "start"):
            attr = "is_start"
        elif (type == "goal"):
            attr = "is_goal"

        for square in self:
            if getattr(square, attr):
                return square
        return False
    
    def clear_result(self, type):
        """Rensar ut ett gulmarkerat resultat från skärmen (och tar bort start/mål)"""
        
        for square in self:
            if square.is_start:
                if (type == "start"):
                    square.is_start = False
                    square.widget.config(bg="skyblue")
            elif square.is_goal:
                if (type == "goal"):
                    square.is_goal = False
                    square.widget.config(bg="skyblue")
            else:
                square.widget.config(bg="skyblue")
                square.widget.delete("step_number")
