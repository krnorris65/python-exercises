from vehicle import Vehicle

class Tesla(Vehicle):
    def __init__(self):
        super().__init__()
        self.battery_kwh = 0

    def drive(self):
        print(f"The {self.main_color} Tesla blazes past. MMmmmmmmmmmm!")

    def turn(self, direction):
        print(f"The {self.main_color} Tesla squeals around a {direction} turn")

    def stop(self):
        print(f"The {self.main_color} Tesla silently stops as if it never moved")
