import datetime

class Building:
    def __init__(self, address, stories):
        self.designer = "Kristen Norris"
        self.date_constructed = ""
        self.owner = ""
        self.address = address
        self.stories = stories
    
    def construct(self):
        self.date_constructed = datetime.datetime.now()
    
    def purchase(self, owner):
        self.owner = owner

# Create 5 building instances
building_one = Building("1 Main St", 3)
building_two = Building("2 Main St", 5)
building_three = Building("3 Main St", 1)
building_four = Building("4 Main St", 2)
building_five = Building("5 Main St", 3)

# Have each one get purchased by a real estate magnate
building_one.purchase("Bob Jones")
building_two.purchase("Ann Jackson")
building_three.purchase("Bob Jones")
building_four.purchase("Ann Jackson")
building_five.purchase("Alan Brown")

# After purchased, construct each one
building_one.construct()
building_two.construct()
building_three.construct()
building_four.construct()
building_five.construct()

# Once all building are purchased and constructed, print the address, owner, stories, and date constructed to the terminal for each one. 
print(f"{building_one.address} was purchased by {building_one.owner} on {building_one.date_constructed} and has {building_one.stories} stories.")

print(f"{building_two.address} was purchased by {building_two.owner} on {building_two.date_constructed} and has {building_two.stories} stories.")

print(f"{building_three.address} was purchased by {building_three.owner} on {building_three.date_constructed} and has {building_three.stories} stories.")

print(f"{building_four.address} was purchased by {building_four.owner} on {building_four.date_constructed} and has {building_four.stories} stories.")

print(f"{building_five.address} was purchased by {building_five.owner} on {building_five.date_constructed} and has {building_five.stories} stories.")