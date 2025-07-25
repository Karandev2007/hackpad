import board
import busio
import adafruit_ssd1306

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners.keypad import KeysScanner
from kmk.modules.macros import Press, Release, Tap, Macros
from kmk.modules.encoder import EncoderHandler
from kmk.scanners import DiodeOrientation

keyboard = KMKKeyboard()
i2c = busio.I2C(board.SCL, board.SDA)

macros = Macros()
encoder_handler = EncoderHandler()
display = adafruit_ssd1306.SSD1306_I2C(128, 32, i2c)

keyboard.modules.append(encoder_handler)
keyboard.modules.append(macros)

keyboard.col_pins = (board.D3, board.D2, board.D1, board.D0)
keyboard.row_pins = (board.D10, board.D9, board.D8)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

encoder_handler.pins = ((board.D6, board.D10, None))

keyboard.keymap = [
  [
    KC.SLEEP,
    KC.LGUI(KC.L),
    KC.LGUI(KC.D),
    KC.MUTE,
    KC.Macro(Press(KC.LCTRL), Tap(KC.W), Release(KC.LCTRL)),
    KC.Macro(Press(KC.LCTRL), Tap(KC.W), Release(KC.LCTRL)),
    KC.MPRV,
    KC.MPLY,
    KC.VOLU,
    KC.VOLD,
    KC.MNXT
  ]
]

encoder_handler.map = [
  [
    KC.VOLU, KC.VOLD
  ]
]

display.fill(0)

display.show()

display.text('ASTRA DECK', 0, 0, 1)
display.show()

if __name__ == '__main__':
    keyboard.go()