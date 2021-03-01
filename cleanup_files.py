import os 
import logging

# logging
logging.basicConfig(filename='/home/pi/weather-lamp/history_delete.log',format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.INFO)

logging.info("program started")

filename="/home/pi/weather-light/history_daily.log"

try: 
    logging.info("starting the removal of the file") 
    os.remove(filename)
    logging.info("file has been deleted successfully")
except Exception as error:
    logging.info('exception occured')
    logging.info(error)

logging.info("program finished")