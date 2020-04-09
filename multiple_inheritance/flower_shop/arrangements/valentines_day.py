from .arrangement import Arrangement
from attributes import INotOrganic


class ValentinesDay(Arrangement):
    def __init__(self):
        super().__init__()
        self.stem_height = 7
    
    # Override the `enhance` method to ensure only
    # roses, lillies, and alstroemeria can be added
    def enhance(self, flower):
        if isinstance(flower, INotOrganic):
            self._Arrangement__flowers.append(flower)
        else:
            print(f"{flower} cannot be added to a Valentine's Day Arrangement")
