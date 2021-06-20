import RPi.GPIO as GPIO
import time
from time import sleep
import PiWarsTurkiyeRobotKiti2019

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

TRIG = 15
ECHO = 14
GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)
motorlar = PiWarsTurkiyeRobotKiti2019.MotorKontrol()
m=400
donus=False
while True:
    time.sleep(1)
    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)
    StartTimeO = time.time()
    StopTimeO = time.time()
    while GPIO.input(ECHO) == 0:
        StartTimeO = time.time()
    while GPIO.input(ECHO) == 1:
        StopTimeO = time.time()
    zmn = StopTimeO - StartTimeO
    mesafe = round((zmn * 34300) / 2)
    if(mesafe <= 3.7):
        motorlar.hizlariAyarla(0,0)
        donus=False
        sleep(1.5)
        while donus==False:
            if mesafe>=100:
                donus=True
            else:
                motorlar.hizlariAyarla(600,600)
    elif(mesafe >= 50):
        motorlar.hizlariAyarla(-400,-400)
    else:
        motorlar.hizlariAyarla(-240,-240)
