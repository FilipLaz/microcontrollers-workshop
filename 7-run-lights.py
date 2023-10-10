import machine
import utime

# RUNNING LIGHT
while True:
    for i in range(29):                      
        if i != 23 and i != 24:      
            machine.Pin(i).value(0)     # turn off the LED
            utime.sleep(0.1)            # sleep for 100ms
            machine.Pin(i).value(1)     # turn on the LED
            
    for i in range(28,-1,-1):           # from 28 to 0
        if i != 23 and i != 24:
            machine.Pin(i).value(1)     # turn on the LED
            utime.sleep(0.1)
            machine.Pin(i).value(0)     # turn off the LED
