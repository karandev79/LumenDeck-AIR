import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.encoder import EncoderHandler
from kmk.modules.media_keys import MediaKeys

keyboard = KMKKeyboard()

keyboard.col_pins = (board.D0, board.D1)
keyboard.row_pins = (board.D2, board.D3)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

keyboard.modules.append(MediaKeys())

encoder_handler = EncoderHandler()
encoder_handler.pins = (
    (board.D4, board.D5, None),
)
encoder_handler.map = [
    (
        (KC.VOLD, KC.VOLU),
    )
]
keyboard.modules.append(encoder_handler)

SNAP = KC.LGUI(KC.LSFT(KC.S))

keyboard.keymap = [
    [
        KC.COPY,  KC.PASTE,
        KC.UNDO,  SNAP,
    ]
]

if __name__ == '__main__':
    keyboard.go()