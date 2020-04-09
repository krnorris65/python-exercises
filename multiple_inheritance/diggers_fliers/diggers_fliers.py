from animals import Ant, BettaFish, CopperheadSnake, Earthworm, Finch, Gerbil, Mouse, Parakeet, Terrapin, TimberRattlesnake
from containers import Diggers, Movers, Swimmers, Fliers

ant = Ant()
betta= BettaFish()
copperhead= CopperheadSnake()
worm = Earthworm()
finch = Finch()
gerbil = Gerbil()
mouse = Mouse()
parakeet = Parakeet()
terrapin = Terrapin()
timber = TimberRattlesnake()

diggers = Diggers()
movers = Movers()
swimmers = Swimmers()
fliers = Fliers()


diggers.add_animal(ant) 
swimmers.add_animal(betta)
movers.add_animal(copperhead)
diggers.add_animal(worm) 
fliers.add_animal(finch) 
movers.add_animal(gerbil) 
movers.add_animal(mouse) 
fliers.add_animal(parakeet) 
movers.add_animal(terrapin) 
movers.add_animal(timber) 
