import RPi.GPIO as IO
import time

IO.setwarnings(False)

IO.setmode(IO.BCM)
IO.setup(12, IO.OUT) #motor1
IO.setup(13, IO.OUT) #moto12

IO.setup(17, IO.OUT,initial=IO.LOW) #enable1.1
IO.setup(27, IO.OUT,initial=IO.HIGH) #enable 1.2

IO.setup(22, IO.OUT,initial=IO.HIGH) #enable 2.1
IO.setup(23, IO.OUT,initial=IO.LOW) #enable 2.2

m1 = IO.PWM(12,10000);
m2 = IO.PWM(13,10000);   

def motorsInit():
    time.sleep(1)
    
def motor1Yonuileri():
    
    m1.ChangeDutyCycle(0)
    IO.output(17,IO.LOW);
    IO.output(27,IO.HIGH);    
    
def motor1YonuGeri():
    m1.ChangeDutyCycle(0)
    IO.output(17,IO.HIGH);
    IO.output(27,IO.LOW);
    
def motor2Yonuileri():
    
    m2.ChangeDutyCycle(0)
    IO.output(22,IO.LOW);
    IO.output(23,IO.HIGH);    
    
def motor2YonuGeri():
    
    m2.ChangeDutyCycle(0)
    IO.output(17,IO.HIGH);
    IO.output(27,IO.LOW);
    
    
def motorStart(dutycyle=0):
    
    IO.output(17,IO.LOW);
    IO.output(27,IO.HIGH);
    
    IO.output(22,IO.LOW);
    IO.output(23,IO.HIGH);
    
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
    
def wait(sec):
    time.sleep(sec)