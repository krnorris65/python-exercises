from vehicle import Vehicle

class Cessna(Vehicle):
    def __init__(self):
        self.fuel_capacity = 0

    def drive(self):
        print(f"The {self.main_color} Cessna flashes past. Zoooooom!")


    def stop(self):
        print(f"The {self.main_color} Cessna rolls to a stop after rolling a mile down the runway")
