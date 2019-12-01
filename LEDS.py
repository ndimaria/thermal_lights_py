import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

red = 22
yellow=27
green=17
GPIO.setup(red,GPIO.OUT)
GPIO.setup(yellow,GPIO.OUT)
GPIO.setup(green,GPIO.OUT)

def blink_led(led):
    print("LED on")
    GPIO.output(led,GPIO.HIGH)
    time.sleep(1)
    print("LED off")
    GPIO.output(led,GPIO.LOW)
    time.sleep(1)

while(True):
    blink_led(red)
    blink_led(yellow)
    blink_led(green)
    
