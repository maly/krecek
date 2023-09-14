input.onGesture(Gesture.Shake, function () {
    basic.showIcon(IconNames.Sad)
    soundExpression.mysterious.playUntilDone()
    basic.showIcon(IconNames.Asleep)
})
input.onLogoEvent(TouchButtonEvent.Pressed, function () {
    basic.showIcon(IconNames.Happy)
    soundExpression.hello.playUntilDone()
    basic.showIcon(IconNames.Asleep)
})
music.startMelody(music.builtInMelody(Melodies.PowerUp), MelodyOptions.Once)
basic.showIcon(IconNames.Asleep)
basic.forever(function () {
	
})
