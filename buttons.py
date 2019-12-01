import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

redButton = 21
whiteButton = 20
blueButton = 16
GPIO.setup(redButton,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(whiteButton,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(blueButton,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(22, GPIO.OUT)
GPIO.setup(27, GPIO.OUT)
GPIO.setup(17, GPIO.OUT)

    
def allOff():
    GPIO.output(22,GPIO.LOW)
    GPIO.output(27,GPIO.LOW)
    GPIO.output(17,GPIO.LOW)
buttonMode = 0
while(1):
    if(GPIO.input(redButton)==GPIO.HIGH):
      buttonMode = 0
      time.sleep(.1)
      print("red")
         
    elif(GPIO.input(whiteButton)==GPIO.HIGH):
      buttonMode =1
      time.sleep(.1)
      print("white")
    elif(GPIO.input(blueButton)==GPIO.HIGH):
      buttonMode=2
      time.sleep(.1)
      print("blue")
    
    if buttonMode == 0:
        allOff()
        GPIO.output(22,1)
        time.sleep(.10)
        GPIO.output(22,0)
        time.sleep(.10)
    elif buttonMode == 1:
        allOff()
        GPIO.output(27,1)
        time.sleep(.10)
        GPIO.output(27,0)
        time.sleep(.10)
    elif buttonMode == 2:
        allOff()
        GPIO.output(17,1)
        time.sleep(.10)
        GPIO.output(17,0)
        time.sleep(.10)      
