from machine import Pin
import time

button1 = Pin(16, Pin.IN, Pin.PULL_UP)
button2 = Pin(17, Pin.IN, Pin.PULL_UP)

led1 = Pin(2, Pin.OUT)
led2 = Pin(4, Pin.OUT)

while True:
    if button1.value() == 0:
        led1.value(1)
        print("Tombol 1 ditekan - LED 1 ON")
    else:
        led1.value(0)
        print("Tombol 1 dilepas - LED 1 OFF")
    
    if button2.value() == 0:
        led2.value(1)
        print("Tombol 2 ditekan - LED 2 ON")
    else:
        led2.value(0)
        print("Tombol 2 dilepas - LED 2 OFF")
    
    time.sleep(0.1)