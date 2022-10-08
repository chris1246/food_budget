# File: fan.py     Function: active cooling for pi   Type: always running script
# 
# configured to run at boot
# made to be as simple as possible
from gpiozero import CPUTemperature
import RPi.GPIO as GPIO
import sys
import time

cpu = CPUTemperature()

fan_relay = 22 #GPIO22
led_pin = 18 #GPIO18
max_temp = 50
on_timer = 100 # seconds

GPIO.setup(fan_relay, GPIO.OUT)
GPIO.setup(led_pin, GPIO.OUT)

try:
    while True:
        GPIO.output(led_pin, 1)
        if cpu.temperature > max_temp:
            GPIO.output(fan_relay, 1)
            time.sleep(on_timer)
        else:
            GPIO.output(fan_relay, 0)

except KeyboardInterrupt:
    print("interrupted")
    GPIO.cleanup
    sys.exit(0)
