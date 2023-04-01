function show_working () {
    serial.writeValue("acc.x", input.acceleration(Dimension.X))
    serial.writeValue("acc.y", input.acceleration(Dimension.Y))
    serial.writeValue("acc.z", input.acceleration(Dimension.Z))
    led.toggle(randint(0, 4), randint(0, 4))
    control.waitMicros(30000)
}
input.onButtonPressed(Button.A, function () {
    basic.clearScreen()
    serial.writeLine("" + (input.temperature()))
    basic.showString("" + (input.temperature()))
})
input.onButtonPressed(Button.B, function () {
    for (let index = 0; index < 100; index++) {
        show_working()
    }
    basic.clearScreen()
})
input.onLogoEvent(TouchButtonEvent.Pressed, function () {
    basic.clearScreen()
    basic.showString("Hello!")
    basic.pause(200)
})
music.playSoundEffect(music.createSoundEffect(WaveShape.Sine, 5000, 0, 255, 0, 1000, SoundExpressionEffect.None, InterpolationCurve.Linear), SoundExpressionPlayMode.InBackground)
basic.forever(function () {
	
})
