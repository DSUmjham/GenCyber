current_group = 0

# set up radio to show any intercepted messages & group number
def on_received(msg):
    music.play(music.builtin_playable_sound_effect(soundExpression.spring), music.PlaybackMode.UNTIL_DONE)
    basic.show_string(str(current_group) + ":" + msg)
radio.on_received_string(on_received)
radio.on()

# scan through all channels (0-255) with a 200ms delay
def scan():
    global current_group
    while True:
        radio.set_group(current_group)
        basic.pause(200)
        current_group = (current_group + 1) % 256

control.in_background(scan)
