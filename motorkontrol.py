import RPi.GPIO as IO
import time



def motorsInit():
    IO.setmode(IO.BCM)
    m1 = IO.setup(12, IO.OUT)
    m2 = IO.setup(13, IO.OUT)

def motorStart(dutycyle=1000):
    m1.start(dutycycle)
    m2.start(dutycycle)
   
def motorsStop():
    m1.ChangeDutyCycle(0)
    m2.ChangeDutyCycle(0)

def motor1speed(speed = 0):
    m1.ChangeDutyCycle(speed)

def motor2speed(speed = 0):
    m2.ChangeDutyCycle(speed)