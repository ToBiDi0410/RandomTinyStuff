import maindriver as md
import board
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

connector_pins = [board.GP0, board.GP1, board.GP2, board.GP3, board.GP4, board.GP5, board.GP6, board.GP7, board.GP8, board.GP9, board.GP10, board.GP11, board.GP12, board.GP13, board.GP14, board.GP15, board.GP16, board.GP17, board.GP18, board.GP19, board.GP20, board.GP21, board.GP22, board.GP26, board.GP27, board.GP28];
keycodes = {'board.GP21|board.GP2': "BACKSPACE", 'board.GP22|board.GP4': 'SPACE', 'board.GP28_A2|board.GP13': 'W', 'board.GP4|board.GP15': 'G', 'board.GP4|board.GP16': 'H', 'board.GP3|board.GP16': 'J', 'board.GP3|board.GP14': 'D', 'board.GP20|board.GP3': 'K', 'board.GP20|board.GP28_A2': 'I', 'board.GP19|board.GP3': 'L', 'board.GP3|board.GP17': '\xd6', 'board.GP4|board.GP17': '\xc4', 'board.GP3|board.GP13': 'S', 'board.GP3|board.GP12': 'A', 'board.GP2|board.GP15': 'T', 'board.GP3|board.GP15': 'F', 'board.GP5|board.GP13': 'X', 'board.GP5|board.GP12': 'Z', 'board.GP19|board.GP28_A2': 'O', 'board.GP5|board.GP14': 'C', 'board.GP5|board.GP15': 'V', 'board.GP6|board.GP15': 'B', 'board.GP6|board.GP16': 'N', 'board.GP2|board.GP16': 'Y', 'board.GP2|board.GP17': '\xdc', 'board.GP5|board.GP16': 'M', 'board.GP28_A2|board.GP16': 'U', 'board.GP28_A2|board.GP17': 'P', 'board.GP28_A2|board.GP14': 'E', 'board.GP28_A2|board.GP15': 'R', 'board.GP28_A2|board.GP12': 'Q'}
keyboard = Keyboard(usb_hid.devices)

def firstShortCallback(pin1, pin2):
    ikeycode = getKeyCodeByPins(pin1,pin2)
    if(ikeycode == ""):
        print("[WARN] Unidentified Keycodes: " + str(getPinsStrings(pin1,pin2)))
    else:
        keyboard.send(getattr(Keycode, ikeycode))
        print("[INPUT] Key fired: " + ikeycode)

def getPinsStrings(pin1, pin2):
    return [str(pin1) + "|" + str(pin2), str(pin2) + "|" + str(pin1)]

def getKeyCodeByPins(pin1, pin2):
    for s in getPinsStrings(pin1, pin2):
        try:
            return keycodes[s]
        except:
            pass
    return ""

def stayShortCallback(pin1, pin2):
    print("STAY!")

def setup():
    md.setup(connector_pins, [firstShortCallback], [stayShortCallback])

def loop():
    md.loop()

setup()
while True:
    loop()
