# DaVinci Resolve Macropad

A 4-key macropad with rotary encoder, OLED screen, and RGB LEDs for faster video editing in DaVinci Resolve.

![Macropad](assets/mani'shackpad.png)
![Macropad](assets/gerber(still).png)
![Macropad](assets/pcb_desgin.png)
![Macropad](assets/schematics.png)
## What It Does

- **J-K-L shuttle controls** for playback (reverse/forward)
- **Mark In/Out** buttons for quick edits
- **Rotary encoder** to scrub frame-by-frame or zoom timeline
- **OLED display** shows current layer
- **RGB LEDs** with breathing effects
- **2 layers** for editing + extra tools

## Quick Setup

1. Install [CircuitPython](https://circuitpython.org) on your XIAO RP2040
2. Clone KMK firmware and copy to your board
3. Install required Adafruit libraries (displayio_ssd1306, framebuf, display_text)
4. Copy `firmware/code.py` to your CIRCUITPY drive

## Controls

**Layer 0:** J (reverse) | L (forward) | I (mark in) | O (mark out)  
**Layer 1** (hold encoder): Undo | Redo | Blade | Marker

Twist encoder to scrub timeline, or zoom in Layer 1.

## Customization

Edit `code.py` to remap keys or change RGB animations. Add more layers for color grading or audio work.

---

**Built by Mani Dev** • MIT License • Made for Hack Club  
[@0xmanidev](https://github.com/0xmanidev) • manikanta.vasamsetti.dev@gmail.com