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
        time.sleep(0.05)
        led[0] = (0, 0, 0)
        led.write()
        time.sleep(0.05)

def blink_yellow(n):
    for i in range(n):
        led[0] = (255, 255, 0)
        led.write()
        time.sleep(0.05)
        led[0] = (0, 0, 0)
        led.write()
        time.sleep(0.05)

last_status = time.time()
while True:
    if uart.any():
        data = uart.read().strip().decode()
        if len(data) == 8 and all(c in '01' for c in data):
            value1 = int(data[:4], 2)
            value2 = int(data[4:], 2)
            print(f'Received binary: {data}, as ints: {value1}, {value2}')
            blink_green(value1 if value1 > 0 else 1)
            time.sleep(0.5)
            blink_yellow(value2 if value2 > 0 else 1)
        else:
            print(f'Invalid data: {data}')
        last_status = time.time()
    if time.time() - last_status > 5:
        print('No data received, waiting...')
        last_status = time.time()
    time.sleep(0.02)
