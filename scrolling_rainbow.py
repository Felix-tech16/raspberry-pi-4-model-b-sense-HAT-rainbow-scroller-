import time
from sense_hat import SenseHat

sense = SenseHat()

colors = [
    [255, 0, 0],      # red
    [255, 100, 0],    # orange
    [255, 255, 0],    # yellow
    [0, 255, 0],      # green
    [0, 150, 255],    # light blue
    [0, 0, 255],      # blue
    [150, 0, 255],    # violet
]

offset = 0

try:
    while True:
        pixels = []

        for y in range(8):
            for x in range(8):
                pixels.append(colors[(x + offset) % len(colors)])

        sense.set_pixels(pixels)
        offset += 1
        time.sleep(0.1)

except KeyboardInterrupt:
    pass
finally:
    sense.clear()
