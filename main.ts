let light_lvl = 0
let FlashingYellowOn = false
let CarInMotion = false
k_Bit.Led(COLOR.white)
basic.clearScreen()
pins.analogSetPitchPin(AnalogPin.P0)
music.startMelody(music.builtInMelody(Melodies.PowerUp), MelodyOptions.Once)
let strip = neopixel.create(DigitalPin.P5, 18, NeoPixelMode.RGB)
strip.setBrightness(127)
function moveForward() {
    
    
    let speed = Math.trunc(light_lvl * 100 / 255)
    k_Bit.run(DIR.RunForward, speed)
    CarInMotion = true
    basic.showArrow(ArrowNames.North)
    strip.setPixelColor(1, neopixel.colors(NeoPixelColors.Red))
    strip.show()
    while (CarInMotion) {
        strip.rotate(-1)
        strip.show()
        basic.pause(100)
    }
}

function moveBack() {
    
    
    let speed = Math.trunc(light_lvl * 100 / 255)
    k_Bit.run(DIR.RunBack, speed)
    CarInMotion = true
    basic.showArrow(ArrowNames.South)
    strip.setPixelColor(1, neopixel.colors(NeoPixelColors.Red))
    strip.show()
    while (CarInMotion) {
        strip.rotate(1)
        strip.show()
        basic.pause(100)
    }
}

function turnLeft() {
    
    
    let course = input.compassHeading()
    let speed = Math.trunc(light_lvl * 100 / 255)
    k_Bit.run(DIR.TurnLeft, speed)
    basic.showArrow(ArrowNames.West)
    FlashingYellowOn = true
    while ((input.compassHeading() - course) % 360 < 90) {
        pause(20)
    }
    k_Bit.carStop()
    basic.clearScreen()
    FlashingYellowOn = false
}

function turnRight() {
    
    
    let course = input.compassHeading()
    let speed = Math.trunc(light_lvl * 100 / 255)
    k_Bit.run(DIR.TurnRight, speed)
    basic.showArrow(ArrowNames.East)
    FlashingYellowOn = true
    while ((course - input.compassHeading()) % 360 < 90) {
        pause(20)
    }
    k_Bit.carStop()
    basic.clearScreen()
    FlashingYellowOn = false
}

function ReverseRight() {
    
    
    let course = input.compassHeading()
    let speed = Math.trunc(light_lvl * 100 / 255)
    k_Bit.run(DIR.TurnRight, speed)
    basic.showArrow(ArrowNames.SouthEast)
    FlashingYellowOn = true
    while ((course - input.compassHeading()) % 360 < 180) {
        pause(20)
    }
    k_Bit.carStop()
    basic.clearScreen()
    FlashingYellowOn = false
}

basic.forever(function GetLightLevel() {
    let light_lvl = input.lightLevel()
    k_Bit.LED_brightness(255 - light_lvl)
})
basic.forever(function on_forever2() {
    input.onButtonPressed(Button.A, function ReverseLeft() {
        
        
        let course = input.compassHeading()
        let speed = Math.trunc(light_lvl * 100 / 255)
        k_Bit.run(DIR.TurnLeft, speed)
        basic.showArrow(ArrowNames.SouthWest)
        FlashingYellowOn = true
        while ((input.compassHeading() - course) % 360 < 180) {
            pause(20)
        }
        k_Bit.carStop()
        basic.clearScreen()
        FlashingYellowOn = false
    })
})
basic.forever(function flashing_yellow() {
    if (FlashingYellowOn == true) {
        strip.showColor(neopixel.colors(NeoPixelColors.Orange))
        basic.pause(500)
        strip.clear()
        strip.show()
        basic.pause(500)
    }
    
})
