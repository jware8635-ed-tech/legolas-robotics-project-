led.enable(false)
pins.setPull(DigitalPin.P8, PinPullMode.PullUp) 
basic.forever(function () {
    if (pins.digitalReadPin(DigitalPin.P8) == 0) {
        pins.digitalWritePin(DigitalPin.P4, 1)
    } else {
         pins.digitalWritePin(DigitalPin.P4, 0)
    }
})
