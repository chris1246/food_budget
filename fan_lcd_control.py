from gpiozero import CPUTemperature
import RPi.GPIO as GPIO
import sys
import time

cpu = CPUTemperature()

fan_relay = 22
led_pin = 18
max_temp = 50
GPIO.setup(fan_relay, GPIO.OUT)
GPIO.setup(led_pin, GPIO.OUT)

try:
    while True:
        GPIO.output(led_pin, 1)

        if cpu.temperature > max_temp:
            GPIO.output(fan_relay, 1)
            time.sleep(30)
        else:
            GPIO.output(fan_relay, 0)

except KeyboardInterrupt:
    print("interrupted")
    GPIO.cleanup
    sys.exit(0)
