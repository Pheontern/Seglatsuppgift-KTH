import graphics
from sea import Sea
from sailboat import Sailboat

class Controller:
    """Controller-klassen hanterar hela programmet och skapar de mest grundläggande komponenterna."""
    
    def __init__(self):
        """Initierar klassen med nya objekt för havet, segelbåten och det grafiska gränssnittet."""
        
        self.sea = Sea("./havsmatris.utf8")
        
        self.sailboat = Sailboat(self)
        
        self.gui = graphics.Graphics(self)
        
if __name__ == '__main__':
    Controller()
