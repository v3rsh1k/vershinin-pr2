light_lvl=0
FlashingYellowOn=False
CarInMotion=False
k_Bit.led(COLOR.WHITE)
basic.clear_screen()
pins.analog_set_pitch_pin(AnalogPin.P0)
music.start_melody(music.built_in_melody(Melodies.POWER_UP), MelodyOptions.ONCE)
strip = neopixel.create(DigitalPin.P5, 18, NeoPixelMode.RGB)
strip.set_brightness(127)

def moveForward():
    global light_lvl
    global CarInMotion
    speed=int(light_lvl*100/255)
    k_Bit.run(DIR.RUN_FORWARD, speed)
    CarInMotion=True
    basic.show_arrow(ArrowNames.NORTH)
    strip.set_pixel_color(1, neopixel.colors(NeoPixelColors.RED))
    strip.show()
    while(CarInMotion):
        strip.rotate(-1)
        strip.show()
        basic.pause(100)
 
def moveBack():
    global light_lvl
    global CarInMotion
    speed=int(light_lvl*100/255)
    k_Bit.run(DIR.RUN_BACK, speed)
    CarInMotion=True
    basic.show_arrow(ArrowNames.SOUTH)
    strip.set_pixel_color(1, neopixel.colors(NeoPixelColors.RED))
    strip.show()
    while(CarInMotion):
        strip.rotate(1)
        strip.show()
        basic.pause(100)

def turnLeft():
    global light_lvl
    global FlashingYellowOn
    course=input.compass_heading()
    speed=int(light_lvl*100/255)
    k_Bit.run(DIR.TURN_LEFT, speed)
    basic.show_arrow(ArrowNames.WEST)
    FlashingYellowOn=True
    while((input.compass_heading()-course)%360<90):
        pause(20)
    k_Bit.car_stop()
    basic.clear_screen()
    FlashingYellowOn=False

def turnRight():
    global light_lvl
    global FlashingYellowOn
    course=input.compass_heading()
    speed=int(light_lvl*100/255)
    k_Bit.run(DIR.TURN_RIGHT, speed)
    basic.show_arrow(ArrowNames.EAST)
    FlashingYellowOn=True
    while((course-input.compass_heading())%360<90):
        pause(20)
    k_Bit.car_stop()
    basic.clear_screen()
    FlashingYellowOn=False

def ReverseLeft():
    global light_lvl
    global FlashingYellowOn
    course=input.compass_heading()
    speed=int(light_lvl*100/255)
    k_Bit.run(DIR.TURN_LEFT, speed)
    basic.show_arrow(ArrowNames.SOUTH_WEST)
    FlashingYellowOn=True
    while((input.compass_heading()-course)%360<180):
        pause(20)
    k_Bit.car_stop()
    basic.clear_screen()
    FlashingYellowOn=False

def ReverseRight():
    global FlashingYellowOn
    global light_lvl
    course=input.compass_heading()
    speed=int(light_lvl*100/255)
    k_Bit.run(DIR.TURN_RIGHT, speed)
    basic.show_arrow(ArrowNames.SOUTH_EAST)
    FlashingYellowOn=True
    while(((course-input.compass_heading())%360)<180):
        pause(20)
    k_Bit.car_stop()
    basic.clear_screen()
    FlashingYellowOn=False
        
def GetLightLevel():
    light_lvl=input.light_level()
    k_Bit.LED_brightness(255-light_lvl)  
basic.forever(GetLightLevel)

def on_forever2():
    input.on_button_pressed(Button.A, ReverseLeft)
basic.forever(on_forever2)

def flashing_yellow():
    if(FlashingYellowOn==True):
        strip.show_color(neopixel.colors(NeoPixelColors.ORANGE))
        basic.pause(500)
        strip.clear()
        strip.show()
        basic.pause(500)
basic.forever(flashing_yellow)

                