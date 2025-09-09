from machine import Pin, UART
import time
import random
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
        time.sleep(0.1)
        led[0] = (0, 0, 0)
        led.write()
        time.sleep(0.1)

while True:
    value = random.randint(1, 3)
    uart.write(f'{value}\n'.encode())
    print(f'Sent: {value}')
    blink_blue(1)
    time.sleep(0.2)
