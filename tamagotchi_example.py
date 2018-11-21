from sense_hat import SenseHat
import time
import random

s = SenseHat()
#s.low_light = True

red = 0
blue = 0
green = 255;
foreground = (red, green, blue)
background = (0, 0, 0)
minimum = -20
maximum = 20

def change_random_color():
    global red
    global green
    global blue
    color_number = random.randint(1,3) # random number between 1 and 3
    if color_number == 1: red = clamp(red + random.randint(minimum, maximum), 0, 255)
    elif color_number == 2: green = clamp(green + random.randint(minimum, maximum), 0, 255)
    else: blue = clamp(blue + random.randint(minimum, maximum), 0, 255)

def clamp(n, smallest, largest): return max(smallest, min(n, largest))

def tamagotchi_face():
    B = background
    F = foreground
    image = [ 
    B, B, B, B, B, B, B, B,
    B, F, F, B, B, F, F, B,
    B, B, F, B, B, F, B, B,
    B, B, B, B, B, B, B, B,
    B, F, B, F, F, B, F, B,
    B, F, B, B, B, B, F, B,
    B, B, F, F, F, F, B, B,
    B, B, B, B, B, B, B, B,
    ]
    return image

s.set_pixels(tamagotchi_face())

while True:
  change_random_color()
  foreground= (red,green,blue)
  s.set_pixels(tamagotchi_face())
  time.sleep(0.05)

#images = [trinket_logo, trinket_logo, plus, raspi_logo, raspi_logo, equals, heart, heart]
#count = 0

#while True: 
#    s.set_pixels(images[count % len(images)]())
#    time.sleep(.75)
#    count += 1
