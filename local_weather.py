import logging
import requests

# logging
logging.basicConfig(filename='history_daily.log',format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.INFO)

# LED colors
light_colors = ['yellow', 'white', 'green', 'blue', 'red', 'blue',]

# examples to test with
# florida
# https://api.weather.gov/gridpoints/MFL/109,70/forecast/hourly
# south dakota
# https://api.weather.gov/gridpoints/ABR/54,43/forecast/hourly

# when endpoint fails it should show a red light, you can try this with this incorrect URL
# weatherURL = "htt2222222ps://api.weather.gov/gridpoints/AKQ/38,80/forecast/hourly"

# weather call
weatherURL = "https://api.weather.gov/gridpoints/AKQ/38,80/forecast/hourly"

# figure out which light to turn on
turnOn = ''

try:
    # call weather service
    response = requests.get(weatherURL)
    logging.info("weather service API was called with a return status code of " + str(response.status_code))

    # parse JSON
    hourlyWeather = response.json()
    properties = hourlyWeather["properties"]
    periods = properties["periods"]
    rightNow = periods[0]
    weatherCondition = rightNow["shortForecast"]

    # log weather condition that was just called
    print(weatherCondition)

    # figure out which light to turn on
    if (weatherCondition.find('Sunny')):
        # yellow
        turnOn = light_colors[0]
    elif (weatherCondition.find('Clear')):
        # white
        turnOn = light_colors[1]
    elif (weatherCondition.find('Cloudy')):
        # green
        turnOn = light_colors[2]
    elif (weatherCondition.find('Showers')):
        # blue
        turnOn = light_colors[3]
except Exception as error:
    # when error occurs in call, show red light so we know an issue happend
    turnOn = light_colors[4]
    logging.info('exception occured')
    logging.info(error)
 
print("program finished")
print(turnOn)