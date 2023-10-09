from machine import Pin
import time

trig = Pin(3, Pin.OUT)
echo = Pin(2, Pin.IN, Pin.PULL_DOWN)

while True:
    trig.value(0)
    time.sleep(0.1)
    trig.value(1)
    time.sleep_us(2)
    trig.value(0)
    while echo.value()==0:
        pulse_start = time.ticks_us()
    while echo.value()==1:
        pulse_end = time.ticks_us()
    pulse_duration = pulse_end - pulse_start
    # sound travels 0.343 meters per millisecond or 0.0343cm per milisecond
    distance = (timepassed * 0.0343) / 2
    distance = round(distance, 0)
    print ('Distance:',"{:.0f}".format(distance),'cm')
    time.sleep(1)

