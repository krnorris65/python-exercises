class City:
    def __init__(self, name):
        self.name = name
        self.mayor = ""
        self.year_established = ""
        self.buildings = list()
    
    def add_building(self, building):
        self.buildings.append(building)