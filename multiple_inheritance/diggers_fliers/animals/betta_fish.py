from movements import ISwim

class BettaFish(ISwim):
    def __init__(self):
        ISwim.__init__(self)
        self.maximum_depth = 5

    def __str__(self):
        return "Betta Fish"