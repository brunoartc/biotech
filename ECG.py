#!/usr/bin/python

import serial
import syslog
import time
import json

#The following line is for serial over GPIO
port = '/dev/ttyACM0'


ard = serial.Serial(port,115200,timeout=0)

i = 0




while (1):



    while not ard.inWaiting():
        pass
    # Serial read section
    msg = ard.readline()
    print ("Message from arduino: ")
    print(msg.decode("utf-8"))
    mesage_json = json.loads(msg.decode("utf-8").replace("'", "\""))
    with open("result.csv", "a") as myfile:
        myfile.write("BPM:,{}\t".format(mesage_json.bpm))



     

    i = i + 1
else:
    print ("Exiting")
exit()
