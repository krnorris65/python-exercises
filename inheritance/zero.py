from vehicle import Vehicle

class Zero(Vehicle):
    def __init__(self):
        self.battery_kwh = 0
    
    def drive(self):
        print(f"The {self.main_color} Zero zips past. Yeeeeooowww!")