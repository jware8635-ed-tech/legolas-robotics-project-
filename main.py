# Microsoft MakeCode (Python-only mode) demo
# LEGOLAS Robot Project - Dropdowns and Toggles Example

from microbit import *

# Dropdown simulated with Enum
class RobotMode:
    LINE_FOLLOW = 0
    OBJECT_AVOID = 1
    DANCE = 2
    MANUAL = 3

# Default selections
mode = RobotMode.LINE_FOLLOW   # Dropdown starts at "Line Follow"
camera_on = False              # Toggle OFF
sensor_on = True               # Toggle ON

def show_config():
    display.scroll("Mode:" + str(mode))
    display.scroll("Camera:" + ("ON" if camera_on else "OFF"))
    display.scroll("Sensor:" + ("ON" if sensor_on else "OFF"))

# Demo loop
while True:
    if button_a.is_pressed():       # A cycles through dropdown modes
        mode = (mode + 1) % 4
        show_config()
        sleep(500)
    if button_b.is_pressed():       # B toggles camera ON/OFF
        global camera_on
        camera_on = not camera_on
        show_config()
        sleep(500)
