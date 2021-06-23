#THIS FILE WAS SCRAPPED DURING THE PROJECT!
#IF YOU REALLY WANT TO USE THIS SECTION OF THE REPO, PLEASE USE THE UPDATED FILES!

#CONFIGURATION
import board;
import digitalio;
import sys;
import time;
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

keyboard = Keyboard(usb_hid.devices)
connector_pins = [board.GP0, board.GP1, board.GP2, board.GP3, board.GP4, board.GP5, board.GP6, board.GP7, board.GP8, board.GP9, board.GP10, board.GP11, board.GP12, board.GP13, board.GP14, board.GP15, board.GP16, board.GP17, board.GP18, board.GP19, board.GP20, board.GP21, board.GP22, board.GP26, board.GP27, board.GP28];

#KB HELPERS
def writeWord(word):
    #keyboard.send(Keycode.CONTROL, Keycode.LEFT_ARROW)
    for i, v in enumerate(word):
        if(RepresentsInt(v)):
            keyboard.send(getattr(Keycode, getIntAsWord(int(v))))
        elif (v == " "):
            keyboard.send(Keycode.SPACE)
        else:
            if(v.isupper()):
                keyboard.send(Keycode.SHIFT, getattr(Keycode, v))
            else:
                keyboard.send(getattr(Keycode, v))
    #keyboard.send(Keycode.TAB)
    #keyboard.send(Keycode.DOWN_ARROW)
    #keyboard.send(Keycode.BACKSPACE)
    keyboard.send(Keycode.ENTER)

def writePins(pin, secpin):
    pin = str(pin)
    pin = pin.replace("board.GP", "")

    secpin = str(secpin)
    secpin = secpin.replace("board.GP", "")
    writeWord(pin + " " + secpin)

def RepresentsInt(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


INT_WORDS = ["ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]
def getIntAsWord(int):
    return INT_WORDS[int]

# ---------- PIN HELPERS -----------
pins = {}

def setupPinIfNotAlready(pin):
    if ((str(pin) in pins) == False):
        pins[str(pin)] = digitalio.DigitalInOut(pin);
    else:
        return

def go_PULLUP(pin):
    setupPinIfNotAlready(pin)
    pins[str(pin)].direction = digitalio.Direction.INPUT
    pins[str(pin)].pull = digitalio.Pull.UP;

def go_GROUND(pin):
    setupPinIfNotAlready(pin)
    pins[str(pin)].direction = digitalio.Direction.OUTPUT
    pins[str(pin)].value = False

def is_GROUNDED(pin):
    return (pins[str(pin)].value == False)

# --------- Setup ----------
def setup():
    for val in connector_pins: #SETUP All Connector Pins as Pullup (High if Grounded)
        go_PULLUP(val)
    print("[INFO] To locate the Pins, that are shorted when Button is clicked, just Hold the Button until something appears here")
setup()
# --------- Loop -----------
def loop():
    Bottom_UP_TEST()
    Top_DOWN_TEST()

def Bottom_UP_TEST():
    #Bottom up Test
    i = 0
    while i < len(connector_pins): # Go through Pins
        go_GROUND(connector_pins[i])
        ii = i + 1 # Set next pin as Start Index for Inner Check

        while ii < len(connector_pins): # Go through all next Pins
            if (is_GROUNDED(connector_pins[ii])):
                writePins(connector_pins[i], connector_pins[ii]);
                print("SHORTED: " + str(connector_pins[i]) + " | " + str(connector_pins[ii]))
                while(is_GROUNDED(connector_pins[ii])):
                    time.sleep(0.1)
            ii+=1
        go_PULLUP(connector_pins[i])
        i+=1

def Top_DOWN_TEST():
    #Bottom up Test
    i = 0
    while i < len(connector_pins): # Go through Pins
        go_GROUND(connector_pins[i])
        ii = i - 1 # Set next pin as Start Index for Inner Check

        while ii > len(connector_pins): # Go through all next Pins
            if (is_GROUNDED(connector_pins[ii])):
                writePins(connector_pins[i], connector_pins[ii]);
                print("SHORTED: " + str(connector_pins[i]) + " | " + str(connector_pins[ii]))
                while(is_GROUNDED(connector_pins[ii])):
                    time.sleep(0.1)
                break
            ii-=1
        go_PULLUP(connector_pins[i])
        i+=1

while True:
    loop()
