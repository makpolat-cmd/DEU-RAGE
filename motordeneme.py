import motorkontrol as mc

mc.motorsInit()
mc.motorStart()
mc.motor2Yonuileri()
mc.motor2speed(80)

mc.wait(5);
mc.motor2speed(0)
print("program bitti")