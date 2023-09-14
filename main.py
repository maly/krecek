def on_gesture_shake():
    basic.show_icon(IconNames.SAD)
    soundExpression.mysterious.play_until_done()
    basic.show_icon(IconNames.ASLEEP)
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

def on_logo_pressed():
    basic.show_icon(IconNames.HAPPY)
    soundExpression.hello.play_until_done()
    basic.show_icon(IconNames.ASLEEP)
input.on_logo_event(TouchButtonEvent.PRESSED, on_logo_pressed)

music.start_melody(music.built_in_melody(Melodies.POWER_UP), MelodyOptions.ONCE)
basic.show_icon(IconNames.ASLEEP)

def on_forever():
    pass
basic.forever(on_forever)
