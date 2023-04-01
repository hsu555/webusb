def show_working():
    serial.write_value("acc.x", input.acceleration(Dimension.X))
    serial.write_value("acc.y", input.acceleration(Dimension.Y))
    serial.write_value("acc.z", input.acceleration(Dimension.Z))
    led.toggle(randint(0, 4), randint(0, 4))
    control.wait_micros(30000)

def on_button_pressed_a():
    basic.clear_screen()
    serial.write_line("" + str((input.temperature())))
    basic.show_string("" + str((input.temperature())))
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    for index in range(100):
        show_working()
    basic.clear_screen()
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_logo_pressed():
    basic.clear_screen()
    basic.show_string("Hello!")
    basic.pause(200)
input.on_logo_event(TouchButtonEvent.PRESSED, on_logo_pressed)

music.play_sound_effect(music.create_sound_effect(WaveShape.SINE,
        5000,
        0,
        255,
        0,
        1000,
        SoundExpressionEffect.NONE,
        InterpolationCurve.LINEAR),
    SoundExpressionPlayMode.IN_BACKGROUND)

def on_forever():
    pass
basic.forever(on_forever)
