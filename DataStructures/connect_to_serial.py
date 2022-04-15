#! /usr/bin/env python3

import serial

ser = serial.Serial('/dev/cu.usbmodem1224201',baudrate=9600,timeout=1)

for i in range(20):
    Data = ser.readline()
    print(Data)

print("now closing serial port : " + ser.name)

ser.close()


