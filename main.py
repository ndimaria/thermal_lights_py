import RPi.GPIO as GPIO
import time
import threading
import serial

ser = serial.Serial("/dev/ttyACM0",9600)
ser.baudrate=9600

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

timeLeft = True

redLED = 22
yellowLED = 27
greenLED = 17

GPIO.setup(redLED,GPIO.OUT)
GPIO.setup(yellowLED,GPIO.OUT)
GPIO.setup(greenLED,GPIO.OUT)

redButton = 21
whiteButton = 20
blueButton = 16

GPIO.setup(redButton,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(whiteButton,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(blueButton,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)

buzzer = 5

GPIO.setup(buzzer, GPIO.OUT)

motion = 4
GPIO.setup(motion, GPIO.IN)

buttonMode = 0 

lightThreshold = 700

def getTemp():
    read_ser = ser.readline()
    read_ser = read_ser.decode('ASCII')
    read_ser = read_ser.split()
    try:
        return float(read_ser[0])
    except:
        return "No Data"

def getLight():
    read_ser = ser.readline()
    read_ser = read_ser.decode('ASCII')
    read_ser = read_ser.split()
    try:
        return int(read_ser[2])
    except:
        return "No Data"
    
def determineLED(temp):
    if(temp > 75):
        return redLED
    elif(temp>50):
        return yellowLED
    else:
        return greenLED
    
def detectMotion(pin):
    i=GPIO.input(pin)
    if i ==1:
        return True
    else:
        return False
    
def allOff():
    GPIO.output(redLED,GPIO.LOW)
    GPIO.output(yellowLED,GPIO.LOW)
    GPIO.output(greenLED,GPIO.LOW)

def ledOn(pin):
    GPIO.output(pin, GPIO.HIGH)

def ledOff(pin):
    GPIO.ouput(pin, GPIO.LOW)

def beep(pin):
    GPIO.output(pin,GPIO.HIGH)
    time.sleep(.5)
    GPIO.output(pin,GPIO.LOW)

def timeUp():
    global timeLeft
    timeLeft= False


allOff()
#time.sleep(30)
print("ready")

on= False

while(True):
    
    if buttonMode == 0:
        light = getLight()
        if light == "No Data":
            print("hi there")
        elif light > lightThreshold:
          whichLED = determineLED(getTemp());
          if(not on):
              beep(buzzer);
              ledOn(whichLED);
              on = True
        else:
            if(on):
                beep(buzzer);
                allOff()
                on = False
            
            
    if buttonMode == 1:
        if timeLeft == False:
            if(on):
                allOff()
                beep(buzzer)
                on=False

        if detectMotion(motion):
            if(not on):
                whichLED = determineLED(getTemp());
                ledOn(whichLED)
                beep(buzzer)
                on=True
            print("detected")
            time.sleep(18)
            timeLeft = True
            timer = threading.Timer(10.0, timeUp)
            timer.start()
            print("timer started")
            
    if buttonMode == 2:
        light = getLight()
        if timeLeft == False:
            if(on):
                allOff()
                beep(buzzer)
                on=False

        if detectMotion(motion) and light > lightThreshold:
            if(not on):
                whichLED = determineLED(getTemp());
                ledOn(whichLED)
                beep(buzzer)
                on=True
            print("detected")
            time.sleep(18)
            timeLeft = True
            timer = threading.Timer(10.0, timeUp)
            timer.start()
            print("timer started")
            
    if(GPIO.input(redButton)==GPIO.HIGH):
      buttonMode =0
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