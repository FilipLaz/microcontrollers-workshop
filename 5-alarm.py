import machine
import utime

sensor = machine.Pin(0, machine.Pin.IN)
led = machine.Pin('LED', machine.Pin.OUT)
buzzer = machine.Pin(18, machine.Pin.OUT)

def pir_handler(pin):
    print("ALARM! Motion detected!")
    for i in range(50):
        led.toggle()
        for j in range(25):
            buzzer.toggle()
            utime.sleep_ms(3)


sensor.irq(trigger = machine.Pin.IRQ_RISING, handler = pir_handler)

while True:
    led.toggle()   
    buzzer.off()   
    utime.sleep(2) 
