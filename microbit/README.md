# Channel Zero: Breaking and Building Radio Security
Participant materials for the micro:bit radio session at DSU GenCyber.

## The Session
The [BBC micro:bit](https://microbit.org) is a pocket-sized computer with an LED display, buttons, and a built-in radio that can talk to other micro:bits nearby. In this session participants program a micro:bit to send and receive messages over the radio, using a shared *group number* to keep their conversation separate from everyone else's.

The group number works like a pre-shared key: only devices set to the same group hear each other. But the messages themselves are not encrypted. Once we've built the messenger, we flip sides and scan through all 256 groups to listen in on other teams' channels. The point is to show that **channel isolation alone is not secure communication**.

### Start Here
 1. [Channel Zero Presentation](https://github.com/DSUmjham/GenCyber/blob/master/microbit/Channel%20Zero%20Presentation.pdf) - Slides for the session, including the micro:bit hardware tour, the messenger build, and the channel group scanner.
 2. Open the [MakeCode editor](https://makecode.microbit.org) and import one of the `.hex` files below to view and edit the code in Blocks, Python, or JavaScript.
 3. Plug your micro:bit into your computer over USB and drag the `.hex` file onto the `MICROBIT` drive to flash it.

## Firmware
All programs were built with [Microsoft MakeCode](https://makecode.microbit.org). Each `.hex` file contains the source code, so importing it into MakeCode opens the full project.

* [microbit-Blink.hex](https://github.com/DSUmjham/GenCyber/raw/master/microbit/Firmware/microbit-Blink.hex) - Starter program that shows a heart on the display. A quick way to test that your micro:bit flashes correctly.
* [microbit-Secret-Messenger.hex](https://github.com/DSUmjham/GenCyber/raw/master/microbit/Firmware/microbit-Secret-Messenger.hex) - Radio messenger on group `123`. Press **A** to broadcast `HI`; any message received is scrolled across the display.
* [microbit-Secret-Messenger-Extension.hex](https://github.com/DSUmjham/GenCyber/raw/master/microbit/Firmware/microbit-Secret-Messenger-Extension.hex) - Adds an alert to the messenger. Press **B** to send `ALERT`, which shows a skull and plays a sound on every receiving micro:bit (the sound requires a micro:bit V2 with its built-in speaker).

## Breaking the Channel
* [channel_group_scanner.py](https://github.com/DSUmjham/GenCyber/blob/master/microbit/channel_group_scanner.py) - MakeCode Python program that steps through every radio group (0–255), pausing 200ms on each. When it picks up a message it plays a sound and shows the group number and message, like `123:HI`. To use it, create a new MakeCode project, switch to the **Python** editor, and paste in the code.

> **Tip:** Change `radio.set_group(123)` to your own number (0–255) so your team has its own channel... until someone scans for it.

## Resources
* [micro:bit](https://microbit.org) - Official site with projects, lessons, and hardware details.
* [MakeCode for micro:bit](https://makecode.microbit.org) - Browser-based editor used to build these programs.
* [micro:bit Radio Reference](https://makecode.microbit.org/reference/radio) - Documentation for the radio blocks used in the messenger.
