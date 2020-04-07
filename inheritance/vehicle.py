class Vehicle:
    def __init__(self):
        self.main_color = ""
        self.maximum_occupancy = 0

    def drive(self):
        print("Vroooom!")
    
    def turn(self, direction):
        print(f"The vehicle turned {direction}")
    
    def stop(self):
        print("The vehicle stopped")