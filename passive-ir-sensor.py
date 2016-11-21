import RPi.GPIO as GPIO 
import time
GPIO.setmode(GPIO.BCM)

IR_PIN = 7			# output signal
GPIO.setup(IR_PIN, GPIO.IN)

threshold = 12

count = 0
person = 0
try:
	time.sleep(2)
	while(True):
		if person == threshold:
			print"PERSON"
			time.sleep(2)

			person = 0
		if GPIO.input(IR_PIN):
			print "iteration: ", count, "Motion Detected"
			## GPIO.output(IR_PIN, GPIO.HIGH)
			# time.sleep(1)
			# GPIO.output(IR_PIN, GPIO.LOW)
			person += 1

		else:
			print "iteration: ", count, "No Motion"
			if person < threshold:
				person = 0
		time.sleep(1)
		count += 1
except KeyboardInterrupt:	 # catches ctrl+c
	print("Quit Passive IR Sensor")
	GPIO.cleanup()

