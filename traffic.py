from itertools import cycle
import time

colors = cycle(['red', 'green', 'yellow'])
for color in colors:
    print(color)
    time.sleep(2)