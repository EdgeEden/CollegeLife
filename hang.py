import pynput
import time
control = pynput.mouse.Controller()
n = 1
while True:
    n = n+1
    pos1 = control.position
    control.move(10*(-1)**n, 10*(-1)**n)
    time.sleep(2)
    pos2 = control.position
    if abs(pos2[0]-pos1[0]) > 100 | abs(pos2[1]-pos1[1]) > 100:
        break
