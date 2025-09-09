from machine import Pin, UART
import time
import neopixel

uart = UART(0, baudrate=9600, tx=Pin(0), rx=Pin(1))
led = neopixel.NeoPixel(Pin(16), 1)

led[0] = (0, 0, 255)
led.write()
time.sleep(1)
led[0] = (0, 0, 0)
led.write()

def blink_blue(n):
    for i in range(n):
        led[0] = (0, 0, 255)
        led.write()
        time.sleep(0.2)
        led[0] = (0, 0, 0)
        led.write()
        time.sleep(0.2)

while True:
    uart.write(b'test\n')
    print('Sent test')
    blink_blue(1)
    time.sleep(1)
