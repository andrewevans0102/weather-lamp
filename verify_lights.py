import RPi.GPIO as GPIO
import time

white_light=21
green_light=20
yellow_light=16
blue_light=14
red_light=18
red_2=17
blue_2=27
yellow_2=22
green_2=10
white_2=9

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(white_light,GPIO.OUT)
print("LED on")
GPIO.output(white_light,GPIO.HIGH)
time.sleep(1)
print("LED off")
GPIO.output(white_light,GPIO.LOW)

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(green_light,GPIO.OUT)
print("LED on")
GPIO.output(green_light,GPIO.HIGH)
time.sleep(1)
print("LED off")
GPIO.output(green_light,GPIO.LOW)

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(yellow_light,GPIO.OUT)
print("LED on")
GPIO.output(yellow_light,GPIO.HIGH)
time.sleep(1)
print("LED off")
GPIO.output(yellow_light,GPIO.LOW)

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(blue_light,GPIO.OUT)
print("LED on")
GPIO.output(blue_light,GPIO.HIGH)
time.sleep(1)
print("LED off")
GPIO.output(blue_light,GPIO.LOW)

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(red_light,GPIO.OUT)
print("LED on")
GPIO.output(red_light,GPIO.HIGH)
time.sleep(1)
print("LED off")
GPIO.output(red_light,GPIO.LOW)

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(red_2,GPIO.OUT)
print("LED on")
GPIO.output(red_2,GPIO.HIGH)
time.sleep(1)
print("LED off")
GPIO.output(red_2,GPIO.LOW)

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(blue_2,GPIO.OUT)
print("LED on")
GPIO.output(blue_2,GPIO.HIGH)
time.sleep(1)
print("LED off")
GPIO.output(blue_2,GPIO.LOW)

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(yellow_2,GPIO.OUT)
print("LED on")
GPIO.output(yellow_2,GPIO.HIGH)
time.sleep(1)
print("LED off")
GPIO.output(yellow_2,GPIO.LOW)

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(green_2,GPIO.OUT)
print("LED on")
GPIO.output(green_2,GPIO.HIGH)
time.sleep(1)
print("LED off")
GPIO.output(green_2,GPIO.LOW)

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(white_2,GPIO.OUT)
print("LED on")
GPIO.output(white_2,GPIO.HIGH)
time.sleep(1)
print("LED off")
GPIO.output(white_2,GPIO.LOW)
