"""
KMK Firmware for Custom Macropad
Board: Seeed Studio XIAO RP2040
Matrix: 2 rows × 3 columns (4 switches + 1 encoder button + 1 empty)
Features: Rotary Encoder, OLED Display, RGB LEDs (2x WS2812B)
"""

import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.extensions.peg_oled_display import Oled, OledDisplayMode, OledReactionType, OledData
from kmk.modules.encoder import EncoderHandler
from kmk.extensions.rgb import RGB, AnimationModes

# ========================================
# INITIALIZE KEYBOARD
# ========================================
keyboard = KMKKeyboard()

# ========================================
# PIN CONFIGURATION
# ========================================
# Matrix pins
keyboard.col_pins = (board.D1, board.D0, board.D9)  # COL1, COL2, COL3
keyboard.row_pins = (board.D3, board.D2)             # ROW1, ROW2
keyboard.diode_orientation = DiodeOrientation.COL2ROW

# ========================================
# RGB LED CONFIGURATION
# ========================================
# Your macropad has 2 WS2812B RGB LEDs
rgb = RGB(
    pixel_pin=board.D6,                      # RGB data pin (change to D10 if D6 doesn't work)
    num_pixels=2,                            # You have 2 RGB LEDs
    animation_mode=AnimationModes.BREATHING, # Default: breathing effect
    hue_default=170,                         # Default color: Blue (0=Red, 85=Green, 170=Blue)
    sat_default=255,                         # Full saturation (vivid color)
    val_default=50,                          # Brightness (0 255, starting low)
    animation_speed=1,                       # Animation speed
)
keyboard.extensions.append(rgb)

# ========================================
# ROTARY ENCODER CONFIGURATION
# ========================================
encoder_handler = EncoderHandler()
keyboard.modules.append(encoder_handler)
encoder_handler.pins = (
    (board.D8, board.D7, None),  # A=D8, B=D7, Button=in matrix
)

# ========================================
# OLED DISPLAY CONFIGURATION
# ========================================
oled_ext = Oled(
    OledData(
        corner_one={0: OledReactionType.STATIC, 1: ["DaVinci"]},
        corner_two={0: OledReactionType.LAYER, 1: ["Edit", "Tools"]},
        corner_three={0: OledReactionType.STATIC, 1: ["Resolve"]},
        corner_four={0: OledReactionType.STATIC, 1: ["Pad"]},
    ),
    toDisplay=OledDisplayMode.TXT,
    flip=False,
    i2c=board.I2C()  # SDA=D4, SCL=D5
)
keyboard.extensions.append(oled_ext)

# ========================================
# KEYMAP CONFIGURATION
# ========================================
# Physical layout (based on your schematic):
#
#   [SW2]   [SW5]   [Encoder Button]   <  Row 1 (D3)
#   [SW3]   [SW4]   [EMPTY]            <  Row 2 (D2)
#     |       |         |
#    D1      D0        D9
#
# Matrix positions:
#   [0]=SW2    [1]=SW5    [2]=Encoder Button
#   [3]=SW3    [4]=SW4    [5]=Empty/No key

# ========================================
# CHOOSE YOUR LAYOUT BELOW:
# ========================================

#     DaVinci Resolve Editing Shortcuts (ACTIVE)    
keyboard.keymap = [
    [
        # Layer 0: Essential Editing Controls
        KC.J,            # [0] SW2: Reverse play (shuttle backward)
        KC.L,            # [1] SW5: Forward play (shuttle forward)
        KC.MO(1),        # [2] Encoder Button: Hold for Layer 1
        KC.I,            # [3] SW3: Mark In point
        KC.O,            # [4] SW4: Mark Out point
        KC.NO,           # [5] Empty position
    ],
    [
        # Layer 1: Tools & Shortcuts (hold encoder button)
        KC.LCTL(KC.Z),   # [0] SW2: Undo
        KC.LCTL(KC.LSFT(KC.Z)),  # [1] SW5: Redo
        KC.TRNS,         # [2] Encoder Button: Transparent
        KC.B,            # [3] SW3: Blade/Cut tool
        KC.M,            # [4] SW4: Add Marker
        KC.NO,           # [5] Empty position
    ],
]

