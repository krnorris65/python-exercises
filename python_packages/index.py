from appliances import CoffeeMaker, DishWasher, Refrigerator, Dryer, Washer, Stove, CanOpener


whirlpool_dishwasher = DishWasher("black")
whirlpool_dishwasher.wash_dishes()

samsung_washer = Washer("red", "normal")
samsung_dryer = Dryer("red", "gas")

lg_fridge = Refrigerator("stainless")
lg_fridge.make_ice()

mr_coffee = CoffeeMaker("white")
mr_coffee.make_coffee()

can = CanOpener("Green")
can.open_can()