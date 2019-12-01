import serial
import RPi.GPIO as GPIO
import time

ser = serial.Serial("/dev/ttyACM1",9600)
ser.baudrate=9600
def blink(pin):
    GPIO.output(pin,GPIO.HIGH)
    time.sleep(1)
    GPIO.output(pin,GPIO.LOW)
    time.sleep(1)
    return

GPIO.setmode(GPIO.BOARD)
GPIO.setup(22, GPIO.OUT)
while True:
    read_ser = ser.readline()
    read_ser = read_ser.decode('ASCII')
    read_ser = read_ser.split()
    #read_ser = read_ser.split()
    try:
        print(float(read_ser[0]))
    except:
        print("hello")
   