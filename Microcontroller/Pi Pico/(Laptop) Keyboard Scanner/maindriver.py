# MAIN DRIVER FOR PI KEYBOARD SCANNER
import board
import digitalio
import time

pins = {}
time_repeat = 0.5
short_first_callbacks = [];
short_stay_callbacks = [];

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
    return (pin.value == False)

def setup(newpins, short_first_callbackse, short_stay_callbackse):
    global short_first_callbacks, short_stay_callbacks
    print("[DRIVER] Setting up Pins as I/O...")
    for val in newpins:
        pins[str(val)] = digitalio.DigitalInOut(val)
    print("[DRIVER] Turning all Pins to Pullup Inputs...")
    setAllPinsToPullup()
    print("[DRIVER] Pins setup (" + str(len(pins)) + ")!")
    print("[DRIVER] Registering Callbacks..")
    short_first_callbacks = short_first_callbackse
    short_stay_callbacks = short_stay_callbackse
    print("[DRIVER] Setup done!")
    time.sleep(1)

def loop():
    Bottom_UP_TEST()
    #Top_DOWN_TEST()

def Bottom_UP_TEST():
    #Bottom Up Test
    i = 0
    while i < len(pins): # Go through Pins
        PIN1 = pins[list(pins)[i]]
        go_GROUND(PIN1)

        ii = i + 1 # Set last pin as Start Index for Outer Check

        while ii < len(pins): # Go through all next Pins
            PIN2 = pins[list(pins)[ii]];
            if (is_GROUNDED(PIN2)):
                firstShort(list(pins)[i],list(pins)[ii])
                t_passed = 0;
                while(is_GROUNDED(PIN2)):
                    time.sleep(0.1)
                    if(t_passed > time_repeat):
                        shortStay(list(pins)[i],list(pins)[ii])
                        t_passed = 0;
                    t_passed+= 0.1
                break
            ii+=1

        go_PULLUP(PIN1)
        i+=1

def Top_DOWN_TEST():
    #Top down Test
    i = 0
    while i < len(pins): # Go through Pins
        PIN1 = pins[list(pins)[i]]
        go_GROUND(PIN1)

        ii = i - 1 # Set last pin as Start Index for Outer Check

        while ii > 0: # Go through all next Pins
            PIN2 = pins[list(pins)[ii]];
            if (is_GROUNDED(PIN2)):
                firstShort(list(pins)[i],list(pins)[ii])
                while(is_GROUNDED(PIN2)):
                    time.sleep(0.1)
                    t_passed = 0
                    if(t_passed > time_repeat):
                        shortStay(list(pins)[i], list(pins)[ii])
                        t_passed = 0;
                    t_passed+= 0.1
                break
            ii-=1

        go_PULLUP(PIN1)
        i+=1

def firstShort(pin1, pin2):
    #print(short_first_callback)
    for val in short_first_callbacks:
        val(pin1, pin2)
    #print("SHORT at: " + str(pin1) + " | " + str(pin2))

def shortStay(pin1, pin2):
    #print(short_stay_callback)
    for val in short_stay_callbacks:
        val(pin1, pin2)
    #print("Please stop the Short at: " + str(pin1) + " | " + str(pin2))
