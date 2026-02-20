# Imports
from machine import Pin
import time

# Set up LED names and GPIO pin numbers
red = Pin(20, Pin.OUT)
amber = Pin(19, Pin.OUT)
green = Pin(18, Pin.OUT)

counter = 1  # Set counter to 1

while counter < 11:  # While count is less than 11
    print(counter)  # Print current counter
    
    # Red ON
    red.value(1)    # ON
    amber.value(0)  # OFF
    green.value(0)  # OFF

    time.sleep(0.5)  # Wait half second

    # Amber ON
    red.value(0)    # OFF
    amber.value(1)  # ON
    green.value(0)  # OFF

    time.sleep(0.5)  # Wait half second

    # Green ON
    red.value(0)    # OFF
    amber.value(0)  # OFF
    green.value(1)  # ON

    time.sleep(0.5)  # Wait half second

    counter += 1  # Add 1 to counter

green.value(0)  # Turn off green after loop ends