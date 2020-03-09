import RPi.GPIO as IO
import time

GPIO.setmode(GPIO.BCM)

motor1_BCM_pin = 12;
motor2_BMC_pin = 13;

IO.setup(motor1_BMC_pin, IO.OUT)
IO.setup(motor2_BMC_pin, IO.OUT)

m1 = IO.PWM(motor1_BMC_pin,1000);
m2 = IO.PWM(motor2_BMC_pin,1000);
    
def motorsInit():
    time.sleep(1)
    
def motorStart(initdutycyle=0):
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