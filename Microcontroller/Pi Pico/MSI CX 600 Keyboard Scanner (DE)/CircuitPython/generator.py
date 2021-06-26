import maindriver as md
import board
import time

connector_pins = [board.GP0, board.GP1, board.GP2, board.GP3, board.GP4, board.GP5, board.GP6, board.GP7, board.GP8, board.GP9, board.GP10, board.GP11, board.GP12, board.GP13, board.GP14, board.GP15, board.GP16, board.GP17, board.GP18, board.GP19, board.GP20, board.GP21, board.GP22, board.GP26, board.GP27, board.GP28];

KEYS = ["ESCAPE", "F1", "F2", "F3", "F4", "F5", "F6", "F7", "F8", "F9", "F10", "F11", "F12", "PRINT_SCREEN", "SCROLL_LOCK", "PAUSE", "INSERT", "DELETE", "PAGE_UP", "PAGE_DOWN",
        "?", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE", "ZERO", "?", "?", "BACKSPACE", "KEYPAD_NUMLOCK", "KEYPAD_FORWARD_SLASH", "KEYPAD_ASTERISK", "KEYPAD_MINUS",
        "TAB", "Q", "W", "E", "R", "T", "Z", "U", "I", "O", "P", "Ü", "?", "?", "KEYPAD_SEVEN", "KEYPAD_EIGHT", "KEYPAD_NINE", "KEYPAD_PLUS",
        "CAPS_LOCK", "A", "S", "D", "F", "G", "H", "J", "K", "L", "Ö", "Ä", "ENTER", "KEYPAD_FOUR", "KEYPAD_FIVE", "KEYPAD_SIX",
        "LEFT_SHIFT", "Y", "X", "C", "V", "B", "N", "M", "COMMA", "PERIOD", "FORWARD_SLASH", "RIGHT_SHIFT", "UP_ARROW" "KEYPAD_ONE", "KEYPAD_TWO", "KEYPAD_THREE", "KEYPAD_ENTER",
        "CONTROL", "APPLICATION", "LEFT_ALT", "?", "SPACEBAR", "RIGHT_ALT", "?", "RIGHT_CONTROL", "LEFT_ARROW", "DOWN_ARROW", "RIGHT_ARROW", "KEYPAD_ZERO", "KEYPAD_PERIOD"
]

LAST_KEY = ""

INDEXED_KEYS = {}

def eventCallback(name, pin):
    global LAST_KEY
    try:
        if(name == "press"):
            LAST_KEY = pin
    except:
        print("[ERR] Could not Process Event: " + str(name) + "(" + str(pin) + ")")

def getPinsStrings(pin1, pin2):
    return [str(pin1) + "|" + str(pin2), str(pin2) + "|" + str(pin1)]

def setup():
    global KEYS, LAST_KEY
    md.setup(connector_pins, eventCallback)

    while len(KEYS) > 0:
        ASK = KEYS[0]
        print("Please enter: " + ASK)
        LAST_KEY = ""
        while LAST_KEY == "":
            md.loop()
        INDEXED_KEYS[LAST_KEY] = ASK;
        KEYS.pop(0)

    print("------------ [!] ------------")
    print("All keys Identified! Please paste this into 'keyboarddriver.py'")
    print("")
    print("keycodes = " + str(INDEXED_KEYS))
    print("")
    print("------------ [!] ------------")
    time.sleep(1000)

setup()
