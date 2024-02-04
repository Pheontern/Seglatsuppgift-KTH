from math import sqrt
import base

class SeaSquare:
    """SeaSquare-klassen definierar en ruta i havet med huvudsakliga egenskaper vindhastighet och riktning.
    Det kommer alltså att finnas lika många SeaSquare-objekt som element i matrisen 
    och de sparas i ett objekt av Sea-klassen.
    """
    
    def __init__(self, coords, data):
        """Initierar instansattribut hos klassen, exempelvis vindhastighet och riktning utifrån konstruktorns parametrar."""

        self.wind_speed = data[0]
        self.wind_dir = data[1]

        self.x = coords[0]
        self.y = coords[1]
        
        self.is_start = False
        self.is_goal = False

        # Klassen behöver dessa grafikrelaterade instansattribut för att de ska vara lättåtkomliga, de initieras i grafikklasserna.
        self.widget = None
        self.raw_arrow = None
        self.image_arrow = None

    def move_time(self, travel_dir):
        """Beräknar tiden det tar för båten att resa genom rutan i vald riktning med nuvarande vind.
        Returnerar -1 om resan inte kunde genomföras (ex. motvind).
        """
        
        rel_wind_dir = abs(self.wind_dir - travel_dir)
        
        boat_speed = 0
        
        if (rel_wind_dir == 0): return -1
        elif (rel_wind_dir in (45, 315)):
            boat_speed = self.fart_med_bidevind()
        elif (rel_wind_dir in (90, 270)):
            boat_speed = self.fart_med_halvvind()
        elif (rel_wind_dir in (135, 225)):
            boat_speed = self.fart_med_slor()
        elif (rel_wind_dir == 180):
            boat_speed = self.fart_med_lans()

        if (boat_speed == 0): return -1

        distance = sqrt(2)
        if (travel_dir % 90 == 0): distance = 1

        return (distance / boat_speed)  # t = s / v


    # Dessa 4 metoder returnerar båtens hastighet med olika vindtyper (-riktningar).
    def fart_med_bidevind(self):
        k = 1 if 0 < self.wind_speed < 5 else 0
        return k * self.wind_speed
    
    def fart_med_halvvind(self):
        k = 0.5 if 0 < self.wind_speed < 7 else 0.25
        return k * self.wind_speed
    
    def fart_med_slor(self):
        return 0.3 * self.wind_speed
    
    def fart_med_lans(self):
        k = 0.25 if 0 < self.wind_speed < 9 else 0.5
        return k * self.wind_speed

if __name__ == '__main__':
    base.Controller()
