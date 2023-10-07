import time
from machine import Pin

state = Pin(20, Pin.IN)
led = Pin(25, Pin.OUT)

while True:
    if state.value():
        led.high()
    else:
        led.low()
