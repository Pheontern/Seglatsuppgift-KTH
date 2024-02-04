import base
import functools
import time

class Sailboat:
    """Sailboat-klassen hanterar allt som krävs för rekursionsberäkningarna."""
    
    def __init__(self, controller):
        """Initierar konstruktorns parametrar, d.v.s. ger tillgång till controller-objektet."""
        
        self.controller = controller
        self.t0 = None

    def start_measuring(self):
        """Startar mätningarna/beräkningarna 
        och returnerar resultatet som en dictionary alternativt en string med felmeddelande.
        """
        
        goal_square = self.controller.sea.get_square(type="goal")
        start_square = self.controller.sea.get_square(type="start")
        
        try:
            self.t0 = time.time()
            result = self.recursive_move(start_square, goal_square, (), 0)
            t1 = time.time()

            if (result["time"] == -1):
                raise Exception("No path found.")
            
            result["path"] = list(result["path"])
            result["path"].append(goal_square)
            result["calc_time"] = t1 - self.t0

            return result
        except Exception as error:
            return str(error)

    @functools.lru_cache(maxsize=None)
    def possible_moves(self, square):
        """Beräknar alla möjliga rutor att förflytta sig till från en viss ruta 'square' 
        samt tiden varje förflyttning tar. En lista med tuples av SeaSquare-objekt och tider returneras.
        Möjliga förflyttningar baseras här enbart på vindriktning och begränsningar av matrisens storlek.
        Metoden är separat från 'recursive_move' för att resultatet ska kunna cachas.
        """
        
        possible_moves = []
        travel_dirs = [(0, 1, 0), (1, 1, 45), (1, 0, 90), (1, -1, 135), (0, -1, 180), (-1, -1, 225), (-1, 0, 270), (-1, 1, 315)]
        
        for travel_dir in travel_dirs:
            time = square.move_time(travel_dir[2])

            if (time != -1):
                x = square.x + travel_dir[0]
                y = square.y - travel_dir[1]  # Minustecken eftersom index minskar när man rör sig uppåt i 2D-listan.

                if (0 <= x < self.controller.sea.width and 0 <= y < self.controller.sea.height):
                    next_square = self.controller.sea.matrix[y][x]
                    possible_moves.append((next_square, time))
        return possible_moves
    
    def recursive_move(self, square, goal, passed_squares, current_time = 0, best_time = -1, best_path = ()):
        """Rekursiv metod som systematiskt testar alla* vägar mellan start och mål för att komma fram till
        den optimala rutten för segelbåten. *Vissa optimeringar har implementerats, exempelvis avbryts alla 
        rutter så fort de tagit längre tid än den nuvarande bästa tiden.

        Vid avslutad rekursion returneras den bästa tiden och vägen som hittades eller ett felmeddelande om 
        beräkningarna tog för lång tid.
        """
        
        if (current_time > best_time and best_time != -1):
            return {"time": best_time, "path": best_path}
        elif (square is goal):
            return {"time": current_time, "path": passed_squares}
        elif (time.time() - self.t0 > 60):
            raise Exception("Execution took over 60 seconds, aborted.")
        
        possible_moves = self.possible_moves(square)
        
        # Den här kodraden sorterar listan med möjliga förflyttningar efter ett tillräckligt noggrant mått på avstånd till målet.
        # Det minskar risken att programmet hamnar i att testa många vägar utan att ha hittat en enda.
        # Om det sker hittas ingen bastid att förhålla sig till (se * från docstringen) 
        # och alla vägar som testas blir långa och komplexa.
        list.sort(possible_moves, key=lambda move: abs(move[0].x - goal.x) + abs(move[0].y - goal.y))

        for square_and_time in possible_moves:
            if (square_and_time[0] not in passed_squares):

                new_passed_squares = passed_squares + (square,)
                new_current_time = current_time + square_and_time[1]
                            
                result = self.recursive_move(square_and_time[0], goal, new_passed_squares, new_current_time, best_time, best_path) #Rekursivt anrop
                best_time = result["time"]
                best_path = result["path"]
                
        return {"time": best_time, "path": best_path}

if __name__ == '__main__':
    base.Controller()
