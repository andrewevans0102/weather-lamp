import RPi.GPIO as GPIO
import time

white_light=21


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(white_light,GPIO.OUT)
print("LED on")
GPIO.output(white_light,GPIO.HIGH)
time.sleep(1)
print("LED off")
GPIO.output(white_light,GPIO.LOW)
