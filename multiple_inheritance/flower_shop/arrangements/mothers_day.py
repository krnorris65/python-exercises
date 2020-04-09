from .arrangement import Arrangement
from attributes import IOrganic

class MothersDay(Arrangement):

    def __init__(self):
        super().__init__()
        self.stem_height = 4

# daisies, baby's breath, and poppies
    def enhance(self, flower):
        if isinstance(flower, IOrganic):
            self._Arrangement__flowers.append(flower)
        else:
            print(f"{flower} cannot be added to a Mother's Day Arrangement")