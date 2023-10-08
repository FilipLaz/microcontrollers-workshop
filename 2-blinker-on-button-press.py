import time
from machine import Pin

button = Pin(20, Pin.IN)
led = Pin(25, Pin.OUT)

while True:
    if button.value():
        led.high()
    else:
        led.low()
