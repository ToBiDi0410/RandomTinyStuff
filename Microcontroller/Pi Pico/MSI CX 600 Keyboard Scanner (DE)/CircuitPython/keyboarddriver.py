import maindriver as md
import time
import board
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

now = time.monotonic()
keys_pressed = 0

connector_pins = [board.GP0, board.GP1, board.GP2, board.GP3, board.GP4, board.GP5, board.GP6, board.GP7, board.GP8, board.GP9, board.GP10, board.GP11, board.GP12, board.GP13, board.GP14, board.GP15, board.GP16, board.GP17, board.GP18, board.GP19, board.GP20, board.GP21, board.GP22, board.GP26, board.GP27, board.GP28]
keyboard = Keyboard(usb_hid.devices)

keycodes = {'board.GP6|board.GP16': 'RIGHT_ARROW', 'board.GP19|board.GP0': 'P', 'board.GP18|board.GP0': 'O', 'board.GP19|board.GP2': '\xd6', 'board.GP19|board.GP5': '\xc4', 'board.GP19|board.GP4': '\xdc', 'board.GP19|board.GP7': 'ZERO', 'board.GP18|board.GP2': 'L', 'board.GP18|board.GP4': 'F7', 'board.GP18|board.GP7': 'NINE', 'board.GP5|board.GP17': 'F11', 'board.GP9|board.GP27_A1': '?', 'board.GP5|board.GP11': 'H', 'board.GP5|board.GP10': 'F4', 'board.GP5|board.GP13': 'F6', 'board.GP6|board.GP20': 'B', 'board.GP0|board.GP9': 'Q', 'board.GP19|board.GP6': 'FORWARD_SLASH', 'board.GP2|board.GP9': 'A', 'board.GP10|board.GP27_A1': 'F2', 'board.GP4|board.GP9': 'TAB', 'board.GP16|board.GP27_A1': 'INSERT', 'board.GP5|board.GP9': 'ESCAPE', 'board.GP14|board.GP27_A1': 'DELETE', 'board.GP28_A2|board.GP16': 'KEYPAD_FORWARD_SLASH', 'board.GP0|board.GP1': 'PAUSE', 'board.GP28_A2|board.GP14': 'KEYPAD_NUMLOCK', 'board.GP28_A2|board.GP15': 'KEYPAD_ASTERISK', 'board.GP28_A2|board.GP17': 'ENTER', 'board.GP7|board.GP9': 'ONE', 'board.GP28_A2|board.GP10': 'C', 'board.GP28_A2|board.GP11': 'M', 'board.GP18|board.GP27_A1': 'F8', 'board.GP3|board.GP0': 'SCROLL_LOCK', 'board.GP7|board.GP3': 'PRINT_SCREEN', 'board.GP7|board.GP1': 'F5', 'board.GP28_A2|board.GP13': 'COMMA', 'board.GP2|board.GP26_A0': 'RIGHT_SHIFT', 'board.GP5|board.GP12': 'UP_ARROW', 'board.GP4|board.GP26_A0': 'LEFT_SHIFT', 'board.GP0|board.GP10': 'E', 'board.GP0|board.GP11': 'U', 'board.GP0|board.GP12': 'KEYPAD_PLUS', 'board.GP0|board.GP13': 'I', 'board.GP7|board.GP20': 'FOUR', 'board.GP7|board.GP21': 'TWO', 'board.GP0|board.GP14': 'KEYPAD_SEVEN', 'board.GP0|board.GP16': 'KEYPAD_EIGHT', 'board.GP0|board.GP15': 'KEYPAD_NINE', 'board.GP4|board.GP14': 'KEYPAD_FOUR', 'board.GP4|board.GP15': 'KEYPAD_SIX', 'board.GP4|board.GP16': 'KEYPAD_FIVE', 'board.GP4|board.GP17': 'BACKSPACE', 'board.GP4|board.GP10': 'F3', 'board.GP4|board.GP13': '?', 'board.GP20|board.GP27_A1': 'FIVE', 'board.GP4|board.GP11': 'Y', 'board.GP4|board.GP8': 'APPLICATION', 'board.GP5|board.GP3': 'LEFT_ALT', 'board.GP12|board.GP27_A1': '?', 'board.GP5|board.GP14': 'SPACEBAR', 'board.GP6|board.GP3': 'RIGHT_ALT', 'board.GP18|board.GP6': '?', 'board.GP5|board.GP16': 'KEYPAD_ZERO', 'board.GP5|board.GP15': 'KEYPAD_PERIOD', 'board.GP7|board.GP17': 'F10', 'board.GP7|board.GP15': 'PAGE_DOWN', 'board.GP7|board.GP13': 'EIGHT', 'board.GP7|board.GP11': 'SEVEN', 'board.GP7|board.GP10': 'THREE', 'board.GP13|board.GP27_A1': '?', 'board.GP11|board.GP27_A1': 'SIX', 'board.GP17|board.GP27_A1': 'F9', 'board.GP15|board.GP27_A1': 'PAGE_UP', 'board.GP19|board.GP27_A1': '?', 'board.GP21|board.GP28_A2': 'X', 'board.GP20|board.GP28_A2': 'V', 'board.GP28_A2|board.GP9': 'Z', 'board.GP21|board.GP2': 'S', 'board.GP2|board.GP13': 'K', 'board.GP21|board.GP0': 'W', 'board.GP2|board.GP10': 'D', 'board.GP2|board.GP11': 'J', 'board.GP6|board.GP12': 'LEFT_ARROW', 'board.GP2|board.GP17': '?', 'board.GP1|board.GP28_A2': 'RIGHT_CONTROL', 'board.GP21|board.GP4': 'CAPS_LOCK', 'board.GP21|board.GP27_A1': 'F1', 'board.GP6|board.GP17': 'F12', 'board.GP20|board.GP0': 'R', 'board.GP20|board.GP4': 'T', 'board.GP6|board.GP15': 'KEYPAD_MINUS', 'board.GP20|board.GP2': 'F', 'board.GP20|board.GP5': 'G', 'board.GP6|board.GP11': 'N', 'board.GP18|board.GP28_A2': 'PERIOD', 'board.GP2|board.GP16': 'KEYPAD_TWO', 'board.GP2|board.GP15': 'KEYPAD_THREE', 'board.GP2|board.GP12': 'KEYPAD_ENTER', 'board.GP22|board.GP4': 'CONTROL', 'board.GP6|board.GP14': 'DOWN_ARROW'}

