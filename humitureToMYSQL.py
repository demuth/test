'''
**********************************************************************
* Filename    : dht11.py
* Description : test for SunFoudner DHT11 humiture & temperature module
* Author      : Dream
* Brand       : SunFounder
* E-mail      : service@sunfounder.com
* Website     : www.sunfounder.com
* Update      : Dream    2016-09-30    New release
**********************************************************************
'''
import RPi.GPIO as GPIO
import time
import mysql.connector
import random
import datetime

DHTPIN = 17

GPIO.setmode(GPIO.BCM)

MAX_UNCHANGE_COUNT = 100

STATE_INIT_PULL_DOWN = 1
STATE_INIT_PULL_UP = 2
STATE_DATA_FIRST_PULL_DOWN = 3
STATE_DATA_PULL_UP = 4
STATE_DATA_PULL_DOWN = 5

def read_dht11_dat():
	GPIO.setup(DHTPIN, GPIO.OUT)
	GPIO.output(DHTPIN, GPIO.HIGH)
	time.sleep(0.05)
	GPIO.output(DHTPIN, GPIO.LOW)
	time.sleep(0.02)
	GPIO.setup(DHTPIN, GPIO.IN, GPIO.PUD_UP)

	unchanged_count = 0
	last = -1
	data = []
	while True:
		current = GPIO.input(DHTPIN)
		data.append(current)
		if last != current:
			unchanged_count = 0
			last = current
		else:
			unchanged_count += 1
			if unchanged_count > MAX_UNCHANGE_COUNT:
				break

	state = STATE_INIT_PULL_DOWN

	lengths = []
	current_length = 0

	for current in data:
		current_length += 1

		if state == STATE_INIT_PULL_DOWN:
			if current == GPIO.LOW:
				state = STATE_INIT_PULL_UP
			else:
				continue
		if state == STATE_INIT_PULL_UP:
			if current == GPIO.HIGH:
				state = STATE_DATA_FIRST_PULL_DOWN
			else:
				continue
		if state == STATE_DATA_FIRST_PULL_DOWN:
			if current == GPIO.LOW:
				state = STATE_DATA_PULL_UP
			else:
				continue
		if state == STATE_DATA_PULL_UP:
			if current == GPIO.HIGH:
				current_length = 0
				state = STATE_DATA_PULL_DOWN
			else:
				continue
		if state == STATE_DATA_PULL_DOWN:
			if current == GPIO.LOW:
				lengths.append(current_length)
				state = STATE_DATA_PULL_UP
			else:
				continue
	if len(lengths) != 40:
		print "Data not good, skip"
		return False

	shortest_pull_up = min(lengths)
	longest_pull_up = max(lengths)
	halfway = (longest_pull_up + shortest_pull_up) / 2
	bits = []
	the_bytes = []
	byte = 0

	for length in lengths:
		bit = 0
		if length > halfway:
			bit = 1
		bits.append(bit)
	print "bits: %s, length: %d" % (bits, len(bits))
	for i in range(0, len(bits)):
		byte = byte << 1
		if (bits[i]):
			byte = byte | 1
		else:
			byte = byte | 0
		if ((i + 1) % 8 == 0):
			the_bytes.append(byte)
			byte = 0
	print the_bytes
	checksum = (the_bytes[0] + the_bytes[1] + the_bytes[2] + the_bytes[3]) & 0xFF
	if the_bytes[4] != checksum:
		print "Data not good, skip"
		return False

	return the_bytes[0], the_bytes[2]

def main():
	print "Raspberry Pi wiringPi DHT11 Temperature test program\n"
	while True:
		result = read_dht11_dat()
		if result:
			humidity, temperature = result
			print "humidity: %s %%,  Temperature: %s C`" % (humidity, temperature)
			f= open("TestResults.txt","a+")
                        f.write("humidity: %s %%, temperature: %s C`\n" % (humidity, temperature))
                        f.close()

#code relating to mySQL begins here

			cnx = mysql.connector.connect(user='root', password='rhoades303', host='localhost', database='embedded17')

			cursor = cnx.cursor()

			my_created = time.strftime("%Y-%m-%d %H:%M:%S")

			add_data = ("INSERT INTO humiditure (temperature, humidity, created) VALUES (%s, %s, %s)")

			data_data = (temperature, humidity, my_created)

			cursor.execute(add_data, data_data)
			humiditure_id = cursor.lastrowid

			cnx.commit()

			cursor.close()

			DB_NAME = 'embedded17'

			TABLES = {}
			TABLES['humiditure'] = (
			        "CREATE TABLE `humiditure` ("
			        "`humiditure_id` int(11) NOT NULL DEFAULT NULL AUTO_INCREMENT,"
			        "`temperature` varchar(32) NULL DEFAULT NULL,"
			        "`humidity` varchar(32) NULL DEFAULT NULL,"
			        "`created` datetime NOT NULL DEFAULT 0000-00-00 00:00:00,"
			        "PRIMARY KEY (`humiditure_id`)"
			        ")ENGINE=InnoDB")

			cnx.close()

#code relating to mySQL end here

		time.sleep(4)

def destroy():
	GPIO.cleanup()

if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt:
		destroy() 
