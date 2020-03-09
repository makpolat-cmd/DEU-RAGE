import motorkontrol as mc


mc.motorsInit() # start 1000 Hertz normally
mc.motorStart() #duty cycle
mc.motor1speed(40) # change duty cycle
mc.motor2speed(40)# change duty cycle
mc.motorsStop() # stop both motors