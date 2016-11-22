# run this on the pi
import RPi.GPIO as GPIO
import time

# import urllib3 
import json
# print(urllib3.__version__)

import requests

count = 1

url = "http://intellibin.herokuapp.com/bin/update/"
route = "/bin/update"
header = {'Content-Type': 'application/json'}

while (True):
    # init things needed for sensing
    GPIO.setmode(GPIO.BCM)
    # outout pin that trigers the sensor GIPO 23 (pin 16)
    TRIG = 23
    # input pin which reads return signal from sensor GPIO 24 (pin 18)
    ECHO = 24

    print("Measuring distance, iteration: " + str(count))
    # set general purpose I/O ports
    GPIO.setup(TRIG, GPIO.OUT)
    GPIO.setup(ECHO, GPIO.IN)

    # set trigger to low
    GPIO.output(TRIG, False)
    print("Waiting for Sensor to Settle")
    time.sleep(2) # wait for sensor to settle

    # set signal
    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)

    # listen to input pin
    while GPIO.input(ECHO) == 0:
        pulse_start = time.time()

    while GPIO.input(ECHO) == 1:
        pulse_end = time.time()

    pulse_duration = pulse_end - pulse_start
    # print("~ Pulse duration: %smicro seconds" % pulse_duration)
    distance = pulse_duration * 17150
    # print("~ Distance: %scm"  % distance)
    # distance = round(distance, 2)
    print("Distance: %scm" % str(distance))
    if distance < 24:
        if distance < 22:
            print("~~THRESHOLD: BIN GREATHER THAN 3/4 FULL!!~~")
        else:
            print("~~THRESHOLD: BIN 3/4 FULL~~")
    data = {'dist': distance}

    encoded_body = json.dumps(dict([
        ('id', 1),('distance', distance)
    ]))
    print("http post: " + encoded_body)
    # http = urllib3.PoolManager()
    # r = http.request('POST', url, 
    #          headers={'Content-Type': 'application/json'}, 
    #        body=encoded_body)

    # req = urllib.request(url, data=params, headers=header)
   #  res = urllib.request.urlopen(req)
    # response = urllib2.urlopen(url, data)
    # response.request ('POST', route, data)
     # 
    # try:
        # r = requests.post(url, headers=header, data=encoded_body)
    # except:
        # pass
    # print(r.status_code, r.reason)
    # similar to f.close i am assuming
    GPIO.cleanup()
    time.sleep(1)
    count += 1