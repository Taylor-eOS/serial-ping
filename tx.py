from machine import Pin, UART
import time
import random
import neopixel

uart = UART(0, baudrate=115200, tx=Pin(0), rx=Pin(1))
led = neopixel.NeoPixel(Pin(16), 1)

def quick_blink(color):
    led[0] = color
    led.write()
    time.sleep(0.02)
    led[0] = (0, 0, 0)
    led.write()

last_update = time.ticks_ms()
interval = 25

while True:
    if time.ticks_diff(time.ticks_ms(), last_update) >= interval:
        value1 = random.randint(192, 255)
        value2 = random.randint(192, 255)
        value1 = (value1 - 192) // 4
        value2 = (value2 - 192) // 4
        data_byte = (value1 << 4) | value2
        uart.write(bytes([data_byte]))
        quick_blink((0, 0, 64))
        last_update = time.ticks_ms()
    time.sleep_ms(1)