# DaVinci Resolve Quick Reference:
# Layer 0 (Normal editing):
#   SW2 (J) = Play backwards / Reverse shuttle
#   SW5 (L) = Play forwards / Forward shuttle
#   SW3 (I) = Mark In point
#   SW4 (O) = Mark Out point
#   Encoder = Scrub timeline (Left/Right arrows)
#
# Layer 1 (Hold encoder button):
#   SW2 = Undo
#   SW5 = Redo
#   SW3 (B) = Blade/Cut tool
#   SW4 (M) = Add Marker
#   Encoder = Zoom timeline in/out

#     Alternative Layout: Playback + Color (Commented)    
# keyboard.keymap = [
#     [
#         KC.SPACE,             # SW2: Play/Pause
#         KC.K,                 # SW5: Stop/Pause
#         KC.MO(1),             # Encoder: Layer switch
#         KC.LSFT(KC.Z),        # SW3: Fit timeline to window
#         KC.M,                 # SW4: Add Marker
#         KC.NO,
#     ],
#     [
#         KC.RGB_TOG,           # SW2: Toggle RGB
#         KC.RGB_MODE_FORWARD,  # SW5: Next animation
#         KC.TRNS,              # Encoder: Transparent
#         KC.RGB_VAI,           # SW3: Brightness up
#         KC.RGB_VAD,           # SW4: Brightness down
#         KC.NO,
#     ],
# ]

# ========================================
# ENCODER MAPPING
# ========================================
encoder_handler.map = [
    ((KC.RIGHT, KC.LEFT),),     # Layer 0: Scrub timeline (frame by frame)
    ((KC.LCTL(KC.EQUAL), KC.LCTL(KC.MINUS)),),  # Layer 1: Zoom timeline in/out
]

# DaVinci Resolve Encoder Functions:
# Layer 0: Left/Right arrows = Move playhead frame by frame (scrub timeline)
# Layer 1: Ctrl+= / Ctrl+  = Zoom timeline in/out

# Other useful encoder options for DaVinci:
# ((KC.UP, KC.DOWN),)             # Move between tracks
# ((KC.PGUP, KC.PGDN),)           # Jump between clips
# ((KC.LBRC, KC.RBRC),)           # Trim clip start/end ([ and ])
# ((KC.COMMA, KC.DOT),)           # Previous/Next frame (faster)

# ========================================
# RGB LED CONTROL KEYS
# ========================================
# Add these to your keymap to control RGB:
# KC.RGB_TOG             Toggle RGB on/off
# KC.RGB_MODE_FORWARD    Next animation mode
# KC.RGB_MODE_REVERSE    Previous animation mode
# KC.RGB_HUI             Hue+ (change color forward)
# KC.RGB_HUD             Hue  (change color backward)
# KC.RGB_SAI             Saturation+ (more vivid)
# KC.RGB_SAD             Saturation  (less vivid)
# KC.RGB_VAI             Brightness+
# KC.RGB_VAD             Brightness 
# KC.RGB_ANI             Animation speed+
# KC.RGB_AND             Animation speed 

# ========================================
# RGB ANIMATION MODES
# ========================================
# Change the animation_mode in RGB config above to:
#   AnimationModes.STATIC              # Solid color
#   AnimationModes.BREATHING           # Smooth fade
#   AnimationModes.RAINBOW             # Rainbow cycle
#   AnimationModes.BREATHING_RAINBOW   # Rainbow + breathing
#   AnimationModes.KNIGHT              # Knight Rider
#   AnimationModes.SWIRL               # Spinning effect

# ========================================
# QUICK REFERENCE   DAVINCI RESOLVE
# ========================================
# Your 4 switches: SW2, SW3, SW4, SW5
# Plus encoder button in matrix
# 
# Default layout (Layer 0   Editing):
#   SW2 (J)   = Play backwards / Reverse shuttle
#   SW5 (L)   = Play forwards / Forward shuttle
#   SW3 (I)   = Mark In point
#   SW4 (O)   = Mark Out point
#   Encoder   = Scrub timeline (Left/Right arrows)
#
# Layer 1 (Hold encoder button   Tools):
#   SW2       = Undo (Ctrl+Z)
#   SW5       = Redo (Ctrl+Shift+Z)
#   SW3 (B)   = Blade/Cut tool
#   SW4 (M)   = Add Marker
#   Encoder   = Zoom timeline in/out (Ctrl+=/ )
#
# DaVinci Resolve Tips:
#   J/K/L are the classic shuttle controls (backwards/stop/forward)
#   Tapping J or L multiple times increases playback speed
#   I/O marks your in and out points for editing
#   Press Space to play/pause (add to a key if you prefer)
#   Use the encoder to scrub frame by frame through your footage

if __name__ == '__main__':
    keyboard.go()