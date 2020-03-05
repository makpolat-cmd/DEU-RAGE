import RPi.GPIO as IO
import time


m1 = IO.setup(12, IO.OUT)
m2 = IO.setup(13, IO.OUT)
    
def motorsInit():
    time.sleep(1)
    
def motorStart(initdutycyle=1000):
    m1.start(initdutycyle)
    m2.start(initdutycyle)
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