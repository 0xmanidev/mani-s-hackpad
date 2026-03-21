DaVinci Resolve Macropad – Video Editing Controller

A custom 4-key macropad with a rotary encoder, OLED display, and bright RGB LEDs, built just for DaVinci Resolve video editing workflows.

What This Macropad Does

Editing in DaVinci Resolve gets way easier with this little controller. You get:
- Classic J-K-L shuttle control—think fast playback, instant response
- Mark In and Out keys for precise edits
- Scrubbing frame-by-frame with a quick twist of the encoder
- Undo/redo and extra editing tools on a second layer
- Bright RGB LEDs and OLED display for instant visual feedback

If you edit a lot and your fingers keep flying back and forth across your keyboard, this macropad is the shortcut you’ve been dreaming of.

Features

- 4 clicky mechanical switches (compatible with Cherry MX)
- A rotary encoder to scrub the timeline or adjust volume
- OLED display shows layer and status info at a glance
- 2 RGB LEDs (WS2812B) with breathing effects—eye candy included
- 2 layers: main editing & tools/RGB control 
- Easy-to-tweak firmware—customize away
- Comes in a snappy 3D printed case

How to Flash the Firmware

1. Install CircuitPython:
   - Get it from circuitpython.org
   - Hold BOOT, press RESET on the XIAO board
   - Drag the .uf2 file onto the RPI-RP2 drive

2. Install KMK Firmware:
   git clone https://github.com/KMKfw/kmk_firmware.git
   cp -r kmk_firmware/kmk /path/to/CIRCUITPY/

3. Install Libraries:
   - Download the Adafruit CircuitPython Bundle
   - Copy to CIRCUITPY/lib/:
     - adafruit_display_text/
     - adafruit_displayio_ssd1306.mpy
     - adafruit_framebuf.mpy

4. Upload Firmware:
   cp firmware/code.py /path/to/CIRCUITPY/

5. Test it: Your board should light up—OLED turns on, RGBs glow!

Using the Macropad

Default Layout

Layer 0 (Main Editing)
[J - Reverse]  [L - Forward]   [Hold: Layer 1]
[I - Mark In]  [O - Mark Out]  [---]

Turn encoder for precise, frame-by-frame scrubbing.

Layer 1 (Tools – Hold encoder button)
[Undo]         [Redo]
[Blade Tool]   [Add Marker]

Encoder here zooms the timeline in and out.

Key Shortcuts

- J: Play backwards (hit it quickly for faster reverse)
- L: Play forwards (again, tap fast for speed)
- I: Mark In point for edits
- O: Mark Out point for edits
- Encoder Turn: Scrub timeline, frame by frame

Layer 1 (Press & Hold Encoder Button)
- Undo: Ctrl+Z
- Redo: Ctrl+Shift+Z
- Blade Tool: B
- Add Marker: M
- Encoder: Zooms timeline (Ctrl+=/Ctrl-)

Customization

Want to adjust how the buttons work? Edit firmware/code.py:
keyboard.keymap = [
    [
        KC.SPACE,        # Make J Play/Pause instead
        KC.M,            # Make L Add Marker
        KC.MO(1),        # Switch layers
        KC.Q,            # Ripple Delete
        KC.W,            # Insert Edit
        KC.NO,
    ],
]

Change the RGB effects:

rgb = RGB(
    animation_mode=AnimationModes.RAINBOW,
    hue_default=0,
    val_default=100,
)

Add more layers if you switch between editing, color grading, or audio—just tweak and go.

Why I Built This

Honestly, reaching for tiny keys in the middle of the keyboard to shuttle or set markers slowed me down. I wanted editing to feel direct and fun—almost like playing music. The encoder makes scrubbing smooth, and with the OLED on top, I always know what my controller’s doing.

This project made editing way less about typing and more about moving—with your hands, eyes, and focus on the story, not the keyboard.

License

All code here falls under the MIT License (see LICENSE for details). Hardware (PCB, case) is CERN-OHL-P v2.

Thanks

Big cheers to:
- Hack Club, for their awesome community
- KMK Firmware, which just works
- CircuitPython, for making hardware hacking easy
- Seeed Studio, for the trusty XIAO RP2040

Contact

Made by Mani Dev
- GitHub: @0xmanidev
- Email: manikanta.vasamsetti.dev@gmail.com

Resources

- KMK Documentation
- XIAO RP2040 Wiki
- DaVinci Resolve Shortcuts

Made with ❤️ for Hack Club.
