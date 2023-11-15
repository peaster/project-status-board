import time
from lighting-controller import LightingController 

controller = LightingController(0.17)
while True:
    controller.updateLights();
    sleep(60)
