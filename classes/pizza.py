class Pizza:
    def __init__(self):
        self.size = ""
        self.style = ""
        self.toppings = []

    def add_topping(self, topping):
        self.toppings.append(topping)

    def print_order(self):
        topping_list = " and ".join(self.toppings)
        print(f"I would like a {self.size}-inch, {self.style} pizza with {topping_list}")

meat_lovers = Pizza()
meat_lovers.size = 16
meat_lovers.style = "Deep dish"
meat_lovers.add_topping("Pepperoni")
meat_lovers.add_topping("Olives")
meat_lovers.print_order()

veggie = Pizza()
veggie.size = 12
veggie.style = "thin crust"
veggie.add_topping("Peppers")
veggie.add_topping("Tomato")
veggie.print_order()