def getPinsStrings(pin1, pin2):
    return [str(pin1) + "|" + str(pin2), str(pin2) + "|" + str(pin1)]

def getKeyCodeByPins(pin1, pin2):
    for s in getPinsStrings(pin1, pin2):
        try:
            return keycodes[s]
        except:
            pass
    return ""

def eventCallback(name, pin):
    global keys_pressed
    try:
        pins = pin.split("|")
        ikeycode = getKeyCodeByPins(pins[0], pins[1])
        if(ikeycode == ""):
            print("[WARN] Unidentified Keycodes: " + pin)
            return

        if(hasattr(Keycode, ikeycode) is False):
            print("[WARN] Keycode not valid: " + ikeycode)
            return

        if name == "press":
            keyboard.press(getattr(Keycode, ikeycode))
            return
        elif name == "release":
            keyboard.release(getattr(Keycode, ikeycode))
            return
        else:
            print("[WARN] Unidentified Event from Main-Driver: " + name)
    except:
        print("[ERR] Could not Process Event: " + str(name) + "(" + str(pin) + ")")

def setup():
    md.setup(connector_pins, eventCallback)

def loop():
    global now, keys_pressed
    md.loop()
    took = (time.monotonic() - now)*1000
    print((took,))
    now = time.monotonic()
    return

setup()
while True:
    loop()
