input.onButtonPressed(Button.A, function () {
    for (let index = 0; index < 4; index++) {
        soundExpression.giggle.playUntilDone()
    }
})
input.onGesture(Gesture.Shake, function () {
    music.setBuiltInSpeakerEnabled(true)
    basic.showIcon(IconNames.Giraffe)
})
input.onLogoEvent(TouchButtonEvent.Pressed, function () {
    basic.showString("?What is up?")
})
input.onButtonPressed(Button.B, function () {
    music.setBuiltInSpeakerEnabled(false)
})
input.onSound(DetectedSound.Loud, function () {
    basic.showLeds(`
        # . . . #
        . # . # .
        . . # . .
        . # . # .
        # . . . #
        `)
})
basic.showIcon(IconNames.StickFigure)
basic.forever(function () {
    basic.showLeds(`
        . # # # .
        # . . . .
        . # # # .
        . . . # .
        # # # # .
        `)
    basic.pause(1000)
    basic.showLeds(`
        . # # . .
        . # . # .
        . # . # .
        . # . # .
        . # # . .
        `)
    basic.pause(1000)
    basic.showLeds(`
        . # . . .
        . # . . .
        . # . . .
        . # . . .
        . # # # .
        `)
})
