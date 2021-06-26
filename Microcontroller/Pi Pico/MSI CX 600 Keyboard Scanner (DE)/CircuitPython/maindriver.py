# MAIN DRIVER FOR PI KEYBOARD SCANNER
import digitalio
import time

pins = {}
time_repeat = 0.5
short_first_callbacks = []
short_stay_callbacks = []
currently_pressed = []

def setAllPinsToPullup():
    for PIN_NAME, PIN_OBJ in pins.items():  # SETUP All Connector Pins as Pullup (High if Grounded)
        go_PULLUP(PIN_OBJ)

def go_PULLUP(pin):
    pin.direction = digitalio.Direction.INPUT
    pin.pull = digitalio.Pull.UP

def go_GROUND(pin):
    pin.direction = digitalio.Direction.OUTPUT
    pin.value = False

def is_GROUNDED(pin):
    return (pin.value is False)

def setup(newpins, event_callbacke):
    global event_callback
    print("[DRIVER] Setting up Pins as I/O...")
    for val in newpins:
        pins[str(val)] = digitalio.DigitalInOut(val)
    print("[DRIVER] Turning all Pins to Pullup Inputs...")
    setAllPinsToPullup()
    print("[DRIVER] Pins setup (" + str(len(pins)) + ")!")
    print("[DRIVER] Registering Callbacks..")
    event_callback = event_callbacke
    print("[DRIVER] Setup done!")
    time.sleep(1)

def loop():
    global currently_pressed
    new_currently_pressed = getShortedPins()
    for v in currently_pressed:
        if (v not in new_currently_pressed):
            newEvent("release", v)

    for v in new_currently_pressed:
        if (v not in currently_pressed):
            newEvent("press", v)

    currently_pressed = new_currently_pressed

def newEvent(name, value):
    event_callback(name, value)


def getShortedPins():
    shortedPins = []
    pinslist = list(pins)
    i = 0
    while i < len(pins):  # Go through Pins
        PIN1 = pins[pinslist[i]]
        go_GROUND(PIN1)
        ii = i + 1

        while ii < len(pins):
            if ii != i:
                PIN2 = pins[pinslist[ii]]
                if (is_GROUNDED(PIN2)):
                    combinations = [(pinslist[i] + "|" + pinslist[ii]), (pinslist[ii] + "|" + pinslist[i])]
                    if(arrayContainsOneOf(combinations, shortedPins) is False):
                        shortedPins.append(combinations[0])
            ii += 1

        go_PULLUP(PIN1)
        i += 1
    return shortedPins

def arrayContainsOneOf(checkarray, array):
    for val in array:
        if(val in checkarray):
            return True
    return False
