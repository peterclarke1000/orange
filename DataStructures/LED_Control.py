#! /usr/bin/env python3
import serial
import time



serialcom = serial.Serial('/dev/cu.usbmodem1224201', baudrate=9600, timeout=1)




print("program to control and LED on the Arduino board")
while True:
    i = input(" input on/off): ").strip()
    if i in ['exit','q']:
        print("program exiting")
        break
    serialcom.write(i.encode())
    time.sleep(0.2)
    print(serialcom.readline().decode('ascii'))

serialcom.close()

