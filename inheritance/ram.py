from vehicle import Vehicle

class Ram(Vehicle):
    def __init__(self):
        self.fuel_capacity = 0
    
    def drive(self):
        print(f"The {self.main_color} Ram growls past. Rrrrrrumble!")
