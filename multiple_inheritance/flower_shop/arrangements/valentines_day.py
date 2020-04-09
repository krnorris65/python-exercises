from .arrangement import Arrangement


class ValentinesDay(Arrangement):
    def __init__(self):
        super().__init__()
    
    # Override the `enhance` method to ensure only
    # roses, lillies, and alstroemeria can be added
