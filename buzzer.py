import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

buzzer = 5

GPIO.setup(buzzer, GPIO.OUT)

while(True):
    print("LED on")
    GPIO.output(buzzer,GPIO.HIGH)
    time.sleep(1)
    print("LED off")
    GPIO.output(buzzer,GPIO.LOW)
    time.sleep(1)