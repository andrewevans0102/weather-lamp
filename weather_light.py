import RPi.GPIO as GPIO
import time
import logging
import requests

# definition of light object
class light:  
    def __init__(self, name, pin):  
        self.name = name
        self.pin = pin 

# create a list of lights
lights = []
# this covers two LEDs
lights.append( light("blue", 27))
# this covers two LEDs
lights.append( light("white", 14))
# this covers two LEDs
lights.append( light("yellow", 16))
# green lights for sucess indicator
lights.append( light("green_1", 20))
lights.append( light("green_2", 10))
# red lights for error indicator
lights.append( light("red_1", 18))
lights.append( light("red_2", 17))

# logging
logging.basicConfig(filename='/home/pi/weather-lamp/history_daily.log',format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.INFO)

# LED colors
light_colors = ['yellow', 'white', 'blue', 'green', 'red']

# weather call
weatherURL = "https://api.weather.gov/gridpoints/AKQ/38,80/forecast/hourly"

# figure out which light to turn on
turnOn = ''

def turnOffAllLights():
    # loop through the list and turn em all off
    for singleLED in lights:
        logging.info("turning off " + singleLED.name)
        GPIO.output(singleLED.pin, GPIO.LOW)

def turnOnGPIOLight( lightName ):
    logging.info("looking for light name " + lightName)
    for singleLED in lights:
        if(singleLED.name.find(lightName) != -1):
            logging.info("turning on " + singleLED.name)
            GPIO.output(singleLED.pin, GPIO.HIGH)
    return

try:
    # official start of program
    logging.info("starting program")
    
    # turn on GPIO settings so we can work with the LEDs connected
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)

    # call setup to initialize all the lights
    for singleLED in lights:
        GPIO.setup(singleLED.pin, GPIO.OUT)

    # first turn off all the lights
    logging.info("lets first turn all the lights off")
    turnOffAllLights()
    
    # call weather service
    logging.info("now lets call the weather service")
    response = requests.get(weatherURL)
    logging.info("weather service API was called with a return status code of " + str(response.status_code))

    # parse JSON
    logging.info("parsing JSON")
    hourlyWeather = response.json()
    properties = hourlyWeather["properties"]
    periods = properties["periods"]
    rightNow = periods[0]
    weatherCondition = rightNow["shortForecast"]

    # log weather condition that was just called
    logging.info("weather condition that was found is " + weatherCondition)

    # figure out which light to turn on
    if (weatherCondition.find('Sunny') != -1) or (weatherCondition.find('Clear') != -1):
        # yellow
        turnOn = light_colors[0]
    elif (weatherCondition.find('Cloudy') != -1) or (weatherCondition.find('Fog') != -1):
        # white
        turnOn = light_colors[1]
    elif (weatherCondition.find('Rain') != -1) or (weatherCondition.find('Snow') != -1):
        # blue
        turnOn = light_colors[2]

    # turn on green light to indicate success
    turnOnGPIOLight(light_colors[3])
    
    # log the output for successful run
    logging.info("color to light has been found to be " + turnOn)
    turnOnGPIOLight(turnOn)
except Exception as error:
    # when error occurs in call, show red light so we know an issue happend
    turnOnGPIOLight(light_colors[4])
    logging.info('exception occured')
    logging.info(error)

logging.info("program finished")
