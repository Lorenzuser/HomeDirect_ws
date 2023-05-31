#!/usr/bin/env python

import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

reader = SimpleMFRC522()
try:
	while True:
		text = input('New data:')
		# Entferne Leerzeichen
		text = text.replace(" ", "")
		# Prüfe ob nur Buchstaben
		if text.isalpha():
			break
		else:
			print("Please only use letters")
			
	print("Now place your tag to write")
	reader.write(text)
	print("Written")
finally:
	GPIO.cleanup()
