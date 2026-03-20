# DaVinci Resolve Macropad - Video Editing Controller

> A custom 4-key macropad with rotary encoder, OLED display, and RGB LEDs, designed specifically for DaVinci Resolve video editing workflows.

![Macropad Hero Shot](assets/mani'shackpad.png)


## ✨ What It Does

This macropad gives you instant, tactile control over DaVinci Resolve's most essential shortcuts:
- **J-K-L shuttle control** for playback (industry standard)
- **I/O marks** for precise three-point editing
- **Frame-by-frame scrubbing** with the rotary encoder
- **Quick undo/redo** and editing tools on second layer
- **Visual feedback** with RGB LEDs and OLED display

Perfect for video editors who want faster, more intuitive editing without constantly reaching for keyboard shortcuts!

## 🎯 Features

- **4 Mechanical Switches** - Cherry MX compatible
- **Rotary Encoder** - Scrub timeline or control volume
- **OLED Display** - Shows current layer and status
- **2 RGB LEDs** - WS2812B with breathing effects
- **2 Layers** - Editing layer + Tools/RGB control layer
- **Hot-swappable firmware** - Easy to customize
- **with a case** - 3D printed bottom




### Flash the Firmware

1. **Install CircuitPython:**
   - Download from [circuitpython.org](https://circuitpython.org/board/seeeduino_xiao_rp2040/)
   - Hold BOOT, press RESET on XIAO
   - Drag `.uf2` file to RPI-RP2 drive

2. **Install KMK Firmware:**
   ```bash
   git clone https://github.com/KMKfw/kmk_firmware.git
   cp -r kmk_firmware/kmk /path/to/CIRCUITPY/
   ```

3. **Install Libraries:**
   - Download [Adafruit CircuitPython Bundle](https://circuitpython.org/libraries)
   - Copy to `CIRCUITPY/lib/`:
     - `adafruit_display_text/`
     - `adafruit_displayio_ssd1306.mpy`
     - `adafruit_framebuf.mpy`

4. **Upload Firmware:**
   ```bash
   cp firmware/code.py /path/to/CIRCUITPY/
   ```

5. **Test!** - Board should show OLED display and RGB LEDs glowing
6. Upload designated firmware

## 🎮 Using the Macropad

### Default Layout

**Layer 0 (Normal Editing):**
```
[J - Reverse]  [L - Forward]   [Hold: Layer 1]
[I - Mark In]  [O - Mark Out]  [---]

Turn Encoder: Scrub timeline frame-by-frame
```

**Layer 1 (Tools - Hold encoder button):**
```
[Undo]         [Redo]          [---]
[Blade Tool]   [Add Marker]    [---]

Turn Encoder: Zoom timeline in/out
```

### Key Shortcuts

- **J** - Play backwards (tap multiple times for faster playback)
- **L** - Play forwards (tap multiple times for faster playback)
- **I** - Mark In point (start of edit)
- **O** - Mark Out point (end of edit)
- **Encoder Turn** - Scrub timeline left/right (frame-by-frame)

**Layer 1 (Hold encoder button):**
- **Undo** (Ctrl+Z)
- **Redo** (Ctrl+Shift+Z)
- **B** - Blade/Cut tool
- **M** - Add Marker
- **Encoder Turn** - Zoom timeline (Ctrl+=/Ctrl+-)

## 🎨 Customization

### Change Key Mappings

Edit `firmware/code.py`:

```python
keyboard.keymap = [
    [
        KC.SPACE,        # Change J to Play/Pause
        KC.M,            # Change L to Add Marker
        KC.MO(1),        # Layer switch
        KC.Q,            # Ripple Delete
        KC.W,            # Insert Edit
        KC.NO,
    ],
]
```


### Change RGB Effects

```python
rgb = RGB(
    animation_mode=AnimationModes.RAINBOW,  # Change animation
    hue_default=0,     # 0=Red, 85=Green, 170=Blue
    val_default=100,   # Brightness (0-255)
)
```

### Add More Layers

Perfect for switching between editing, color grading, and audio workflows!


## 🎬 Why This Project?

As a video editor, I was constantly reaching for keyboard shortcuts. The J-K-L shuttle control is the foundation of fast editing, but it's buried in the middle of the keyboard. Having dedicated, tactile keys for these essential controls transformed my editing workflow.

The rotary encoder is perfect for frame-by-frame scrubbing - much more intuitive than arrow keys. And the OLED display means I always know which layer I'm on.

This macropad makes editing feel more like playing an instrument than typing on a keyboard. 🎹


## 📝 License

This project is licensed under the MIT License - see [LICENSE](LICENSE) file for details.

Hardware designs (PCB, case) are licensed under CERN-OHL-P v2.

## 🙏 Acknowledgments

- **Hack Club** - For fostering the maker community and providing the platform to share this
- **KMK Firmware** - Amazing keyboard firmware framework 
- **CircuitPython** - Making hardware programming accessible
- **Seeed Studio** - Great XIAO RP2040 board
## 📧 Contact

Built by **Mani Dev**

- GitHub: [@0xmanidev](https://github.com/0xmamidev)
- Email: manikanta.vasamsetti.dev@gmail.com

## 🔗 Resources

- [KMK Documentation](https://github.com/KMKfw)
- [XIAO RP2040 Wiki](https://wiki.seeedstudio.com/XIAO-RP2040/)
- [DaVinci Resolve Shortcuts](https://documents.blackmagicdesign.com/UserManuals/DaVinci_Resolve_18_Keyboard_Shortcuts.pdf)

---

**Made with ❤️ for the Hack Club community**

[Join Hack Club](https://hackclub.com) 
---
