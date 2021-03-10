from machine import Pin, UART
import time

led = Pin(11, Pin.OUT)
BT = UART(1, 9600)

while True:   
    if BT.any() > 0:
        dato = BT.read(1)
        if "A" in dato:
            led.on()        
        elif "B" in dato:        
            led.off()