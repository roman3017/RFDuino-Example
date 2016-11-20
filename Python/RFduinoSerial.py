#!/usr/bin/env python
# RFDuinoSerial.py roman3017
#
# This test script connects to the RFduino, generates data and sends
# it to RFduino over serial connection and receives it back over BLE
#

from RFduino import RFduino
from threading import Timer
import time
import serial
import sys

PORT = "/dev/ttyUSB1"
BAUDRATE = 57600
DONGLE_ID = "hci0"
RFDUINO_NAME = "RFduino"
DELAY = 5

device = RFduino(DONGLE_ID, RFDUINO_NAME)
ser = serial.Serial(
	port=PORT,
	baudrate=BAUDRATE,
	parity=serial.PARITY_NONE,
	stopbits=serial.STOPBITS_ONE,
	bytesize=serial.EIGHTBITS)

def transferData():
	data = "0123456789abcde@"
	ser.write(str(data))
	print "data sent: [", data, "]", time.time()
	Timer(1, transferData, ()).start()

def main():
	if ser.isOpen():
		ser.close()
	ser.open()

	if (not device.find()):
		print "RFduino not found."
		ser.close()
		sys.exit(-1)

	transferData()
	while True:
		data = device.read()
		print "data received: [", data, "]", time.time()

if __name__ == "__main__":
	main()

