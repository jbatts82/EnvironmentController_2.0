###############################################################################
# File Name  : TheSensorApp.py
# Date       : 03/13/2021
# Description: 
###############################################################################

import asyncio
from time import sleep
from config import Config
from temp_sensing.DHT11 import DHT11
from support import log
from support import div
from data.DB_App import DataBase_App
from control.leds import leds
from control.plug import KasaPlug
import threading

last_good_reading = None
the_config = Config()

def plausiblity_check(current_data):

	if current_data.error_state == True:
		return None

	if current_data.temperature_f > the_config.plausible_high:
		return False

	if current_data.temperature_f < the_config.plausible_low:
		return False

	global last_good_reading
	if last_good_reading == None: 
		last_good_reading = current_data
		return True

	difference_f = abs(current_data.temperature_f - last_good_reading.temperature_f)
	if difference_f > the_config.plausible_degrees:
		return False
	last_good_reading = current_data

	return True


def read_sensor(idx):
	div()
	the_leds.turn_on(idx)
	sensor_array[idx].process_sensor()
	current_data = sensor_array[idx].get_current_data()
	result = plausiblity_check(current_data)
	if result == True: #clean
		the_database.write_sensor_data(current_data)
		log("DB Status", "Saved to database")
		sleep(1)
	else:
		error_count = error_count + 1
	the_leds.turn_off(idx)



if __name__ == '__main__':
	log("Starting Main System", __file__)
	div()
	
	# initialize database
	div()
	the_database = DataBase_App(the_config)

	# initialize leds
	div()
	the_leds = leds(the_config)

	# initialize temp sensing
	sensor1 = DHT11(the_config)
	sensor2 = DHT11(the_config)
	sensor3 = DHT11(the_config)
	sensor4 = DHT11(the_config)

	sensor_array = [sensor1, sensor2, sensor3, sensor4]

	cnt = 0
	error_count = 0
	
	while True:
		for idx, sensor in enumerate(sensor_array):
			div()
			read_sensor(idx)
	#end main loop