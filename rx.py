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
        time.sleep(0.1)
        led[0] = (0, 0, 0)
        led.write()
        time.sleep(0.1)

def blink_red(n):
    for i in range(n):
        led[0] = (255, 0, 0)
        led.write()
        time.sleep(0.1)
        led[0] = (0, 0, 0)
        led.write()
        time.sleep(0.1)

def blink_blue(n):
    for i in range(n):
        led[0] = (0, 0, 255)
        led.write()
        time.sleep(0.1)
        led[0] = (0, 0, 0)
        led.write()
        time.sleep(0.1)

last_status = time.time()
while True:
    if uart.any():
        data = uart.read().strip()
        print('Received:', data.decode())
        if data == b'1':
            blink_green(1)
        elif data == b'2':
            blink_red(1)
        elif data == b'3':
            blink_blue(1)
        last_status = time.time()
    if time.time() - last_status > 5:
        print('No data received, waiting...')
        last_status = time.time()
    time.sleep(0.02)
