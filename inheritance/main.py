from zero import Zero
from cessna import Cessna
from ram import Ram
from tesla import Tesla

fxs = Zero()
fxs.main_color = "red"
fxs.drive()
fxs.turn("right")
fxs.stop()

modelS = Tesla()
modelS.main_color = "green"
modelS.drive()
modelS.turn("left")
modelS.stop()

mx410 = Cessna()
mx410.main_color = "white"
mx410.drive()
mx410.turn("right")
mx410.stop()

ram1500 = Ram()
ram1500.main_color = "orange"
ram1500.drive()
ram1500.turn("left")
ram1500.stop()
