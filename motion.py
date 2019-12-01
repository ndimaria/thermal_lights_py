import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.IN)         #Read output from PIR motion sensor
GPIO.setup(22, GPIO.OUT)         #LED output pin

time.sleep(30)
print("ready")
while True:
    i=GPIO.input(4)
    if i==0:                 #When output from motion sensor is LOW
        print("No intruders",i)
        GPIO.output(22, 0)  #Turn OFF LED
        time.sleep(5)
    elif i==1:               #When output from motion sensor is HIGH
        print("Intruder detected",i)
        GPIO.output(22, 1)  #Turn ON LED
        time.sleep(5)