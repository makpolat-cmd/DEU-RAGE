import RPi.GPIO as IO
import time

m1 = IO.setup(12, IO.OUT,5,6)
m2 = IO.setup(13, IO.OUT,5,6)
    
def motorsInit():
    IO.setmode(IO.BCM)
    time.sleep(1)
    
def motorStart(dutycyle=1000):
    m1.start(dutycyle)
    m2.start(dutycyle)
    time.sleep(1)
   
def motorsStop():
    m1.ChangeDutyCycle(0)
    m2.ChangeDutyCycle(0)
    time.sleep(1)

def motor1speed(speed = 0):
    m1.ChangeDutyCycle(speed)
    time.sleep(1)

def motor2speed(speed = 0):
    m2.ChangeDutyCycle(speed)
    time.sleep(1)