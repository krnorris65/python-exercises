from flowers import Rose, Daisy, Alstroemeria, Lily, Poppy, BabysBreath
from arrangements import Arrangement, ValentinesDay, MothersDay

rose = Rose()
daisy = Daisy()
poppy = Poppy()



vday = ValentinesDay()
mothers_day = MothersDay()

mothers_day.enhance(daisy)
mothers_day.enhance(rose)

vday.enhance(poppy)

