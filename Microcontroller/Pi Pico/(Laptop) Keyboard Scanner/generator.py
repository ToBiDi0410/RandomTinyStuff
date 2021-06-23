import maindriver as md
import board
import time

connector_pins = [board.GP0, board.GP1, board.GP2, board.GP3, board.GP4, board.GP5, board.GP6, board.GP7, board.GP8, board.GP9, board.GP10, board.GP11, board.GP12, board.GP13, board.GP14, board.GP15, board.GP16, board.GP17, board.GP18, board.GP19, board.GP20, board.GP21, board.GP22, board.GP26, board.GP27, board.GP28];

KEYS = ["Q", "W", "E", "R", "T", "Z", "U", "I", "O", "P", "Ü", "A", "S", "D", "F", "G", "H", "J", "K", "L", "Ö", "Ä", "Y", "X", "C", "V", "B", "N", "M"]
LAST_KEY = ""

INDEXED_KEYS = {}

def firstShortCallback(pin1, pin2):
    global LAST_KEY
    LAST_KEY = getPinsStrings(pin1,pin2)[0]

def getPinsStrings(pin1, pin2):
    return [str(pin1) + "|" + str(pin2), str(pin2) + "|" + str(pin1)]

def stayShortCallback(pin1, pin2):
    return;

def setup():
    global KEYS, LAST_KEY
    md.setup(connector_pins, [firstShortCallback], [stayShortCallback])

    while len(KEYS) > 0:
        ASK = KEYS[0]
        print("Please enter: " + ASK)
        LAST_KEY = ""
        while LAST_KEY == "":
            md.loop()
        INDEXED_KEYS[LAST_KEY] = ASK;
        KEYS.pop(0)

    print("------------ [!] ------------")
    print("All keys Identified! Please paste this into 'driver.py'")
    print("")
    print("keycodes = " + str(INDEXED_KEYS))
    print("")
    print("------------ [!] ------------")
    time.sleep(1000)

setup()
