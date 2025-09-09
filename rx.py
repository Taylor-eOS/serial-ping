from machine import Pin, UART
import time
import neopixel

uart = UART(0, baudrate=115200, tx=Pin(0), rx=Pin(1))
led = neopixel.NeoPixel(Pin(16), 1)
last_data_time = time.ticks_ms()

def quick_blink(color):
    led[0] = color
    led.write()
    time.sleep(0.02)
    led[0] = (0, 0, 0)
    led.write()

while True:
    if uart.any():
        data = uart.read(1)
        if data:
            value1 = (data[0] >> 4) & 0x0F
            value2 = data[0] & 0x0F
            value1 = 4 * value1 + 195
            value2 = 4 * value2 + 195
            print(f'Values: {value1}, {value2}')
            quick_blink((0, 64, 0))
            last_data_time = time.ticks_ms()
    if time.ticks_diff(time.ticks_ms(), last_data_time) > 500:
        quick_blink((64, 64, 0))
        last_data_time = time.ticks_ms()
    time.sleep_ms(1)
