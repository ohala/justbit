def on_button_pressed_a():
    for index in range(4):
        soundExpression.giggle.play_until_done()
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_gesture_shake():
    music.set_built_in_speaker_enabled(True)
    basic.show_icon(IconNames.GIRAFFE)
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

def on_logo_pressed():
    basic.show_string("?What is up?")
input.on_logo_event(TouchButtonEvent.PRESSED, on_logo_pressed)

def on_button_pressed_b():
    music.set_built_in_speaker_enabled(False)
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_sound_loud():
    basic.show_leds("""
        # . . . #
        . # . # .
        . . # . .
        . # . # .
        # . . . #
        """)
input.on_sound(DetectedSound.LOUD, on_sound_loud)

basic.show_icon(IconNames.STICK_FIGURE)

def on_forever():
    basic.show_leds("""
        . # # # .
        # . . . .
        . # # # .
        . . . # .
        # # # # .
        """)
    basic.pause(1000)
    basic.show_leds("""
        . # # . .
        . # . # .
        . # . # .
        . # . # .
        . # # . .
        """)
    basic.pause(1000)
    basic.show_leds("""
        . # . . .
        . # . . .
        . # . . .
        . # . . .
        . # # # .
        """)
basic.forever(on_forever)
