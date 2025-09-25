# Paste this exactly into MakeCode (micro:bit) Python editor

from microbit import *

# show "Hello!" once, then blink a heart on the LED display
display.scroll("Hello!")
while True:
    display.show(Image.HEART)
    sleep(500)
    display.show(Image.HEART_SMALL)
    sleep(500)
