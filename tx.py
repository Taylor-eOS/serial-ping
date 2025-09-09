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
        time.sleep(0.05)
        led[0] = (0, 0, 0)
        led.write()
        time.sleep(0.05)

def blink_red(n):
    for i in range(n):
        led[0] = (255, 0, 0)
        led.write()
        time.sleep(0.05)
        led[0] = (0, 0, 0)
        led.write()
        time.sleep(0.05)

while True:
    value1 = random.randint(0, 15)
    value2 = random.randint(0, 15)
    binary_str = f'{value1:04b}{value2:04b}'
    uart.write(f'{binary_str}\n'.encode())
    print(f'Sent ints: {value1}, {value2}, as binary: {binary_str}')
    blink_blue(value1 if value1 > 0 else 1)
    time.sleep(0.5)
    blink_red(value2 if value2 > 0 else 1)
    time.sleep(2)
