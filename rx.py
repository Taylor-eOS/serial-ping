from machine import Pin, UART
import time
import neopixel

uart = UART(0, baudrate=9600, tx=Pin(0), rx=Pin(1))
led = neopixel.NeoPixel(Pin(16), 1)

led[0] = (0, 255, 0)
led.write()
time.sleep(1)
led[0] = (0, 0, 0)
led.write()

def blink_green(n):
    for i in range(n):
        led[0] = (0, 255, 0)
        led.write()
        time.sleep(0.2)
        led[0] = (0, 0, 0)
        led.write()
        time.sleep(0.2)

last_status = time.time()
while True:
    if uart.any():
        data = uart.read().strip()
        print('Received:', data.decode())
        if data == b'test':
            blink_green(1)
        last_status = time.time()
    if time.time() - last_status > 10:
        print('No data received, waiting...')
        last_status = time.time()
    time.sleep(0.05)
