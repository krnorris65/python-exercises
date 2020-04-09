from movements import IMove

class TimberRattlesnake(IMove):
    def __init__(self):
        IMove.__init__(self)

    def __str__(self):
        return "Timber Rattlesnake"