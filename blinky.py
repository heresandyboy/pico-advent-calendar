from machine import Pin
import time

green = Pin(18, Pin.OUT)
amber = Pin(19, Pin.OUT)
red = Pin(20, Pin.OUT)

green.value(1)
amber.value(1)
red.value(1)

time.sleep(5)

green.value(0)
amber.value(0)
red.value(0)