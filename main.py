def show_working():
    serial.write_value("acc.x", input.acceleration(Dimension.X))
    serial.write_value("acc.y", input.acceleration(Dimension.Y))
    serial.write_value("acc.z", input.acceleration(Dimension.Z))
    led.toggle(randint(0, 4), randint(0, 4))
    basic.pause(200)

def on_button_pressed_a():
    basic.clear_screen()
    serial.write_line("" + str((input.temperature())))
    basic.show_string("" + str((input.temperature())))
    basic.pause(200)
    serial.write_line("" + str((input.light_level())))
    basic.show_string("" + str((input.light_level())))
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    show_working()
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_logo_pressed():
    basic.clear_screen()
    basic.show_string("Hello!")
    basic.pause(200)
input.on_logo_event(TouchButtonEvent.PRESSED, on_logo_pressed)

music.play_melody("C D E F G A B C5 ", 120)

def on_forever():
    pass
basic.forever(on_forever)
